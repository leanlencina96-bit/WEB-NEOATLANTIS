# Recursos gratis de la marca personal (Leandro Lencina · Consultor IA). Uno por video: lo que la gente pide con «Comentá PALABRA».
# Regla: se regala lo que usa la gente (prompts, plantillas, checklists, guías). Nunca lo interno (scripts de la Fábrica, n8n,
# Hermes, claves). Cada recurso tiene que funcionar solo, sin que Leandro esté.
# Para sumar uno: agregar un dict a RECURSOS y correr generar_paginas.py. "listo": False lo oculta hasta que el video salga.

RECURSOS = [
    {
        "slug": "cv",
        "palabra": "CV",
        "listo": True,
        "titulo": "Prompts para armar tu CV con IA (gratis)",
        "corto": "CV con IA",
        "descripcion": "El prompt para armar un CV profesional con IA en 10 minutos, 3 prompts para mejorarlo y la lista de control antes de mandarlo.",
        "bajada": "Lo que uso en el video «Hice mi CV profesional en 10 minutos con IA». Copialo, pegalo en Claude o ChatGPT y completá con tus datos.",
        "herramientas": [("Claude", "https://claude.ai"), ("ChatGPT", "https://chatgpt.com"), ("Canva", "https://www.canva.com")],
        "bloques": [
            {"tipo": "prompt", "titulo": "1. El prompt principal",
             "texto": "Sos un experto en recursos humanos de Argentina. Con estos datos armá un CV de una página, claro y profesional.\n\nReglas:\n- Un perfil de 3 líneas al principio.\n- Experiencia con logros concretos (verbos de acción), del trabajo más nuevo al más viejo.\n- Habilidades en una lista corta.\n- Sin inventar nada que no esté en mis datos. Si falta algo importante, preguntame.\n\nMis datos:\n[pegá acá tus datos, aunque estén desordenados]"},
            {"tipo": "prompt", "titulo": "2. Adaptarlo a un aviso",
             "texto": "Este es mi CV y este es el aviso de trabajo al que me quiero postular. Adaptá el perfil y el orden de la experiencia para que se note que encajo, sin inventar nada. Marcame qué habilidades del aviso no aparecen en mi CV.\n\nMi CV:\n[pegá tu CV]\n\nEl aviso:\n[pegá el aviso]"},
            {"tipo": "prompt", "titulo": "3. Convertir tareas en logros",
             "texto": "Reescribí estas tareas como logros concretos para un CV. Usá verbos de acción y, si se puede, un resultado medible. Si no tengo un número, no lo inventes: dejá el logro sin número.\n\nTareas:\n[ej.: atendía el mostrador, hacía los pedidos a proveedores]"},
            {"tipo": "prompt", "titulo": "4. Revisión final",
             "texto": "Revisá mi CV como si fueras quien selecciona personal. Decime en 5 puntos: qué se entiende rápido, qué sobra, qué falta, si hay errores de ortografía y si cabe en una página.\n\nMi CV:\n[pegá tu CV]"},
            {"tipo": "lista", "titulo": "Antes de mandarlo",
             "items": ["Entra en una página.", "Tu email y tu teléfono están bien escritos.", "No hay nada que la IA haya exagerado o inventado: leelo entero.",
                       "Los trabajos van del más nuevo al más viejo.", "Lo guardaste en PDF con tu nombre: «CV-Nombre-Apellido.pdf».",
                       "La foto (si ponés) es reciente, con fondo liso y de frente."]},
            {"tipo": "texto", "titulo": "Cómo pasarlo a Canva",
             "texto": "En Canva buscá «currículum», elegí una plantilla simple de una columna y reemplazá los textos sección por sección. Descargalo en PDF."},
        ],
    },
    {
        "slug": "podcast", "palabra": "PODCAST", "listo": False,
        "titulo": "Guía de NotebookLM: de PDF a podcast", "corto": "PDF a podcast",
        "descripcion": "Cómo convertir cualquier PDF en un resumen en audio con NotebookLM y 5 preguntas para hacerle a un documento.",
        "bajada": "Lo que uso en el video «Esta IA de Google convierte cualquier PDF en un podcast».",
        "herramientas": [("NotebookLM", "https://notebooklm.google.com")], "bloques": [],
    },
    {
        "slug": "audio", "palabra": "AUDIO", "listo": False,
        "titulo": "Prompt para resumir audios largos", "corto": "Audios largos",
        "descripcion": "El prompt para resumir audios de WhatsApp en 3 puntos y cómo activar la transcripción.",
        "bajada": "Lo que uso en el video «Nunca más escuches un audio largo de WhatsApp».",
        "herramientas": [("Claude", "https://claude.ai"), ("TurboScribe", "https://turboscribe.ai")], "bloques": [],
    },
    {
        "slug": "ia", "palabra": "IA", "listo": False,
        "titulo": "Las 3 pruebas para comparar IA", "corto": "Comparar IA",
        "descripcion": "Las 3 pruebas y la planilla de puntaje para comparar ChatGPT, Claude y Gemini con tus propias tareas.",
        "bajada": "Lo que uso en el video «Probé ChatGPT, Claude y Gemini para lo mismo».",
        "herramientas": [("ChatGPT", "https://chatgpt.com"), ("Claude", "https://claude.ai"), ("Gemini", "https://gemini.google.com")], "bloques": [],
    },
]
