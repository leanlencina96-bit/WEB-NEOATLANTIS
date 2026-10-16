# Genera las páginas por especialidad (/odontologos/, …) y las guías (/guias/…) de neoatlantis.com.ar
# con el mismo diseño, datos estructurados y enlaces. Correr desde la raíz del sitio:
#   python herramientas/generar_paginas.py
# El contenido de cada página está en herramientas/contenido_paginas.py.
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from contenido_paginas import ESPECIALIDADES, GUIAS

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = "https://www.neoatlantis.com.ar"
WA = "https://wa.me/5493412269841?text="
FUENTES = open(os.path.join(RAIZ, "assets", "fonts", "fuentes.css"), encoding="utf-8").read().strip()
e = html.escape

CSS = """
:root{--void:#05070A;--navy:#0D1424;--navy-2:#111B30;--off:#EDEEF1;--slate:#4B5563;--white:#fff;--electric:#4C6FFF;--electric-ink:#3554E0;--violet:#7B5CFA;--line-dark:rgba(255,255,255,.10);--line-light:rgba(11,20,36,.10)}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;line-height:1.65;background:var(--void);color:var(--white);overflow-x:hidden}
h1,h2,h3{font-family:'Space Grotesk',sans-serif;font-weight:600;letter-spacing:-.01em}
a{color:inherit}
img,svg{display:block;max-width:100%}
.wrap{max-width:1180px;margin:0 auto;padding:0 40px}
@media(max-width:700px){.wrap{padding:0 22px}}
header{position:sticky;top:0;z-index:50;background:rgba(5,7,10,.85);backdrop-filter:blur(10px);border-bottom:1px solid var(--line-dark)}
header nav{display:flex;align-items:center;justify-content:space-between;padding:16px 0}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-family:'Space Grotesk',sans-serif;font-weight:600}
.brand img{width:28px;height:28px}
.navlinks{display:flex;gap:34px}
.navlinks a{font-size:.88rem;color:rgba(255,255,255,.68);text-decoration:none}
.navlinks a:hover{color:#fff}
@media(max-width:880px){.navlinks{display:none}}
.navcta{border:1px solid rgba(255,255,255,.25);padding:9px 20px;font-size:.82rem;border-radius:100px;text-decoration:none}
.navcta:hover{background:#fff;color:var(--void)}
.migas{font-size:.82rem;color:rgba(255,255,255,.55);margin-bottom:26px}
.migas a{color:rgba(255,255,255,.7);text-decoration:none}
.migas a:hover{text-decoration:underline}
.hero{padding:90px 0 100px;background:radial-gradient(ellipse 55% 60% at 82% 30%,rgba(76,111,255,.16),transparent 65%),var(--void)}
.eyebrow{font-size:.9rem;color:rgba(255,255,255,.55);margin-bottom:18px}
.hero h1{font-size:clamp(2.4rem,5.4vw,4.4rem);line-height:1.02;max-width:900px}
.hero p.sub{margin-top:24px;font-size:1.12rem;color:rgba(255,255,255,.66);max-width:620px;font-weight:300}
.ctas{display:flex;gap:14px;flex-wrap:wrap;margin-top:34px;align-items:center}
.btn{display:inline-flex;align-items:center;gap:8px;padding:15px 28px;border-radius:100px;font-size:.92rem;font-weight:500;text-decoration:none;border:1px solid transparent}
.btn-claro{background:#fff;color:var(--void)}
.btn-claro:hover{background:var(--electric);color:#fff}
.btn-wa{background:#173A2A;color:#9BE8C3;border-color:#23573E}
.btn-wa:hover{border-color:#3FCF8E}
.sec{padding:100px 0}
@media(max-width:800px){.sec{padding:70px 0}.hero{padding:60px 0 70px}}
.claro{background:var(--off);color:#0D1424}
.claro h2,.claro h3{color:var(--void)}
.claro .muted{color:var(--slate)}
.oscuro{background:var(--navy)}
.sec h2{font-size:clamp(1.9rem,3.6vw,2.7rem);line-height:1.1;margin-bottom:16px;max-width:760px}
.sec .intro{font-size:1.04rem;max-width:640px;margin-bottom:46px}
.oscuro .intro{color:rgba(255,255,255,.66)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media(max-width:820px){.grid2{grid-template-columns:1fr}}
.tarjeta{background:#fff;border:1px solid var(--line-light);border-radius:14px;padding:26px}
.tarjeta h3{font-size:1.15rem;margin-bottom:8px}
.tarjeta p{color:var(--slate);font-size:.96rem}
.sol{display:grid;grid-template-columns:1fr auto;gap:18px;align-items:start;padding:24px 0;border-top:1px solid var(--line-dark)}
.sol:last-child{border-bottom:1px solid var(--line-dark)}
.sol h3{font-size:1.15rem;margin-bottom:6px}
.sol p{color:rgba(255,255,255,.66);font-size:.96rem;max-width:640px}
.chip{font-size:.75rem;padding:4px 11px;border-radius:999px;border:1px solid rgba(255,255,255,.2);color:rgba(255,255,255,.75);white-space:nowrap}
.chip.inc{border-color:rgba(124,224,176,.5);color:#9BE8C3}
.chip.plan{border-color:rgba(123,147,255,.55);color:#B3C1FF}
.pasos{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;counter-reset:p}
@media(max-width:820px){.pasos{grid-template-columns:1fr}}
.paso{background:#fff;border:1px solid var(--line-light);border-radius:14px;padding:26px;counter-increment:p}
.paso::before{content:counter(p,decimal-leading-zero);display:block;font-family:'Space Grotesk',sans-serif;color:var(--electric-ink);font-weight:600;margin-bottom:10px}
.paso h3{font-size:1.1rem;margin-bottom:6px}
.paso p{color:var(--slate);font-size:.95rem}
.demo{display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap;background:var(--navy-2);border:1px solid var(--line-dark);border-radius:16px;padding:30px}
.demo p{color:rgba(255,255,255,.7);max-width:620px}
.faq{max-width:860px;border-top:1px solid var(--line-light)}
.faq details{border-bottom:1px solid var(--line-light)}
.faq summary{list-style:none;cursor:pointer;padding:22px 40px 22px 0;font-family:'Space Grotesk',sans-serif;font-size:1.1rem;position:relative;color:var(--void)}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:'+';position:absolute;right:4px;top:50%;transform:translateY(-50%);font-size:1.5rem;color:var(--electric-ink)}
.faq details[open] summary::after{content:'–'}
.faq details p{padding:0 0 22px;color:var(--slate);max-width:720px}
.cierre{text-align:center;padding:110px 0;background:radial-gradient(ellipse 60% 70% at 50% 100%,rgba(76,111,255,.14),transparent 65%),var(--void)}
.cierre h2{font-size:clamp(2rem,4.6vw,3.2rem);max-width:820px;margin:0 auto}
.cierre p{margin-top:16px;color:rgba(255,255,255,.62)}
.cierre .ctas{justify-content:center}
.otras{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
.otras a{font-size:.88rem;padding:8px 16px;border-radius:999px;border:1px solid var(--line-light);text-decoration:none;color:#0D1424;background:#fff}
.otras a:hover{border-color:var(--electric-ink)}
/* artículo (guías) */
.articulo{background:var(--off);color:#1F2937;padding:70px 0 90px}
.articulo .cuerpo{max-width:784px;margin:0 auto;padding:0 22px}
.articulo h2{font-size:1.75rem;color:var(--void);margin:46px 0 14px;line-height:1.2}
.articulo h3{font-size:1.2rem;color:var(--void);margin:28px 0 8px}
.articulo p{margin-bottom:16px;font-size:1.06rem}
.articulo ul,.articulo ol{margin:0 0 18px 22px;font-size:1.06rem}
.articulo li{margin-bottom:8px}
.articulo .tabla{overflow-x:auto;margin:0 0 22px}
.articulo table{width:100%;border-collapse:collapse;font-size:.98rem;background:#fff;border-radius:12px;overflow:hidden}
.articulo th,.articulo td{padding:12px 14px;text-align:left;border-bottom:1px solid #E5E7EB;vertical-align:top}
.articulo th{background:var(--void);color:#fff;font-weight:600}
@media(max-width:600px){.articulo table{font-size:.86rem}.articulo th,.articulo td{padding:10px 8px;-webkit-hyphens:auto;hyphens:auto}.articulo td:first-child{width:28%}}
.articulo a{color:var(--electric-ink)}
.articulo a.btn-claro{color:var(--void)}
.articulo a.btn-wa{color:#9BE8C3}
.articulo .indice{background:#fff;border:1px solid var(--line-light);border-radius:14px;padding:20px 24px;margin:8px 0 30px}
.articulo .indice b{display:block;margin-bottom:8px;color:var(--void)}
.articulo .indice ol{margin-bottom:0}
.nota{background:#fff;border-left:4px solid var(--electric-ink);border-radius:8px;padding:16px 20px;margin:20px 0;font-size:1rem}
.caja-cta{background:var(--navy);color:#fff;border-radius:16px;padding:32px;margin-top:46px}
.caja-cta h2{color:#fff;margin:0 0 10px;font-size:1.5rem}
.caja-cta p{color:rgba(255,255,255,.72)}
.fuentes{font-size:.92rem;color:var(--slate)}
.meta-art{font-size:.88rem;color:rgba(255,255,255,.6);margin-top:18px}
.lista-guias{display:grid;gap:18px}
.lista-guias a{display:block;background:#fff;border:1px solid var(--line-light);border-radius:14px;padding:26px;text-decoration:none;color:#0D1424}
.lista-guias a:hover{border-color:var(--electric-ink)}
.lista-guias h2{font-size:1.3rem;margin:0 0 6px}
.lista-guias p{color:var(--slate);margin:0}
footer{border-top:1px solid var(--line-dark);padding:50px 0 34px}
.pie{display:flex;justify-content:space-between;flex-wrap:wrap;gap:30px;margin-bottom:34px}
.pie p{color:rgba(255,255,255,.55);font-size:.94rem;max-width:300px;margin-top:12px}
.pie-links{display:flex;gap:48px;flex-wrap:wrap}
.pie-links a{display:block;color:rgba(255,255,255,.6);font-size:.9rem;margin-bottom:10px;text-decoration:none}
.pie-links a:hover{color:#fff}
.pie-fin{border-top:1px solid var(--line-dark);padding-top:22px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;color:rgba(255,255,255,.6);font-size:.82rem}
.wa-float{position:fixed;right:22px;bottom:22px;z-index:60;width:58px;height:58px;border-radius:50%;background:#25D366;display:grid;place-items:center;box-shadow:0 8px 24px rgba(0,0,0,.35)}
.wa-float svg{width:30px;height:30px;fill:#fff}
:focus-visible{outline:2px solid var(--electric);outline-offset:3px}
"""

