# Arma el ebook «100 prompts para tu día a día» en PDF (sin Gamma: HTML + Edge sin ventana).
# Correr desde cualquier lado:  python herramientas/generar_ebook_prompts.py
# Salida: descargas/100-prompts-dia-a-dia.pdf (y el .html al lado, en herramientas/_ebook/, para revisarlo).
import html, os, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from contenido_100prompts import CAPITULOS, TITULO, SUBTITULO

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_ebook")
PDF = os.path.join(RAIZ, "descargas", "100-prompts-dia-a-dia.pdf")
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
e = html.escape
url = lambda p: "file:///" + os.path.join(RAIZ, p).replace("\\", "/")

CSS = f"""
@font-face{{font-family:'Inter';font-weight:300 600;src:url({url('assets/fonts/inter-latin.woff2')}) format('woff2')}}
@font-face{{font-family:'Space Grotesk';font-weight:400 700;src:url({url('assets/fonts/space-grotesk-latin.woff2')}) format('woff2')}}
@page{{size:A5;margin:0}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:Inter,sans-serif;color:#1F2937;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
h1,h2,h3{{font-family:'Space Grotesk',sans-serif;letter-spacing:-.01em}}
.pag{{width:148mm;height:210mm;padding:16mm 14mm 14mm;position:relative;page-break-after:always;overflow:hidden;background:#EDEEF1}}
.pie{{position:absolute;bottom:7mm;left:14mm;right:14mm;display:flex;justify-content:space-between;font-size:7pt;color:#6B7280}}
.oscura{{background:#05070A;color:#fff}}
.portada{{background:radial-gradient(ellipse 70% 50% at 80% 20%,rgba(76,111,255,.35),transparent 70%),radial-gradient(ellipse 60% 40% at 10% 90%,rgba(123,92,250,.30),transparent 70%),#05070A;color:#fff;display:flex;flex-direction:column;justify-content:space-between}}
.marca{{display:flex;align-items:center;gap:8px;font-family:'Space Grotesk';font-weight:600;font-size:9pt;letter-spacing:.12em}}
.marca img{{width:18px;height:18px}}
.portada .num{{font-family:'Space Grotesk';font-weight:700;font-size:120pt;line-height:.85;background:linear-gradient(120deg,#4C6FFF,#7B5CFA);-webkit-background-clip:text;color:transparent}}
.portada h1{{font-size:30pt;line-height:1.02;margin-top:6px}}
.portada .sub{{margin-top:12px;font-size:10pt;color:rgba(255,255,255,.72);max-width:105mm;font-weight:300}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;margin-top:16px}}
.chips span{{font-size:7.5pt;border:1px solid rgba(255,255,255,.28);border-radius:99px;padding:3px 9px;color:rgba(255,255,255,.85)}}
.autor{{display:flex;align-items:center;gap:10px;font-size:9pt}}
.autor img{{width:40px;height:40px;border-radius:50%;object-fit:cover;border:2px solid #4C6FFF}}
.autor small{{display:block;color:rgba(255,255,255,.6);font-size:7.5pt}}
h2.t{{font-size:19pt;color:#05070A;margin-bottom:10px}}
p{{font-size:9.5pt;line-height:1.55;margin-bottom:8px}}
ol.pasos{{list-style:none;counter-reset:p;display:grid;gap:8px;margin-top:10px}}
ol.pasos li{{counter-increment:p;background:#fff;border-radius:10px;padding:9px 12px 9px 40px;position:relative;font-size:9pt;line-height:1.45}}
ol.pasos li::before{{content:counter(p,decimal-leading-zero);position:absolute;left:12px;top:9px;font-family:'Space Grotesk';font-weight:700;color:#3554E0}}
.indice{{list-style:none;display:grid;gap:5px;margin-top:6px}}
.indice li{{display:grid;grid-template-columns:22px 1fr auto;gap:8px;background:#fff;border-radius:9px;padding:7px 11px;font-size:9pt;align-items:center}}
.indice b{{font-family:'Space Grotesk';color:#3554E0}}
.indice em{{font-style:normal;color:#6B7280;font-size:8pt}}
.cap{{display:flex;flex-direction:column;justify-content:flex-end}}
.cap .grande{{font-family:'Space Grotesk';font-weight:700;font-size:96pt;line-height:.8;color:transparent;-webkit-text-stroke:1.5px #4C6FFF}}
.cap h2{{font-size:26pt;line-height:1.05;margin:12px 0 10px}}
.cap p{{color:rgba(255,255,255,.7);font-size:10pt;max-width:110mm}}
.cap .rango{{margin-top:14px;font-size:8pt;letter-spacing:.14em;color:#B3C1FF}}
.card{{background:#fff;border-radius:12px;padding:10px 12px 11px;margin-bottom:9px;border-left:4px solid #4C6FFF;page-break-inside:avoid}}
.card h3{{font-size:10.5pt;color:#05070A;margin-bottom:5px;display:flex;gap:8px;align-items:baseline}}
.card h3 span{{font-size:8pt;color:#fff;background:linear-gradient(120deg,#4C6FFF,#7B5CFA);border-radius:99px;padding:1px 7px;flex:none}}
.card pre{{font-family:Consolas,ui-monospace,monospace;font-size:8.1pt;line-height:1.5;white-space:pre-wrap;color:#374151;background:#F5F6F9;border-radius:8px;padding:7px 9px}}
.cab{{display:flex;justify-content:space-between;font-size:7.5pt;color:#6B7280;margin-bottom:9px;letter-spacing:.06em;text-transform:uppercase}}
.cierre{{display:flex;flex-direction:column;justify-content:center;gap:12px}}
.cierre h2{{font-size:22pt;line-height:1.1}}
.cierre p{{color:rgba(255,255,255,.75)}}
.cierre .boton{{display:inline-block;background:linear-gradient(120deg,#4C6FFF,#7B5CFA);color:#fff;border-radius:99px;padding:8px 16px;font-size:9pt;text-decoration:none;font-weight:600}}
.cierre img.yo{{width:70px;height:70px;border-radius:14px;object-fit:cover}}
"""

