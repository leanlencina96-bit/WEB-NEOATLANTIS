// api/autodiagnostico.js
// Recibe el autodiagnóstico de neoatlantis.com.ar/diagnostico/ y lo manda al mismo workflow de n8n que el formulario de
// contacto: crea el prospecto en el CRM (Fuente Web) con las respuestas en las notas y le avisa a Leandro por Telegram.
// El cálculo se repite acá con los datos crudos (no se confía en lo que manda el navegador). El token de n8n nunca llega al navegador.

const intentos = new Map();
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

const OPC = {
  profesion: ['Odontología', 'Psicología', 'Medicina', 'Kinesiología o nutrición', 'Otra'],
  turnosHoy: ['WhatsApp o teléfono', 'Una secretaria', 'Una app (Doctoralia u otra)', 'Mi propia web'],
  recordatorios: ['No mando', 'A mano por WhatsApp', 'Automáticos'],
  web: ['No tengo', 'Sí, pero sin turnos', 'Sí, con turnos online'],
  maps: ['Sí', 'No', 'No sé'],
};
const num = (v, min, max) => { const n = Number(v); return Number.isFinite(n) ? Math.min(max, Math.max(min, Math.round(n))) : null; };
const llano = (t) => String(t || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().trim();
const opcion = (lista, v) => lista.find((o) => llano(o) === llano(v)) || '';
const pesos = (n) => 'ARS ' + Math.round(n).toLocaleString('es-AR');

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Método no permitido' });
  if (!dentroDelLimite(ipDe(req))) return res.status(429).json({ error: 'Mandaste varios seguidos. Esperá un minuto y volvé a intentar.' });

  const b = req.body || {};
  if (b.empresa || (Number(b.t0) && Date.now() - Number(b.t0) < 8000)) return res.status(200).json({ ok: true }); // trampa para robots

  const nombre = String(b.nombre || '').trim(), whatsapp = String(b.whatsapp || '').trim(), email = String(b.email || '').trim();
  if (nombre.length < 2 || nombre.length > 80) return res.status(400).json({ error: 'Ingresá tu nombre.' });
  if (whatsapp.replace(/\D/g, '').length < 8) return res.status(400).json({ error: 'Ingresá un WhatsApp para que te pasemos el resultado.' });
  if (email && (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 120)) return res.status(400).json({ error: 'El email no parece válido.' });

  const r = b.respuestas || {};
  const d = {
    profesion: opcion(OPC.profesion, r.profesion), turnosHoy: opcion(OPC.turnosHoy, r.turnosHoy), recordatorios: opcion(OPC.recordatorios, r.recordatorios),
    web: opcion(OPC.web, r.web), maps: opcion(OPC.maps, r.maps), ciudad: String(r.ciudad || '').trim().slice(0, 60),
    turnosSemana: num(r.turnosSemana, 0, 500), faltasSemana: num(r.faltasSemana, 0, 100), valor: num(r.valor, 0, 1000000), horasSemana: num(r.horasSemana, 0, 60),
  };
  const perdidaMes = (d.faltasSemana || 0) * 4.3 * (d.valor || 0);
  const resumen = `Autodiagnóstico: ${d.faltasSemana ?? '?'} faltas/sem · ~${pesos(perdidaMes)}/mes`.slice(0, 80);
  const mensaje = [
    'AUTODIAGNÓSTICO (lo completó solo en la web)',
    `Profesión: ${d.profesion || '—'} · Ciudad: ${d.ciudad || '—'}`,
    `Hoy toma turnos por: ${d.turnosHoy || '—'}`,
    `Turnos por semana: ${d.turnosSemana ?? '—'} · Faltan o cancelan tarde: ${d.faltasSemana ?? '—'} por semana`,
    `Valor de la consulta: ${d.valor ? pesos(d.valor) : '—'} → pierde ~${pesos(perdidaMes)} por mes en turnos vacíos`,
    `Recordatorios: ${d.recordatorios || '—'} · Horas por semana con los turnos: ${d.horasSemana ?? '—'}`,
    `Web: ${d.web || '—'} · Aparece en Google Maps: ${d.maps || '—'}`,
    `Le sugerimos: ${String(b.sugerido || '').slice(0, 60) || '—'}`,
    'Próximo paso: escribirle por WhatsApp para la charla de 15 minutos.',
  ].join('\n');

  const url = process.env.N8N_CONTACTO_URL, token = process.env.N8N_CONTACTO_TOKEN;
  if (!url || !token) {
    console.error('Faltan N8N_CONTACTO_URL o N8N_CONTACTO_TOKEN');
    return res.status(500).json({ error: 'No pudimos guardar tu resultado. Escribinos por WhatsApp al +54 9 341 226-9841.' });
  }
  try {
    const rr = await fetch(url, {
      method: 'POST', headers: { 'Content-Type': 'application/json', 'X-Contacto-Token': token },
      body: JSON.stringify({ nombre, email, whatsapp, necesidad: resumen, mensaje }), signal: AbortSignal.timeout(20000),
    });
    if (!rr.ok) { console.error('n8n respondió', rr.status); return res.status(502).json({ error: 'No pudimos guardar tu resultado. Escribinos por WhatsApp al +54 9 341 226-9841.' }); }
    return res.status(200).json({ ok: true });
  } catch (err) {
    console.error('Error enviando a n8n:', err?.name || err);
    return res.status(502).json({ error: 'No pudimos guardar tu resultado. Escribinos por WhatsApp al +54 9 341 226-9841.' });
  }
}