WA_SVG = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16.04 3C9.4 3 4 8.36 4 14.96c0 2.1.56 4.16 1.62 5.97L4 29l8.3-1.6a12.1 12.1 0 0 0 3.74.6C22.68 28 28 22.64 28 16.04 28 9.4 22.68 3 16.04 3zm0 22.9c-1.18 0-2.34-.2-3.44-.6l-.5-.18-4.92.95.98-4.8-.2-.5a9.9 9.9 0 0 1-1.5-5.8c0-5.46 4.48-9.9 9.6-9.9 5.46 0 9.9 4.44 9.9 9.94S21.5 25.9 16.04 25.9zm5.44-7.4c-.3-.15-1.76-.86-2.03-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.4-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.44-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.6-.92-2.2-.24-.58-.49-.5-.67-.5h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.48 0 1.46 1.07 2.88 1.21 3.08.15.2 2.1 3.2 5.08 4.48.71.31 1.27.5 1.7.63.72.23 1.37.2 1.88.12.57-.09 1.76-.72 2-1.41.25-.7.25-1.29.18-1.41-.08-.13-.27-.2-.57-.35z"/></svg>'

def cabeza(titulo, desc, ruta, schema, og_tipo="website"):
    url = SITIO + ruta
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(titulo)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="{og_tipo}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITIO}/assets/og-image.jpg">
<meta property="og:locale" content="es_AR">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(titulo)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITIO}/assets/og-image.jpg">
<meta name="theme-color" content="#05070A">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/space-grotesk-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>
{FUENTES}
{CSS}
</style>
""" + "".join(f'<script type="application/ld+json">\n{json.dumps(s, ensure_ascii=False, indent=1)}\n</script>\n' for s in schema) + """<script>window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };</script>
<script defer src="/_vercel/insights/script.js"></script>
</head>
<body>
<header><div class="wrap"><nav>
  <a class="brand" href="/"><img src="/assets/isotipo.png" alt="" width="128" height="128">NEOATLANTIS</a>
  <div class="navlinks"><a href="/como-funciona/">Cómo funciona</a><a href="/#incluye">Qué incluye</a><a href="/#casos">Demos</a><a href="/guias/">Guías</a><a href="/#preguntas">Preguntas</a><a href="/#captacion">Contacto</a></div>
  <a class="navcta" href="/diagnostico/">Diagnóstico gratis</a>