pie = lambda n: f'<div class="pie"><span>{e(TITULO)} · Leandro Lencina</span><span>{n}</span></div>'

def construir():
    paginas, n_pag = [], 1
    paginas.append(f"""<section class="pag portada">
<div class="marca"><img src="{url('assets/isotipo.png')}" alt="">NEOATLANTIS</div>
<div><div class="num">100</div><h1>prompts para<br>tu día a día</h1><p class="sub">{e(SUBTITULO)}</p>
<div class="chips"><span>10 capítulos</span><span>Listos para copiar</span><span>Gratis</span></div></div>
<div class="autor"><img src="{url('assets/img/leandro.webp')}" alt=""><div>Leandro Lencina<small>Consultor de IA · pruebo herramientas y te las explico simple</small></div></div>
</section>""")
    n_pag += 1
    paginas.append(f"""<section class="pag"><h2 class="t">Cómo usar este ebook</h2>
<p>Cada prompt es un pedido listo para la IA. No hace falta saber nada técnico: copiás, completás y listo.</p>
<ol class="pasos">
<li>Abrí ChatGPT, Claude o Gemini. La versión gratis alcanza para todos.</li>
<li>Copiá el prompt y reemplazá lo que está entre <b>[corchetes]</b> con tus datos. Cuanto más concreto, mejor.</li>
<li>Si la respuesta no te convence, seguí la charla: «más corto», «más simple», «dame otra opción».</li>
<li>No pegues contraseñas, números de tarjeta ni datos de otras personas.</li>
<li>Revisá lo que te da. La IA se equivoca, sobre todo con fechas, precios y trámites. En salud, plata o temas legales, te ayuda a prepararte: la decisión la tomás con un profesional.</li>
</ol>{pie(n_pag)}</section>""")
    n_pag += 1
    filas = "".join(f'<li><b>{i:02d}</b><span>{e(c["nombre"])}</span><em>{(i-1)*10+1}–{i*10}</em></li>' for i, c in enumerate(CAPITULOS, 1))
    paginas.append(f'<section class="pag"><h2 class="t">Índice</h2><ol class="indice">{filas}</ol>{pie(n_pag)}</section>')
    num = 0
    for i, c in enumerate(CAPITULOS, 1):
        n_pag += 1
        paginas.append(f"""<section class="pag oscura cap"><div class="grande">{i:02d}</div><h2>{e(c['nombre'])}</h2><p>{e(c['intro'])}</p>
<div class="rango">PROMPTS {(i-1)*10+1} AL {i*10}</div></section>""")
        lote = []
        for t, txt in c["prompts"]:
            num += 1
            lote.append(f'<div class="card"><h3><span>{num}</span>{e(t)}</h3><pre>{e(txt)}</pre></div>')
        for j in range(0, 10, 4):  # 4 tarjetas por página
            n_pag += 1
            paginas.append(f'<section class="pag"><div class="cab"><span>Capítulo {i:02d}</span><span>{e(c["nombre"])}</span></div>{"".join(lote[j:j+4])}{pie(n_pag)}</section>')
    paginas.append(f"""<section class="pag oscura cierre"><img class="yo" src="{url('assets/img/leandro.webp')}" alt="">
<h2>¿Te sirvió? Hay más.</h2>
<p>Soy Leandro Lencina. Todas las semanas pruebo una herramienta de IA nueva y te muestro cómo usarla, paso a paso y sin tecnicismos.</p>
<p>En la biblioteca gratis tenés guías para tu CV, audios de WhatsApp, presentaciones, Google Maps y más.</p>
<div><a class="boton" href="https://www.neoatlantis.com.ar/recursos/">neoatlantis.com.ar/recursos</a></div>
<p style="font-size:8.5pt">Instagram: @leandrolencina.ia</p></section>""")
    return f'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>{e(TITULO)}</title><style>{CSS}</style></head><body>{"".join(paginas)}</body></html>'

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(os.path.dirname(PDF), exist_ok=True)
    hp = os.path.join(OUT_DIR, "ebook.html")
    open(hp, "w", encoding="utf-8").write(construir())
    subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--allow-file-access-from-files", "--no-pdf-header-footer",
                    f"--print-to-pdf={PDF}", "file:///" + hp.replace("\\", "/")], check=True, capture_output=True, timeout=180)
    print("PDF:", PDF, os.path.getsize(PDF) // 1024, "KB")
