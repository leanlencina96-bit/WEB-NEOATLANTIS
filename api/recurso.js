// api/recurso.js
// Función serverless (Vercel). Recibe el formulario de las páginas /recursos/* (nombre, email, WhatsApp opcional, a qué se dedica)
// y lo guarda en Baserow, tabla «Suscriptores recursos» (Marketing NeoAtlantis).
// El token solo puede CREAR filas en esa tabla (no lee ni borra nada). Vive en las variables de entorno de Vercel:
//   BASEROW_URL · BASEROW_RECURSOS_TABLA · BASEROW_RECURSOS_TOKEN

const intentos = new Map();
function ipDe(req) {
  const f = req.headers['x-forwarded-for'];
  return f ? f.split(',')[0].trim() : (req.socket?.remoteAddress || 'desconocida');
}
function dentroDelLimite(ip, max = 4, ventanaMs = 60 * 1000) {
  const ahora = Date.now();
  const h = (intentos.get(ip) || []).filter((t) => ahora - t < ventanaMs);
  if (h.length >= max) { intentos.set(ip, h); return false; }
  h.push(ahora); intentos.set(ip, h);
  if (intentos.size > 500) for (const [k, v] of intentos) if (!v.some((t) => ahora - t < ventanaMs)) intentos.delete(k);
  return true;
}

const DEDICA = ['Tengo un negocio', 'Trabajo en relación de dependencia', 'Soy creador de contenido', 'Estudio', 'Otro'];

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Método no permitido' });
  if (!dentroDelLimite(ipDe(req))) return res.status(429).json({ error: 'Muchos intentos seguidos.' });

  const { nombre, email, whatsapp, dedica, recurso, origen, novedades, empresa, t0 } = req.body || {};
  // trampa para robots: campo oculto o envío en menos de 2 segundos → "ok" sin guardar
  if (empresa || (Number(t0) && Date.now() - Number(t0) < 2000)) return res.status(200).json({ ok: true });

  const n = String(nombre || '').trim(), e = String(email || '').trim().toLowerCase();
  if (n.length < 2 || n.length > 80) return res.status(400).json({ error: 'Escribí tu nombre.' });
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e) || e.length > 120) return res.status(400).json({ error: 'Revisá el email.' });
  const rec = String(recurso || '').replace(/[^a-z0-9-]/gi, '').slice(0, 40);
  const ori = String(origen || '').slice(0, 200);
  const wa = String(whatsapp || '').replace(/[^\d+\s()-]/g, '').trim().slice(0, 30);

  const base = (process.env.BASEROW_URL || '').replace(/\/$/, ''), tabla = process.env.BASEROW_RECURSOS_TABLA, token = process.env.BASEROW_RECURSOS_TOKEN;
  if (!base || !tabla || !token) {
    console.error('Faltan variables BASEROW_* para /api/recurso');
    return res.status(500).json({ error: 'No se pudo guardar.' });
  }
  const fila = { 'Nombre': n, 'Email': e, 'Recurso': rec, 'Origen': ori, 'Acepta novedades': !!novedades, 'Estado': 'Nuevo' };
  if (wa.replace(/\D/g, '').length >= 6) fila['WhatsApp'] = wa;
  if (DEDICA.includes(dedica)) fila['A qué se dedica'] = dedica;
  try {
    const r = await fetch(`${base}/api/database/rows/table/${tabla}/?user_field_names=true`, {
      method: 'POST',
      headers: { 'Authorization': `Token ${token}`, 'Content-Type': 'application/json', 'User-Agent': 'neoatlantis-web-recursos/1.0' },
      body: JSON.stringify(fila),
      signal: AbortSignal.timeout(15000),
    });
    if (!r.ok) { console.error('Baserow respondió', r.status); return res.status(502).json({ error: 'No se pudo guardar.' }); }
    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Error con Baserow', err?.message);
    return res.status(502).json({ error: 'No se pudo guardar.' });
  }
}