</nav></div></header>
"""

def especialidades_pie():
    return ''.join(f'<a href="/{x["slug"]}/">{e(x["nombre"])}</a>' for x in ESPECIALIDADES if x.get('listo'))

def pie(texto_wa):
    return f"""<footer><div class="wrap">
  <div class="pie">
    <div><a class="brand" href="/"><img src="/assets/isotipo.png" alt="" width="128" height="128">NEOATLANTIS</a><p>Web, turnos online y automatizaciones para profesionales de la salud.</p></div>
    <div class="pie-links">
      <div>{especialidades_pie()}</div>
      <div><a href="/como-funciona/">Cómo funciona</a><a href="/guias/">Guías</a><a href="/#casos">Demos</a><a href="/#captacion">Contacto</a><a href="https://www.instagram.com/neoatlantis.digital" target="_blank" rel="noopener">Instagram</a><a href="/privacidad.html">Privacidad</a><a href="/terminos.html">Términos</a></div>
    </div>
  </div>
  <div class="pie-fin"><span>© {2026} NeoAtlantis</span><span>Villa Gobernador Gálvez · Rosario, Argentina</span></div>
</div></footer>
<a class="wa-float" href="{WA}{texto_wa}" target="_blank" rel="noopener" aria-label="Escribinos por WhatsApp">{WA_SVG}</a>
</body>
</html>
"""

def migas(pasos):
    partes = ['<a href="/">Inicio</a>'] + [f'<a href="{r}">{e(n)}</a>' if r else e(n) for n, r in pasos]
    return '<nav class="migas" aria-label="Estás en">' + " › ".join(partes) + "</nav>"
def schema_migas(pasos):
    items = [{"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITIO + "/"}]
    for i, (n, r) in enumerate(pasos, 2): items.append({"@type": "ListItem", "position": i, "name": n, "item": SITIO + r})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}
def schema_faq(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}

ETIQ = {"inc": ("inc", "Incluido"), "plan": ("plan", "Plan mensual"), "extra": ("", "Para sumar")}

def pagina_especialidad(p):
    ruta = f"/{p['slug']}/"
    wa = (p["wa"]).replace(" ", "%20")
    schema = [
        {"@context": "https://schema.org", "@type": "Service", "name": p["servicio"], "serviceType": "Página web y turnos online para consultorios",
         "provider": {"@type": "ProfessionalService", "name": "NeoAtlantis", "url": SITIO + "/", "telephone": "+54 9 341 226-9841"},
         "areaServed": [{"@type": "City", "name": "Rosario"}, {"@type": "City", "name": "Villa Gobernador Gálvez"}], "audience": {"@type": "Audience", "audienceType": p["audiencia"]},
         "description": p["descripcion"]},
        schema_faq(p["faq"]), schema_migas([(p["nombre"], ruta)])]
    otras = [x for x in ESPECIALIDADES if x["slug"] != p["slug"] and x.get("listo")]
    h = cabeza(p["titulo"], p["descripcion"], ruta, schema)
    h += f"""<main>
