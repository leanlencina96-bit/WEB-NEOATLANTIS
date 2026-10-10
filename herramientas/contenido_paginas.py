# Contenido de las páginas por especialidad y de las guías. Lo usa generar_paginas.py.
# Regla: todo lo que se promete tiene que coincidir con la propuesta y el acuerdo
# (inc = paquete Consultorio Digital · plan = plan mensual · extra = extras con precio aparte).

ESPECIALIDADES = [
    {
        "slug": "odontologos", "listo": True,
        "nombre": "Odontólogos", "nombre_corto": "odontólogos", "audiencia": "Odontólogos y consultorios odontológicos",
        "servicio": "Web y turnos online para odontólogos",
        "titulo": "Turnos online para odontólogos en Rosario | NeoAtlantis",
        "descripcion": "Web y turnos online para consultorios odontológicos en Rosario y Villa Gobernador Gálvez: reservas las 24 h, menos faltazos y agenda por tratamiento y sillón.",
        "eyebrow": "Para odontólogos · Rosario y Villa Gobernador Gálvez",
        "h1": "Turnos online para tu consultorio odontológico",
        "sub": "Tus pacientes reservan solos, a cualquier hora, en el horario justo para cada tratamiento. Vos confirmás con un toque y el sistema se ocupa de los recordatorios.",
        "wa": "Hola NeoAtlantis, soy odontólogo/a y quiero consultar por los turnos online.",
        "dolores_titulo": "Lo que pasa todos los días en un consultorio odontológico",
        "dolores_intro": "Si te suena alguno de estos, no es falta de organización: es que la agenda depende de que alguien esté atento todo el tiempo.",
        "dolores": [
            ("Pacientes que faltan sin avisar", "El sillón queda vacío y ese horario ya no se recupera, aunque otro paciente lo estaba esperando."),
            ("Cada tratamiento dura distinto", "Una limpieza no ocupa lo mismo que un implante. Dar turnos fijos de 30 minutos desordena el día."),
            ("El WhatsApp de la noche", "Los pacientes escriben fuera de horario para pedir turno, y a la mañana siguiente hay que responder uno por uno."),
            ("Pacientes que no vuelven al control", "Vinieron una vez y nadie les recordó el control de los 6 meses. Se pierden pacientes que ya te conocían."),
            ("Las urgencias se mezclan con todo", "Un dolor fuerte no puede esperar a que alguien lea un mensaje entre otros veinte."),
            ("No aparecés en Google cuando te buscan", "Cuando alguien busca «dentista» en tu zona, encuentra a otro."),
        ],
        "solucion_intro": "Una web propia con reserva online y automatizaciones que trabajan solas. Te marco qué incluye el paquete, qué suma el plan mensual y qué se agrega aparte, para que no haya sorpresas.",
        "soluciones": [
            ("Tu web con turnos online las 24 horas", "El paciente elige tratamiento, día y horario, y solo ve los horarios libres. Sin llamados, sin doble reserva.", "inc"),
            ("Cada turno nuevo te llega a Telegram", "Lo aprobás o lo rechazás con un toque desde el celular, y el paciente recibe la confirmación por email.", "inc"),
            ("Recordatorios 24 h y 2 h antes", "Con un botón para cancelar: si el paciente no puede venir, el horario se libera solo.", "inc"),
            ("Tu ficha de Google para aparecer en Maps", "Configurada y conectada con tu web, para que te encuentren cuando buscan dentista en tu zona.", "inc"),
            ("Confirmación en tres tiempos (72, 24 y 2 h)", "El paciente confirma, cambia el horario o cancela con un toque, y vos te enterás por Telegram.", "plan"),
            ("Un asistente que responde las preguntas de siempre", "Horarios, obras sociales, cómo llegar. Ante una urgencia indica llamar al consultorio. Nunca da indicaciones de salud.", "plan"),
            ("Reporte de los lunes", "Por Telegram: quién viene esta semana, quién confirmó y qué falta aprobar.", "plan"),
            ("Agenda por duración de tratamiento y por sillón", "Cada tratamiento ocupa su tiempo real, y se reservan varios sillones a la vez.", "extra"),
            ("Lista de espera", "Si un día está completo, el paciente se anota. Si alguien cancela, le llega un email para reservar ese horario.", "extra"),
            ("Aviso de control a los 6 meses", "Un email a los pacientes que no volvieron, solo si aceptaron recibir avisos.", "extra"),
            ("Pedido de reseña en Google", "Después de la consulta, el mismo email a todos con el botón para dejar su opinión.", "extra"),
        ],
        "demo_titulo": "Probalo vos mismo: Dental Vértice",
        "demo_texto": "Un consultorio de ejemplo con todo funcionando: reserva por tratamiento, asistente de consultas y lista de espera. El negocio es ficticio; la tecnología es real.",
        "demo_url": "https://consultorio-dental-flax.vercel.app/", "demo_boton": "Abrir la demo",
        "faq": [
            ("¿Funciona si trabajo con obras sociales y prepagas?", "Sí. El sistema organiza los turnos; no factura ni gestiona autorizaciones. El asistente puede informar con qué obras sociales trabajás, y si lo necesitás, se puede pedir la obra social al reservar."),
            ("¿Sirve si tenemos varios sillones o varios profesionales?", "Sí. La agenda por sillón permite reservar varios turnos a la misma hora. Si son varios profesionales con agendas distintas, lo vemos en el diagnóstico y lo adaptamos."),
            ("¿Qué pasa con las urgencias?", "No se reservan como un turno común: la web y el asistente le indican al paciente que llame al consultorio, para que lo atiendas como corresponde."),
            ("¿Mis pacientes tienen que bajar una app o registrarse?", "No. Reservan desde la web del consultorio con su nombre, teléfono y email, desde el celular o la computadora."),
            ("¿Qué datos de los pacientes se guardan?", "Solo los del turno: nombre, contacto, tratamiento, día y hora. Nunca información clínica. Los datos son tuyos."),
            ("¿Cuánto cuesta?", "Depende de lo que necesite tu consultorio: lo vemos en el diagnóstico gratis y te pasamos una propuesta por escrito. El plan mensual de acompañamiento arranca en USD 100."),
        ],
        "cierre": "Tus pacientes ya te buscan. Que puedan reservar solos.",
    },
    {"slug": "psicologos", "nombre": "Psicólogos", "listo": False},
    {"slug": "medicos", "nombre": "Médicos", "listo": False},
    {"slug": "kinesiologos-nutricionistas", "nombre": "Kinesiólogos y nutricionistas", "listo": False},
]

