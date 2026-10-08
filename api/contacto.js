// api/contacto.js
// Función serverless (Vercel). Recibe el formulario de contacto de neoatlantis.com.ar
// y lo reenvía a n8n, que lo carga en el CRM y le avisa a Leandro por Telegram.
// El token de n8n queda en las variables de entorno: nunca llega al navegador.

const intentos = new Map(); // ip -> [timestamps] (límite aproximado: Vercel puede tener varias instancias)

function ipDe(req) {
  const f = req.headers['x-forwarded-for'];
  return f ? f.split(',')[0].trim() : (req.socket?.remoteAddress || 'desconocida');
}
function dentroDelLimite(ip, max = 3, ventanaMs = 60 * 1000) {
  const ahora = Date.now();
  const h = (intentos.get(ip) || []).filter((t) => ahora - t < ventanaMs);
  if (h.length >= max) { intentos.set(ip, h); return false; }
  h.push(ahora); intentos.set(ip, h);
  if (intentos.size > 500) for (const [k, v] of intentos) if (!v.some((t) => ahora - t < ventanaMs)) intentos.delete(k);
  return true;
}

const NECESIDADES = [
  'Una web para mi consultorio', 'Turnos online y recordatorios', 'Mejorar mi web actual',
  'Aparecer en Google Maps', 'Quiero un diagnóstico gratis',
];

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Método no permitido' });
  if (!dentroDelLimite(ipDe(req))) {
    return res.status(429).json({ error: 'Mandaste varios mensajes seguidos. Esperá un minuto y volvé a intentar.' });
  }

  const { nombre, email, whatsapp, necesidad, mensaje, empresa, t0 } = req.body || {};
  // Trampa para robots: un campo oculto que una persona nunca completa, y un formulario
  // enviado en menos de 3 segundos. Se responde "ok" para no darles pistas.
  if (empresa || (Number(t0) && Date.now() - Number(t0) < 3000)) return res.status(200).json({ ok: true });

  const n = String(nombre || '').trim(), e = String(email || '').trim(), w = String(whatsapp || '').trim();
  if (n.length < 2 || n.length > 80) return res.status(400).json({ error: 'Ingresá tu nombre.' });
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e) || e.length > 120) return res.status(400).json({ error: 'Ingresá un email válido.' });
  if (w && w.replace(/\D/g, '').length < 8) return res.status(400).json({ error: 'El WhatsApp parece incompleto (mínimo 8 dígitos).' });
  const nec = NECESIDADES.includes(necesidad) ? necesidad : '';
  const msj = String(mensaje || '').trim().slice(0, 1500);

  const url = process.env.N8N_CONTACTO_URL, token = process.env.N8N_CONTACTO_TOKEN;
  if (!url || !token) {
    console.error('Faltan N8N_CONTACTO_URL o N8N_CONTACTO_TOKEN');
    return res.status(500).json({ error: 'No pudimos enviar tu mensaje. Escribinos a neoatlantisia@gmail.com.' });
  }
  try {
    const r = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-Contacto-Token': token },
      body: JSON.stringify({ nombre: n, email: e, whatsapp: w, necesidad: nec, mensaje: msj }),
      signal: AbortSignal.timeout(20000),
    });
    if (!r.ok) {
      console.error('n8n respondió', r.status);
      return res.status(502).json({ error: 'No pudimos enviar tu mensaje. Escribinos a neoatlantisia@gmail.com.' });
    }
    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Error enviando a n8n:', err?.name || err);
    return res.status(502).json({ error: 'No pudimos enviar tu mensaje. Escribinos a neoatlantisia@gmail.com.' });
  }
}