<section class="hero"><div class="wrap">
  {migas([(p['nombre'], None)])}
  <div class="eyebrow">{e(p['eyebrow'])}</div>
  <h1>{p['h1']}</h1>
  <p class="sub">{e(p['sub'])}</p>
  <div class="ctas"><a class="btn btn-claro" href="/diagnostico/">Quiero mi diagnóstico gratis</a><a class="btn btn-wa" href="{WA}{wa}" target="_blank" rel="noopener">Escribinos por WhatsApp</a></div>
</div></section>

<section class="sec claro"><div class="wrap">
  <h2>{e(p['dolores_titulo'])}</h2>
  <p class="intro muted">{e(p['dolores_intro'])}</p>
  <div class="grid2">{''.join(f'<div class="tarjeta"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in p['dolores'])}</div>
</div></section>

<section class="sec oscuro"><div class="wrap">
  <h2>Cómo lo resolvemos</h2>
  <p class="intro">{e(p['solucion_intro'])}</p>
  {''.join(f'<div class="sol"><div><h3>{e(t)}</h3><p>{e(d)}</p></div><span class="chip {ETIQ[k][0]}">{ETIQ[k][1]}</span></div>' for t, d, k in p['soluciones'])}
</div></section>

<section class="sec" style="background:var(--void)"><div class="wrap">
  <div class="demo"><div><h2 style="font-size:1.6rem;margin-bottom:8px">{e(p['demo_titulo'])}</h2><p>{e(p['demo_texto'])}</p></div>
  <a class="btn btn-claro" href="{p['demo_url']}" target="_blank" rel="noopener">{e(p['demo_boton'])}</a></div>
</div></section>

<section class="sec claro"><div class="wrap">
  <h2>Cómo empezamos</h2>
  <p class="intro muted">Sin compromiso y sin tecnicismos. Lo hablás directamente conmigo.</p>
  <div class="pasos">
    <div class="paso"><h3>Diagnóstico gratis</h3><p>Una charla de 15 minutos para entender cómo das los turnos hoy y qué te conviene resolver primero.</p></div>
    <div class="paso"><h3>Propuesta por escrito</h3><p>Qué incluye, cuánto cuesta y en cuánto tiempo, sin letra chica.</p></div>
    <div class="paso"><h3>Funcionando en 7 a 15 días hábiles</h3><p>Desde que tenemos el anticipo y tu material. Te muestro cómo usarlo y te acompaño 30 días.</p></div>
  </div>
</div></section>

<section class="sec claro" style="padding-top:0"><div class="wrap">
  <h2>Preguntas de {e(p['nombre_corto'])}</h2>
  <div class="faq">{''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in p['faq'])}</div>
  <p class="muted" style="margin-top:34px">¿Otra especialidad?</p>
  <div class="otras">{''.join(f'<a href="/{x["slug"]}/">{e(x["nombre"])}</a>' for x in otras)}<a href="/guias/">Guías para consultorios</a></div>
</div></section>

<section class="cierre"><div class="wrap">
  <h2>{e(p['cierre'])}</h2>
  <p>Diagnóstico gratis de 15 minutos · Sin compromiso · Villa Gobernador Gálvez y Gran Rosario</p>
  <div class="ctas"><a class="btn btn-claro" href="/diagnostico/">Hacer el autodiagnóstico gratis</a><a class="btn btn-wa" href="{WA}{wa}" target="_blank" rel="noopener">Escribinos por WhatsApp</a></div>
</div></section>
</main>
"""
    h += pie(wa)
    return ruta, h

def pagina_guia(g):
    ruta = f"/guias/{g['slug']}/"
    schema = [{"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["descripcion"],
               "datePublished": g["fecha"], "dateModified": g.get("actualizada", g["fecha"]), "inLanguage": "es-AR",
               "author": {"@type": "Person", "name": "Leandro Lencina", "url": SITIO + "/#quien"},
               "publisher": {"@type": "Organization", "name": "NeoAtlantis", "logo": {"@type": "ImageObject", "url": SITIO + "/assets/apple-touch-icon.png"}},
               "mainEntityOfPage": SITIO + ruta, "image": SITIO + "/assets/og-image.jpg"},
              schema_migas([("Guías", "/guias/"), (g["corto"], ruta)])]
    h = cabeza(g["titulo"], g["descripcion"], ruta, schema, "article")
    fecha = g["fecha_txt"]
    h += f"""<main>
<section class="hero" style="padding-bottom:60px"><div class="wrap">
  {migas([('Guías', '/guias/'), (g['corto'], None)])}
  <div class="eyebrow">Guía para consultorios</div>
  <h1>{g['h1']}</h1>
  <p class="sub">{e(g['bajada'])}</p>
  <p class="meta-art">Por Leandro Lencina · NeoAtlantis · {e(fecha)} · {g['minutos']} min de lectura</p>
</div></section>
<article class="articulo"><div class="cuerpo">
{g['cuerpo']}
<div class="caja-cta"><h2>{e(g['cta_titulo'])}</h2><p>{e(g['cta_texto'])}</p>
<div class="ctas"><a class="btn btn-claro" href="/diagnostico/">Hacer el autodiagnóstico gratis</a><a class="btn btn-wa" href="{WA}{g['wa'].replace(' ', '%20')}" target="_blank" rel="noopener">Escribinos por WhatsApp</a></div></div>
{('<h2 style="font-size:1.2rem;margin-top:40px">Fuentes</h2>' + '<ul class="fuentes">' + ''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{e(t)}</a></li>' for t, u in g['fuentes']) + '</ul>') if g['fuentes'] else ''}
<p class="fuentes" style="margin-top:20px"><a href="/guias/">← Todas las guías</a></p>
</div></article>
</main>
"""
    h += pie(g["wa"].replace(" ", "%20"))
    return ruta, h


CSS_CF = """<style>
.cf-paso{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center;padding:56px 0;border-top:1px solid var(--line-dark)}
.cf-paso:first-child{border-top:0}
@media(max-width:820px){.cf-paso{grid-template-columns:1fr;gap:26px;padding:40px 0}}
.cf-num{font-family:'Space Grotesk',sans-serif;color:#B3C1FF;font-weight:600;margin-bottom:10px}
.cf-paso h2{font-size:clamp(1.5rem,3vw,2.1rem);line-height:1.15;margin-bottom:12px}
.cf-paso p{color:rgba(255,255,255,.7);max-width:520px}
.cf-paso .quien{display:inline-block;margin-top:14px;font-size:.8rem;padding:4px 11px;border-radius:999px;border:1px solid rgba(255,255,255,.2);color:rgba(255,255,255,.75)}
.cel{max-width:320px;width:100%;margin:0 auto;background:#0B0F19;border:1px solid rgba(255,255,255,.14);border-radius:30px;padding:16px 14px 20px;box-shadow:0 20px 50px rgba(0,0,0,.4)}
.cel .barra{display:flex;justify-content:space-between;font-size:.72rem;color:rgba(255,255,255,.5);padding:0 8px 12px}
.cel .app{font-size:.78rem;color:rgba(255,255,255,.55);padding:0 8px 10px;border-bottom:1px solid rgba(255,255,255,.08);margin-bottom:12px}
.burbuja{background:#182033;border-radius:14px;padding:12px 14px;font-size:.9rem;line-height:1.45;color:#E8EAF0}
.burbuja b{color:#fff}
.botones{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
.botones span{text-align:center;background:#22304D;border-radius:10px;padding:9px;font-size:.85rem;color:#DCE3FF}
.horarios{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:10px}
.horarios span{text-align:center;border:1px solid rgba(255,255,255,.16);border-radius:10px;padding:9px 4px;font-size:.85rem;color:#E8EAF0}
.horarios span.on{background:var(--electric);border-color:var(--electric);color:#fff}
.horarios span.no{opacity:.3;text-decoration:line-through}
.mail{background:#fff;color:#1F2937;border-radius:14px;padding:16px;font-size:.88rem;line-height:1.5}
.mail .de{font-size:.75rem;color:#6B7280;margin-bottom:6px}
.mail b{color:#05070A}
.mail .bt{display:inline-block;margin-top:10px;border:1px solid #D1D5DB;border-radius:8px;padding:6px 12px;font-size:.8rem;color:#374151}
.ilus{font-size:.75rem;color:rgba(255,255,255,.4);text-align:center;margin-top:10px}
.paquetes{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
@media(max-width:900px){.paquetes{grid-template-columns:1fr}}
.paquete{background:#fff;border:1px solid var(--line-light);border-radius:14px;padding:26px}
.paquete.dest{border:2px solid var(--electric-ink)}
.paquete h3{font-size:1.25rem;margin-bottom:6px}
.paquete .para{color:var(--slate);font-size:.95rem;margin-bottom:14px}
.paquete ul{list-style:none;display:grid;gap:8px;font-size:.95rem;color:#1F2937}
.paquete li{padding-left:22px;position:relative}
.paquete li::before{content:"✓";position:absolute;left:0;color:var(--electric-ink);font-weight:600}
</style>
"""

def cel(app, cuerpo):
    return f'<div><div class="cel" aria-hidden="true"><div class="barra"><span>10:02</span><span>●●●</span></div><div class="app">{app}</div>{cuerpo}</div><p class="ilus">Ilustración</p></div>'

def pagina_como_funciona():
    ruta = "/como-funciona/"
    titulo = "Cómo funcionan los turnos online para tu consultorio | NeoAtlantis"
    desc = "Paso a paso: el paciente reserva en tu web, vos aprobás desde el celular y los recordatorios salen solos. Qué ves vos, qué recibe el paciente y qué necesitás."
    faq = [
        ("¿Tengo que instalar algo?", "Solo Telegram en tu celular, que es gratis. Por ahí te llega cada turno nuevo para aprobarlo. Todo lo demás lo configuramos nosotros."),
        ("¿Y si no estoy atento al celular?", "El turno queda esperando tu aprobación y el paciente sabe que está pendiente. Lo aprobás cuando terminás de atender."),
        ("¿Qué datos del paciente se guardan?", "Solo los del turno: nombre, contacto, día y hora. Nunca información clínica ni el motivo de la consulta."),
        ("¿Puedo bloquear días o cambiar horarios?", "Sí. Vacaciones, feriados o un cambio de horario se ajustan y la agenda deja de ofrecer esos días."),
        ("¿Puedo seguir dando turnos por WhatsApp?", "Sí. WhatsApp puede seguir para conversar con tus pacientes. La diferencia es que los turnos quedan todos en la misma agenda y no se superponen."),
    ]
    schema = [{"@context": "https://schema.org", "@type": "WebPage", "name": "Cómo funcionan los turnos online", "description": desc, "url": SITIO + ruta, "inLanguage": "es-AR"},
              schema_faq(faq), schema_migas([("Cómo funciona", ruta)])]
    h = cabeza(titulo, desc, ruta, schema).replace("</head>", CSS_CF + "</head>", 1)
    p1 = cel("tuconsultorio.com.ar · Reservar turno", '<div class="burbuja"><b>Jueves 17</b> · Elegí un horario</div><div class="horarios"><span class="no">9:00</span><span>9:45</span><span class="on">10:30</span><span>11:15</span><span class="no">12:00</span><span>16:00</span></div>')
    p2 = cel("Telegram · NeoAtlantis Turnos", '<div class="burbuja">📅 <b>Nuevo turno</b><br>Laura G.<br>Jueves 17 · 10:30<br>Primera consulta</div><div class="botones"><span>✅ Confirmar</span><span>❌ Rechazar</span></div>')
    p3 = cel("Email del paciente", '<div class="mail"><div class="de">Consultorio Lic. Pérez</div><b>Tu turno está confirmado</b><br>Jueves 17 a las 10:30<br>Córdoba 1234, Rosario</div>')
    p4 = cel("Email del paciente · 24 h antes", '<div class="mail"><div class="de">Consultorio Lic. Pérez</div><b>Te esperamos mañana a las 10:30</b><br>Si no podés venir, avisanos para que otro paciente use el horario.<br><span class="bt">Cancelar turno</span></div>')
    p5 = cel("Agenda", '<div class="burbuja">↩️ <b>Laura G. canceló</b><br>Jueves 17 · 10:30 vuelve a estar libre</div><div class="horarios"><span class="no">9:00</span><span>9:45</span><span class="on">10:30</span></div>')
    pasos = [
        ("01", "El paciente reserva en tu web", "Entra a tu web, ve solo los horarios libres y elige el que le queda bien, a cualquier hora y sin escribirte. No hay doble reserva: un horario tomado deja de aparecer.", "Lo hace el paciente", p1),
        ("02", "Te llega al celular y aprobás con un toque", "Cada turno nuevo te llega por Telegram con dos botones: Confirmar o Rechazar. Lo aprobás entre paciente y paciente, sin ida y vuelta de mensajes.", "Lo hacés vos: un toque", p2),
        ("03", "El paciente recibe la confirmación", "Cuando confirmás (o rechazás), al paciente le llega el aviso por email, con el día, la hora y la dirección. Vos no escribís nada.", "Automático", p3),
        ("04", "Los recordatorios salen solos", "24 horas antes y 2 horas antes, el paciente recibe un recordatorio. El de 24 horas trae un botón para cancelar con un clic, así te enterás a tiempo.", "Automático", p4),
        ("05", "Si cancela, el horario se libera", "El horario vuelve a aparecer libre en tu web para otro paciente. En el paquete Integral, además, se avisa a la lista de espera para llenarlo.", "Automático", p5),
    ]
    bloques = "".join(f'<div class="cf-paso"><div><div class="cf-num">{n}</div><h2>{e(t)}</h2><p>{e(d)}</p><span class="quien">{e(q)}</span></div>{m}</div>' for n, t, d, q, m in pasos)
    paquetes = [
        ("Presencia", "Para que te encuentren.", ["Web profesional pensada para el celular", "Ficha de Google Maps completa", "Botón de WhatsApp"], False),
        ("Turnos", "Lo de esta página. El más elegido.", ["Todo Presencia", "Turnos online sin doble reserva", "Aprobación desde Telegram", "Confirmación y recordatorios por email", "Botón para cancelar"], True),
        ("Integral", "Para agendas llenas.", ["Todo Turnos", "Confirmación en tres tiempos (72, 24 y 2 h)", "Lista de espera", "Pedido de reseña y aviso de control", "Asistente de consultas y reporte semanal"], False),
    ]
    paq = "".join(f'<div class="paquete{" dest" if d else ""}"><h3>{e(n)}</h3><p class="para">{e(pa)}</p><ul>{"".join(f"<li>{e(x)}</li>" for x in it)}</ul></div>' for n, pa, it, d in paquetes)
    h += f"""<main>
<section class="hero"><div class="wrap">
  {migas([('Cómo funciona', None)])}
  <div class="eyebrow">Turnos online para consultorios · Paso a paso</div>
  <h1>Tus turnos, organizados solos. Así funciona.</h1>
  <p class="sub">Lo que ve el paciente, lo que te llega a vos y lo que pasa solo. Tu único trabajo: aprobar cada turno con un toque.</p>
  <div class="ctas"><a class="btn btn-claro" href="/diagnostico/">Hacer el autodiagnóstico gratis</a><a class="btn btn-wa" href="{WA}Hola%20NeoAtlantis,%20vi%20c%C3%B3mo%20funcionan%20los%20turnos%20y%20quiero%20consultar." target="_blank" rel="noopener">Escribinos por WhatsApp</a></div>
</div></section>

<section class="sec oscuro"><div class="wrap">{bloques}</div></section>

<section class="sec claro"><div class="wrap">
  <h2>Qué necesitás vos</h2>
  <p class="intro muted">Casi nada. Nosotros configuramos todo y te mostramos cómo usarlo.</p>
  <div class="grid2">
    <div class="tarjeta"><h3>Telegram en tu celular</h3><p>Es gratis. Por ahí te llega cada turno para aprobarlo.</p></div>
    <div class="tarjeta"><h3>Tus horarios y tratamientos</h3><p>Días y horas de atención, y cuánto dura cada tipo de consulta. Con eso armamos la agenda.</p></div>
    <div class="tarjeta"><h3>Unos minutos para aprender</h3><p>Te mostramos cómo funciona en una llamada corta y te acompañamos 30 días.</p></div>
    <div class="tarjeta"><h3>Nada de datos clínicos</h3><p>El sistema solo guarda nombre, contacto, día y hora del turno. Lo clínico queda en tu consultorio.</p></div>
  </div>
</div></section>

<section class="sec claro" style="padding-top:0"><div class="wrap">
  <h2>Qué incluye cada paquete</h2>
  <p class="intro muted">El precio depende de lo que necesites. Lo vemos con tus números en el diagnóstico gratis.</p>
  <div class="paquetes">{paq}</div>
</div></section>

<section class="sec" style="background:var(--void)"><div class="wrap">
  <div class="demo"><div><h2 style="font-size:1.6rem;margin-bottom:8px">Probalo como paciente</h2><p>Entrá a un consultorio de ejemplo y reservá un turno. Es ficticio, pero la tecnología es la misma.</p></div>
  <a class="btn btn-claro" href="https://consultorio-dental-flax.vercel.app/" target="_blank" rel="noopener">Ver la demo</a></div>
</div></section>

<section class="sec claro"><div class="wrap">
  <h2>Preguntas frecuentes</h2>
  <div class="faq">{''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in faq)}</div>
</div></section>

<section class="cierre"><div class="wrap">
  <h2>¿Cuánto te ahorraría a vos?</h2>
  <p>Autodiagnóstico gratis · 3 minutos · Con tus números</p>
  <div class="ctas"><a class="btn btn-claro" href="/diagnostico/">Hacer el autodiagnóstico gratis</a></div>
</div></section>
</main>
"""
    h += pie("Hola%20NeoAtlantis,%20vi%20c%C3%B3mo%20funcionan%20los%20turnos%20y%20quiero%20consultar.")
    return ruta, h


def indice_guias():
    ruta = "/guias/"
    desc = "Guías prácticas para consultorios de salud: turnos, ausentismo, Google Maps y organización. Por NeoAtlantis, Villa Gobernador Gálvez y Rosario."
    schema = [schema_migas([("Guías", ruta)]), {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Guías para consultorios", "description": desc, "url": SITIO + ruta}]
    h = cabeza("Guías para consultorios de salud | NeoAtlantis", desc, ruta, schema)
    h += f"""<main>
<section class="hero" style="padding-bottom:60px"><div class="wrap">
  {migas([('Guías', None)])}
  <div class="eyebrow">Para profesionales de la salud</div>
  <h1>Guías para consultorios</h1>
  <p class="sub">Ideas concretas para organizar los turnos, que falten menos pacientes y que te encuentren en Google. Gratis y sin vueltas.</p>
</div></section>
<section class="articulo"><div class="cuerpo"><div class="lista-guias">
{''.join(f'<a href="/guias/{g["slug"]}/"><h2>{e(g["corto_largo"])}</h2><p>{e(g["descripcion"])}</p></a>' for g in GUIAS)}
</div></div></section>
</main>
"""
    h += pie("Hola%20NeoAtlantis%2C%20le%C3%AD%20sus%20gu%C3%ADas%20y%20quiero%20consultar%20por%20mi%20consultorio.")
    return ruta, h

def escribir(ruta, h):
    carpeta = os.path.join(RAIZ, ruta.strip("/").replace("/", os.sep))
    os.makedirs(carpeta, exist_ok=True)
    open(os.path.join(carpeta, "index.html"), "w", encoding="utf-8", newline="\n").write(h)
    print("ok", ruta)

if __name__ == "__main__":
    solo = sys.argv[1:]  # slugs a generar (vacío = todas las que tengan contenido)
    for p in ESPECIALIDADES:
        if p.get("listo") and (not solo or p["slug"] in solo): escribir(*pagina_especialidad(p))
    for g in GUIAS:
        if not solo or g["slug"] in solo: escribir(*pagina_guia(g))
    escribir(*indice_guias())
    escribir(*pagina_como_funciona())