GUIAS = [
    {
        "slug": "reducir-ausentismo-pacientes",
        "corto": "Cómo reducir el ausentismo",
        "corto_largo": "Cómo reducir el ausentismo de pacientes en tu consultorio",
        "titulo": "Cómo reducir el ausentismo de pacientes en tu consultorio | NeoAtlantis",
        "descripcion": "Por qué faltan los pacientes y 7 medidas concretas para que falten menos: recordatorios, cancelación fácil, lista de espera y cómo medirlo.",
        "h1": "Cómo reducir el ausentismo de pacientes en tu consultorio",
        "bajada": "Por qué faltan los pacientes, 7 medidas concretas que funcionan y cómo medir si estás mejorando. Sirve para odontología, psicología, medicina, kinesiología y nutrición.",
        "fecha": "2026-10-11", "fecha_txt": "11 de octubre de 2026", "minutos": 7,
        "wa": "Hola NeoAtlantis, leí la guía de ausentismo y quiero consultar por mi consultorio.",
        "cta_titulo": "¿Querés que esto funcione solo en tu consultorio?",
        "cta_texto": "Recordatorios automáticos, cancelación con un toque y lista de espera, conectados a tu agenda. En un diagnóstico gratis de 15 minutos vemos qué te conviene.",
        "fuentes": [
            ("Gurol-Urganci I. y otros (2013). Mobile phone messaging reminders for attendance at healthcare appointments. Cochrane Database of Systematic Reviews.", "https://www.cochrane.org/evidence/CD007458_mobile-phone-messaging-reminders-attendance-healthcare-appointments"),
        ],
        "cuerpo": """
<div class="indice"><b>En esta guía</b><ol>
<li><a href="#por-que">Por qué faltan los pacientes</a></li>
<li><a href="#medidas">7 medidas que funcionan</a></li>
<li><a href="#medir">Cómo medir tu ausentismo</a></li>
<li><a href="#automatizar">Qué automatizar (y qué no)</a></li>
</ol></div>

<p>Un turno al que el paciente no viene es un horario que ya no se recupera: el consultorio está preparado, el tiempo está reservado y, muchas veces, había otra persona que lo necesitaba. La buena noticia es que la mayoría de las ausencias no son mala voluntad, y por eso se pueden prevenir.</p>

<h2 id="por-que">1. Por qué faltan los pacientes</h2>
<p>Si mirás tus últimas ausencias con atención, casi siempre aparecen las mismas causas:</p>
<ul>
<li><strong>Se olvidaron.</strong> Sobre todo si el turno se dio hace semanas.</li>
<li><strong>Cancelar era incómodo.</strong> Había que llamar en horario de atención o escribir y esperar respuesta, y el paciente lo fue dejando.</li>
<li><strong>Surgió un imprevisto</strong> y no tenía una forma rápida de avisar.</li>
<li><strong>No tenía claro el día o la hora</strong>, porque el turno quedó en un mensaje perdido entre otros.</li>
</ul>
<p>Fijate que casi todas tienen la misma solución: <strong>recordar a tiempo y que avisar sea fácil</strong>.</p>

<h2 id="medidas">2. Siete medidas que funcionan</h2>

<h3>1. Mandá recordatorios, y en dos momentos</h3>
<p>Es la medida con más respaldo. Una revisión de la Cochrane, que analizó ensayos clínicos sobre el tema, concluyó que <strong>los recordatorios por mensaje aumentan la asistencia a los turnos frente a no mandar recordatorio</strong>, que tienen un efecto similar al de una llamada telefónica y que cuestan menos que llamar. Lo práctico es combinar dos avisos:</p>
<ul>
<li><strong>Uno con tiempo</strong> (24 a 72 horas antes), para que quien no puede venir avise y el horario se pueda volver a ofrecer.</li>
<li><strong>Uno cercano</strong> (2 horas antes), para el olvido de último momento.</li>
</ul>

<h3>2. Que cancelar sea un toque</h3>
<p>Parece al revés, pero facilitar la cancelación <strong>reduce las ausencias</strong>: el paciente que no puede venir avisa en vez de desaparecer. Un botón de «cancelar» en el recordatorio, que libere el horario solo, convierte una ausencia en un turno que se puede reocupar.</p>

<h3>3. Tené una lista de espera</h3>
<p>Si un día está completo, anotá a quien quería ese día. Cuando alguien cancela, avisale a la lista: el primero que reserva se queda con el lugar. Así, cada cancelación con aviso se transforma en un paciente atendido.</p>

<h3>4. Dejá clara tu política de cancelación</h3>
<p>Decila al momento de reservar, en una línea: «Si no podés venir, avisanos con 24 horas para que otro paciente pueda usar el turno». Si cobrás seña, explicalo también ahí. Lo importante es que sea simple y que el paciente la conozca antes, no después.</p>

<h3>5. Cuidado con los turnos muy lejanos</h3>
<p>Cuanto más lejos está el turno, más fácil es olvidarlo o que cambien los planes. Si das turnos a varias semanas, el recordatorio con tiempo se vuelve imprescindible.</p>

<h3>6. Que el turno quede escrito en un solo lugar</h3>
<p>Una confirmación por email o mensaje con día, hora, dirección y cómo cancelar evita el «pensé que era el jueves». Si el turno se dio por teléfono, mandá igual la confirmación escrita.</p>

<h3>7. Hablá con los que faltan seguido</h3>
<p>Llevá registro de quién no vino. Si alguien falta seguido, una conversación amable (¿le queda mejor otro horario?, ¿prefiere que le recuerden por otro medio?) suele resolverlo mejor que una sanción.</p>

<h2 id="medir">3. Cómo medir tu ausentismo</h2>
<p>Lo que no se mide no mejora. La cuenta es simple:</p>
<div class="nota"><strong>Ausentismo del mes</strong> = turnos a los que el paciente no vino (sin avisar) ÷ turnos dados en el mes.<br>
<em>Ejemplo inventado para la cuenta:</em> si en un mes diste 200 turnos y 16 pacientes faltaron sin avisar, tu ausentismo fue 16 ÷ 200 = 8 %.</div>
<p>Anotalo un mes antes de aplicar estas medidas y repetí la cuenta los meses siguientes. Separá también las <strong>cancelaciones con aviso</strong>: esas no son un problema, son horarios que podés volver a ocupar.</p>

<h2 id="automatizar">4. Qué automatizar (y qué no)</h2>
<p>Los recordatorios, las cancelaciones y la lista de espera se pueden automatizar por completo: es trabajo repetitivo que nadie debería hacer a mano todos los días. Lo que conviene que siga siendo humano es la conversación con el paciente que falta seguido y cualquier tema de salud.</p>
<p>Y un cuidado importante: <strong>en los mensajes automáticos nunca va información clínica</strong>. Día, hora, profesional y cómo cancelar alcanzan; el motivo de la consulta queda dentro del consultorio.</p>
""",
    },
]
