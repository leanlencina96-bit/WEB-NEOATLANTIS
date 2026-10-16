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
            ("¿Cuánto cuesta?", "Depende de lo que necesite tu consultorio: lo vemos en el diagnóstico gratis y te pasamos una propuesta por escrito. La web con turnos online arranca en USD 320 (en pesos al dólar oficial, en dos pagos) y el acompañamiento mensual en USD 32."),
        ],
        "cierre": "Tus pacientes ya te buscan. Que puedan reservar solos.",
    },
    {
        "slug": "psicologos", "listo": True,
        "nombre": "Psicólogos", "nombre_corto": "psicólogos", "audiencia": "Psicólogos y consultorios de psicología",
        "servicio": "Web y turnos online para psicólogos",
        "titulo": "Turnos online para psicólogos en Rosario | NeoAtlantis",
        "descripcion": "Web y turnos online para psicólogos en Rosario y Villa Gobernador Gálvez: primera entrevista online, recordatorios automáticos y confidencialidad. Diagnóstico gratis.",
        "eyebrow": "Para psicólogos · Rosario y Villa Gobernador Gálvez",
        "h1": "Turnos online para tu consultorio de psicología",
        "sub": "Que un paciente nuevo pueda pedir su primera entrevista sin tener que animarse a llamar. Vos confirmás con un toque; el sistema recuerda las sesiones.",
        "wa": "Hola NeoAtlantis, soy psicólogo/a y quiero consultar por los turnos online.",
        "dolores_titulo": "Lo que pasa todos los días en un consultorio de psicología",
        "dolores_intro": "Atender bien también es cuidar la agenda. Estos son los problemas que más se repiten.",
        "dolores": [
            ("Pacientes que no se animan a llamar", "Dar el primer paso cuesta. Si para pedir turno hay que llamar o explicar algo por WhatsApp, muchos lo postergan."),
            ("Mensajes entre sesiones", "Responder pedidos de turno o cambios de horario en los huecos entre pacientes te saca de lo importante."),
            ("Sesiones que se pierden", "Una cancelación a último momento es una hora libre que nadie más puede aprovechar."),
            ("Presencial y online mezclados", "Llevar a mano quién viene al consultorio y quién se conecta es fácil de confundir."),
            ("Datos sensibles en cualquier lado", "Turnos anotados en chats y papeles sueltos, sin saber bien quién los puede ver."),
            ("No te encuentran en Google", "Quien busca «psicólogo» en tu zona ve primero a otros, aunque vos tengas lugar."),
        ],
        "solucion_intro": "Una web propia con reserva online y avisos que trabajan solos, pensada para la confidencialidad. Te marco qué incluye el paquete, qué suma el plan mensual y qué se agrega aparte.",
        "soluciones": [
            ("Pedido de primera entrevista online", "El paciente elige día y horario libre desde la web, a cualquier hora, sin llamar ni dar explicaciones.", "inc"),
            ("Cada pedido te llega a Telegram", "Lo aprobás o lo rechazás con un toque, y el paciente recibe la confirmación por email.", "inc"),
            ("Recordatorios 24 h y 2 h antes", "Con un botón para cancelar: si el paciente no puede, el horario se libera solo.", "inc"),
            ("Tu ficha de Google para aparecer en Maps", "Configurada y conectada con tu web, para que te encuentren cuando buscan psicólogo en tu zona.", "inc"),
            ("Confirmación en tres tiempos (72, 24 y 2 h)", "El paciente confirma, cambia el horario o cancela con un toque, y vos te enterás por Telegram.", "plan"),
            ("Un asistente que responde las preguntas de siempre", "Honorarios, modalidad, obras sociales, cómo llegar. Nunca da indicaciones de salud; ante una crisis indica comunicarse con un servicio de emergencias.", "plan"),
            ("Reporte de los lunes", "Por Telegram: quién viene esta semana y quién confirmó.", "plan"),
            ("Duración distinta para la primera entrevista", "Por ejemplo, 60 minutos para la primera y 45 para las siguientes.", "extra"),
            ("Lista de espera", "Si no tenés lugar, el paciente se anota. Si alguien cancela, le llega un email para tomar ese horario.", "extra"),
        ],
        "demo_titulo": "Mirá un ejemplo: Espacio Claro",
        "demo_texto": "Un consultorio de psicología ficticio con la reserva de turnos de ejemplo. El negocio es inventado; el diseño y la reserva son los que armamos.",
        "demo_url": "/demo-psicologia.html", "demo_boton": "Abrir el ejemplo",
        "faq": [
            ("¿Qué datos de los pacientes se guardan?", "Solo los del turno: nombre, contacto, día y hora. El sistema nunca pide el motivo de consulta ni información clínica, y los datos son tuyos."),
            ("¿Sirve si atiendo online y presencial?", "Sí. En el formulario de reserva se puede sumar la opción online o presencial, y queda indicada en el aviso que te llega."),
            ("¿Los pacientes tienen que registrarse o bajar una app?", "No. Reservan desde tu web con nombre, teléfono y email."),
            ("¿Y los pacientes que vienen todas las semanas?", "Pueden reservar la próxima sesión desde la web, y los recordatorios les llegan igual. Si preferís otra forma de manejar los turnos fijos, lo vemos en el diagnóstico."),
            ("¿El asistente habla con mis pacientes sobre lo que les pasa?", "No. Solo responde preguntas prácticas (horarios, honorarios, cómo llegar). Nunca da indicaciones de salud y, ante una crisis, indica comunicarse con un servicio de emergencias."),
            ("¿Cuánto cuesta?", "Depende de lo que necesites: lo vemos en el diagnóstico gratis y te pasamos una propuesta por escrito. La web con turnos online arranca en USD 320 (en pesos al dólar oficial, en dos pagos) y el acompañamiento mensual en USD 32."),
        ],
        "cierre": "Que pedir el primer turno sea fácil. Lo demás, lo hablan en sesión.",
    },
    {
        "slug": "medicos", "listo": True,
        "nombre": "Médicos", "nombre_corto": "médicos", "audiencia": "Médicos, especialistas y consultorios médicos",
        "servicio": "Web y turnos online para médicos",
        "titulo": "Turnos online para médicos en Rosario | NeoAtlantis",
        "descripcion": "Web y turnos online para médicos y especialistas en Rosario y Villa Gobernador Gálvez: reservas las 24 h, recordatorios automáticos y menos ausencias.",
        "eyebrow": "Para médicos y especialistas · Rosario y Villa Gobernador Gálvez",
        "h1": "Turnos online para tu consultorio médico",
        "sub": "Tus pacientes reservan solos, a cualquier hora, y reciben su recordatorio. Vos confirmás con un toque y la secretaría deja de vivir en el teléfono.",
        "wa": "Hola NeoAtlantis, soy médico/a y quiero consultar por los turnos online.",
        "dolores_titulo": "Lo que pasa todos los días en un consultorio médico",
        "dolores_intro": "La agenda no se desordena por falta de ganas: se desordena porque depende de que alguien atienda el teléfono todo el tiempo.",
        "dolores": [
            ("El teléfono no para", "Pedidos de turno, cambios y cancelaciones interrumpen la atención y se acumulan en la secretaría."),
            ("Pacientes que faltan sin avisar", "Turnos dados con semanas de anticipación que se olvidan, y huecos que ya no se pueden ofrecer."),
            ("Primera consulta y control no duran lo mismo", "Dar el mismo turno a todos atrasa el día o deja tiempos muertos."),
            ("Pacientes que no vuelven al control", "Nadie les recordó el control anual o el seguimiento, y vuelven cuando el problema ya creció."),
            ("Mensajes fuera de horario", "WhatsApp a la noche para pedir turno, que alguien tiene que contestar a la mañana."),
            ("No aparecés en Google", "Quien busca tu especialidad en la zona encuentra primero a otro consultorio."),
        ],
        "solucion_intro": "Una web propia con reserva online y automatizaciones que trabajan solas. Te marco qué incluye el paquete, qué suma el plan mensual y qué se agrega aparte, para que no haya sorpresas.",
        "soluciones": [
            ("Tu web con turnos online las 24 horas", "El paciente elige el tipo de consulta, día y horario, y solo ve los horarios libres. Sin doble reserva.", "inc"),
            ("Cada turno nuevo te llega a Telegram", "Lo aprobás vos o tu secretaria con un toque, y el paciente recibe la confirmación por email.", "inc"),
            ("Recordatorios 24 h y 2 h antes", "Con un botón para cancelar: si el paciente no puede venir, el horario se libera solo.", "inc"),
            ("Tu ficha de Google para aparecer en Maps", "Configurada y conectada con tu web, para que te encuentren cuando buscan tu especialidad.", "inc"),
            ("Confirmación en tres tiempos (72, 24 y 2 h)", "El paciente confirma, cambia el horario o cancela con un toque, y vos te enterás por Telegram.", "plan"),
            ("Un asistente que responde las preguntas de siempre", "Horarios, obras sociales, qué traer, cómo llegar. Ante una urgencia indica llamar al consultorio o a emergencias. Nunca da indicaciones de salud.", "plan"),
            ("Reporte de los lunes", "Por Telegram: quién viene esta semana, quién confirmó y qué falta aprobar.", "plan"),
            ("Agenda por tipo de consulta", "La primera consulta, el control y los estudios ocupan cada uno su tiempo real.", "extra"),
            ("Lista de espera", "Si un día está completo, el paciente se anota. Si alguien cancela, le llega un email para reservar ese horario.", "extra"),
            ("Aviso de control", "Un email a los pacientes que no volvieron en el tiempo que vos definas, solo si aceptaron recibir avisos.", "extra"),
            ("Pedido de reseña en Google", "Después de la consulta, el mismo email a todos con el botón para dejar su opinión.", "extra"),
        ],
        "demo_titulo": "Probalo vos mismo",
        "demo_texto": "Un consultorio de ejemplo con todo funcionando: reserva por tipo de consulta, asistente y lista de espera. Es de odontología, pero el sistema es el mismo y se adapta a tu especialidad.",
        "demo_url": "https://consultorio-dental-flax.vercel.app/", "demo_boton": "Abrir la demo",
        "faq": [
            ("¿Funciona con obras sociales y prepagas?", "Sí. El sistema organiza los turnos; no factura ni gestiona autorizaciones. El asistente puede informar con cuáles trabajás y se puede pedir la obra social al reservar."),
            ("¿Sirve si somos varios profesionales?", "Sí. Si cada uno tiene su agenda, lo vemos en el diagnóstico y lo adaptamos."),
            ("¿Qué pasa con las urgencias?", "No se reservan como un turno común: la web y el asistente le indican al paciente que llame al consultorio o a emergencias."),
            ("¿Mi secretaria puede seguir dando turnos por teléfono?", "Sí. Los turnos online conviven con los que se dan por teléfono, y los recordatorios les llegan a todos los que dejaron su email."),
            ("¿Qué datos de los pacientes se guardan?", "Solo los del turno: nombre, contacto, tipo de consulta, día y hora. Nunca historia clínica ni información de salud. Los datos son tuyos."),
            ("¿Cuánto cuesta?", "Depende de lo que necesites: lo vemos en el diagnóstico gratis y te pasamos una propuesta por escrito. La web con turnos online arranca en USD 320 (en pesos al dólar oficial, en dos pagos) y el acompañamiento mensual en USD 32."),
        ],
        "cierre": "Menos teléfono, menos ausencias, más tiempo para atender.",
    },
    {
        "slug": "kinesiologos-nutricionistas", "listo": True,
        "nombre": "Kinesiólogos y nutricionistas", "nombre_corto": "kinesiólogos y nutricionistas", "audiencia": "Kinesiólogos, nutricionistas y profesionales que atienden por sesiones",
        "servicio": "Web y turnos online para kinesiólogos y nutricionistas",
        "titulo": "Turnos online para kinesiólogos y nutricionistas | NeoAtlantis",
        "descripcion": "Web y turnos online para kinesiólogos y nutricionistas en Rosario y Villa Gobernador Gálvez: sesiones y controles con recordatorio automático y menos abandonos.",
        "eyebrow": "Para kinesiólogos y nutricionistas · Rosario y Villa Gobernador Gálvez",
        "h1": "Turnos online para kinesiólogos y nutricionistas",
        "sub": "Cuando el tratamiento es de varias sesiones, cada turno que se pierde se nota. Que reserven solos, que no se olviden y que no abandonen a mitad de camino.",
        "wa": "Hola NeoAtlantis, soy kinesiólogo/a o nutricionista y quiero consultar por los turnos online.",
        "dolores_titulo": "Lo que pasa todos los días cuando atendés por sesiones",
        "dolores_intro": "Un tratamiento de 10 sesiones o un control cada 15 días depende de que el paciente vuelva. Estos son los problemas de siempre.",
        "dolores": [
            ("Muchas sesiones, mucho ida y vuelta", "Cada paciente necesita varios turnos, y coordinarlos por WhatsApp lleva tiempo todos los días."),
            ("Pacientes que abandonan a mitad de tratamiento", "Faltan a una sesión, después a otra, y un día dejan de venir sin avisar."),
            ("Olvidos de la sesión de la semana", "El paciente no tiene el turno anotado y se entera tarde."),
            ("Huecos que nadie aprovecha", "Una cancelación deja libre un horario que otro paciente quería."),
            ("Controles que se postergan", "En nutrición, el control que no se agenda en el momento muchas veces no se agenda nunca."),
            ("No aparecés en Google", "Quien busca kinesiólogo o nutricionista en la zona encuentra primero a otro."),
        ],
        "solucion_intro": "Una web propia con reserva online y avisos que ayudan a sostener el tratamiento. Te marco qué incluye el paquete, qué suma el plan mensual y qué se agrega aparte.",
        "soluciones": [
            ("Tu web con turnos online las 24 horas", "El paciente reserva su próxima sesión o control desde el celular, viendo solo los horarios libres.", "inc"),
            ("Cada turno nuevo te llega a Telegram", "Lo aprobás o lo rechazás con un toque, y el paciente recibe la confirmación por email.", "inc"),
            ("Recordatorios 24 h y 2 h antes", "Con un botón para cancelar: si el paciente no puede venir, el horario se libera solo.", "inc"),
            ("Tu ficha de Google para aparecer en Maps", "Configurada y conectada con tu web, para que te encuentren en tu zona.", "inc"),
            ("Confirmación en tres tiempos (72, 24 y 2 h)", "El paciente confirma, cambia el horario o cancela con un toque, y vos te enterás por Telegram.", "plan"),
            ("Un asistente que responde las preguntas de siempre", "Horarios, obras sociales, qué traer, cómo llegar. Nunca da indicaciones de salud.", "plan"),
            ("Reporte de los lunes", "Por Telegram: quién viene esta semana y quién confirmó.", "plan"),
            ("Duración por tipo de sesión", "La evaluación inicial, la sesión y el control ocupan cada uno su tiempo real.", "extra"),
            ("Lista de espera", "Si un día está completo, el paciente se anota. Si alguien cancela, le llega un email para reservar ese horario.", "extra"),
            ("Aviso para retomar", "Un email a los pacientes que dejaron de venir, en el tiempo que vos definas, solo si aceptaron recibir avisos.", "extra"),
            ("Pedido de reseña en Google", "Al terminar, el mismo email a todos con el botón para dejar su opinión.", "extra"),
        ],
        "demo_titulo": "Probalo vos mismo",
        "demo_texto": "Un consultorio de ejemplo con todo funcionando: reserva por tipo de turno, asistente y lista de espera. Es de odontología, pero el sistema es el mismo y se adapta a tu forma de atender.",
        "demo_url": "https://consultorio-dental-flax.vercel.app/", "demo_boton": "Abrir la demo",
        "faq": [
            ("¿Sirve para tratamientos de varias sesiones?", "Sí. El paciente reserva cada sesión desde la web y recibe su recordatorio. Si preferís dejar armadas varias sesiones de una vez, lo vemos en el diagnóstico."),
            ("¿Funciona con obras sociales y órdenes médicas?", "El sistema organiza los turnos; no gestiona autorizaciones ni cuenta las sesiones de la orden. Se puede pedir la obra social al reservar."),
            ("¿Sirve si atiendo en más de un lugar?", "Sí. Lo vemos en el diagnóstico para que el paciente elija dónde atenderse y vos sepas dónde tenés que estar."),
            ("¿Los pacientes tienen que bajar una app?", "No. Reservan desde tu web con nombre, teléfono y email."),
            ("¿Qué datos de los pacientes se guardan?", "Solo los del turno: nombre, contacto, tipo de sesión, día y hora. Nunca información clínica. Los datos son tuyos."),
            ("¿Cuánto cuesta?", "Depende de lo que necesites: lo vemos en el diagnóstico gratis y te pasamos una propuesta por escrito. La web con turnos online arranca en USD 320 (en pesos al dólar oficial, en dos pagos) y el acompañamiento mensual en USD 32."),
        ],
        "cierre": "Que cada sesión llegue a la agenda, y cada paciente, al final del tratamiento.",
    },
]

GUIAS = [
    {
        "slug": "turnos-whatsapp-vs-turnos-online",
        "corto": "WhatsApp vs. turnos online",
        "corto_largo": "Turnos por WhatsApp o turnos online: qué le conviene a tu consultorio",
        "titulo": "Turnos por WhatsApp o turnos online: qué conviene | NeoAtlantis",
        "descripcion": "Ventajas y límites de dar turnos por WhatsApp, qué resuelve un sistema de turnos online y cómo combinar los dos en tu consultorio sin perder pacientes.",
        "h1": "Turnos por WhatsApp o turnos online: qué le conviene a tu consultorio",
        "bajada": "WhatsApp es cercano y todos lo usan, pero dar turnos por chat tiene un costo que no siempre se ve. Qué gana y qué pierde cada opción, y cómo combinarlas.",
        "fecha": "2026-10-11", "fecha_txt": "11 de octubre de 2026", "minutos": 6,
        "wa": "Hola NeoAtlantis, leí la guía de WhatsApp vs. turnos online y quiero consultar por mi consultorio.",
        "cta_titulo": "¿Querés sumar turnos online sin dejar WhatsApp?",
        "cta_texto": "Tu web con reserva las 24 horas, recordatorios automáticos y el link para mandar por WhatsApp. En un diagnóstico gratis de 15 minutos vemos cómo das los turnos hoy y qué te conviene.",
        "fuentes": [
            ("Medical Economics (2019). Survey: Patients want timely care, digital communication. Encuesta de DocASAP y OnePoll a 1.000 adultos de EE. UU.", "https://www.medicaleconomics.com/view/survey-patients-want-timely-care-digital-communication"),
            ("Ley 25.326 de Protección de los Datos Personales (Argentina). InfoLEG.", "https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm"),
            ("Ley 26.529 de Derechos del Paciente (Argentina). InfoLEG.", "https://servicios.infoleg.gob.ar/infolegInternet/anexos/160000-164999/160432/texact.htm"),
        ],
        "cuerpo": """
<div class="indice"><b>En esta guía</b><ol>
<li><a href="#whatsapp">Lo bueno de dar turnos por WhatsApp</a></li>
<li><a href="#limites">Dónde se complica</a></li>
<li><a href="#online">Qué resuelve un sistema de turnos online</a></li>
<li><a href="#comparacion">Comparación rápida</a></li>
<li><a href="#combinar">La mejor opción: combinarlos</a></li>
</ol></div>

<p>En la mayoría de los consultorios, los turnos se dan por WhatsApp. Tiene sentido: es lo que todos usan y se siente cercano. La pregunta no es si WhatsApp sirve, sino <strong>cuánto te está costando usarlo para todo</strong>, y si hay una forma mejor de repartir el trabajo.</p>

<h2 id="whatsapp">1. Lo bueno de dar turnos por WhatsApp</h2>
<ul>
<li><strong>Todos lo tienen.</strong> El paciente no tiene que aprender nada nuevo.</li>
<li><strong>Es cercano.</strong> Se pueden resolver dudas, explicar una preparación o calmar a alguien que está nervioso.</li>
<li><strong>Es gratis</strong> y se empieza hoy, sin configurar nada.</li>
</ul>
<p>Para conversar con el paciente, WhatsApp es difícil de reemplazar. El problema aparece cuando además se usa como agenda.</p>

<h2 id="limites">2. Dónde se complica</h2>
<h3>Cada turno es una conversación</h3>
<p>«¿Tenés algo el martes?» «A la tarde.» «Tengo 17 o 18:30.» «¿Y el miércoles?»… Un turno que en una agenda se reserva en un minuto, por chat puede llevar varios mensajes de ida y vuelta, y alguien tiene que estar atento para responderlos.</p>
<h3>Los pacientes escriben cuando pueden, no cuando atendés</h3>
<p>Muchos pacientes piden turno a la noche o el fin de semana. En una encuesta de DocASAP a 1.000 adultos de EE. UU., el <strong>84 % dijo que poder reservar fuera del horario de atención le resulta algo o muy importante</strong>. No encontramos un dato equivalente para Argentina, pero cualquier consultorio que use WhatsApp conoce los mensajes de las 23 h. Si el paciente no tiene respuesta, a veces le escribe a otro profesional.</p>
<h3>La agenda queda en dos lugares</h3>
<p>El turno se acuerda en el chat y después hay que pasarlo a mano a la agenda. Ahí aparecen los errores: un horario dado dos veces, un turno que nunca se anotó, un cambio que quedó en el chat y no en la agenda.</p>
<h3>Los recordatorios dependen de que alguien se acuerde</h3>
<p>Mandar el recordatorio de cada turno, uno por uno, es justo la tarea que se saltea los días con mucho trabajo. Y son los recordatorios los que más ayudan a que los pacientes no falten (lo vimos en la <a href="/guias/reducir-ausentismo-pacientes/">guía de ausentismo</a>).</p>
<h3>Datos de salud en el celular</h3>
<p>Por chat, los pacientes suelen contar el motivo de la consulta, mandar estudios o fotos. Para la ley argentina, la información sobre la salud es un <strong>dato sensible</strong> (Ley 25.326), y el paciente tiene derecho a la <strong>confidencialidad</strong> de su documentación clínica (Ley 26.529). Si el WhatsApp del consultorio está en el celular personal, o lo comparten varias personas, conviene pensar quién puede ver esas conversaciones.</p>

<h2 id="online">3. Qué resuelve un sistema de turnos online</h2>
<ul>
<li><strong>El paciente reserva solo, a cualquier hora</strong>, viendo únicamente los horarios libres. Sin ida y vuelta.</li>
<li><strong>Una sola agenda.</strong> Lo que se reserva ya está anotado: no hay que pasar nada a mano ni hay doble reserva.</li>
<li><strong>Confirmación por escrito</strong> con día, hora y dirección.</li>
<li><strong>Recordatorios automáticos</strong>, con un botón para cancelar que libera el horario.</li>
<li><strong>Solo los datos del turno</strong>: nombre, contacto, día y hora. Lo clínico queda dentro del consultorio.</li>
</ul>
<p>Lo que no reemplaza: la conversación. Si el paciente tiene una duda o una urgencia, tiene que seguir pudiendo hablar con vos.</p>

<h2 id="comparacion">4. Comparación rápida</h2>
<div class="tabla"><table>
<thead><tr><th></th><th>Turnos por WhatsApp</th><th>Turnos online</th></tr></thead>
<tbody>
<tr><td><strong>Reservar a la noche</strong></td><td>El paciente escribe y espera respuesta</td><td>Reserva en el momento</td></tr>
<tr><td><strong>Tiempo por turno</strong></td><td>Varios mensajes de ida y vuelta</td><td>Ninguno: llega anotado</td></tr>
<tr><td><strong>Doble reserva</strong></td><td>Posible, si se anota a mano</td><td>No: solo se ven los horarios libres</td></tr>
<tr><td><strong>Recordatorios</strong></td><td>A mano, uno por uno</td><td>Automáticos</td></tr>
<tr><td><strong>Cancelaciones</strong></td><td>Hay que leerlas y reacomodar</td><td>El horario se libera solo</td></tr>
<tr><td><strong>Dudas y urgencias</strong></td><td>Ideal para conversar</td><td>Necesita un canal de contacto al lado</td></tr>
<tr><td><strong>Costo</strong></td><td>Gratis, pero se paga en tiempo</td><td>Tiene un costo de armado y mantenimiento</td></tr>
</tbody></table></div>

<h2 id="combinar">5. La mejor opción: combinarlos</h2>
<p>No hace falta elegir. Lo que mejor funciona es que <strong>cada herramienta haga lo suyo</strong>:</p>
<ul>
<li><strong>Los turnos, por la web.</strong> Cuando alguien pide turno por WhatsApp, respondé con el link de reserva. Con WhatsApp Business podés dejarlo en la <strong>respuesta automática</strong> y en el perfil, así también le llega a quien escribe de noche.</li>
<li><strong>Las conversaciones, por WhatsApp.</strong> Dudas, preparación para un estudio, algo que no se resuelve con un formulario.</li>
<li><strong>Las urgencias, por teléfono.</strong> Que estén claras en la web y en la respuesta automática, para que nadie espere un mensaje.</li>
<li><strong>Nada clínico por chat</strong> si se puede evitar: pedile al paciente que lo traiga a la consulta.</li>
</ul>
<div class="nota"><strong>Para decidir:</strong> si respondés pocos turnos por semana y nunca se te mezclan, WhatsApp solo puede alcanzar. Si pasás más de un rato por día respondiendo turnos, tenés pacientes que faltan sin avisar o te escriben fuera de horario, los turnos online te devuelven ese tiempo.</div>
""",
    },
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
    {
        "slug": "aparecer-en-google-maps-consultorio",
        "corto": "Aparecer en Google Maps",
        "corto_largo": "Cómo aparecer en Google Maps siendo profesional de la salud en Rosario",
        "titulo": "Cómo aparecer en Google Maps con tu consultorio en Rosario | NeoAtlantis",
        "descripcion": "Paso a paso para crear y completar tu Perfil de Negocio de Google, aparecer en Maps cuando buscan tu especialidad en Rosario y conseguir reseñas sin romper reglas.",
        "h1": "Cómo aparecer en Google Maps siendo profesional de la salud en Rosario",
        "bajada": "Cuando alguien busca «psicólogo en Rosario» u «odontólogo cerca», lo primero que ve es el mapa. Cómo crear tu ficha gratis, qué completar para que Google te muestre y cómo pedir reseñas cuidando a tus pacientes.",
        "fecha": "2026-10-14", "fecha_txt": "14 de octubre de 2026", "minutos": 7,
        "wa": "Hola NeoAtlantis, leí la guía de Google Maps y quiero consultar por mi consultorio.",
        "cta_titulo": "¿Querés saber cómo te ve hoy un paciente que te busca?",
        "cta_texto": "En 3 minutos, el autodiagnóstico gratis te muestra qué te falta en Google, en tu web y en tus turnos, y cuánto se te escapa por mes.",
        "fuentes": [
            ("Google. Sugerencias para mejorar tu ranking local en Google (Ayuda de Perfil de Negocio de Google).", "https://support.google.com/business/answer/7091?hl=es-419"),
            ("Google. Contenido prohibido y restringido (Política de contenido aportado por los usuarios de Maps).", "https://support.google.com/contributionpolicy/answer/7400114?hl=es-419"),
        ],
        "cuerpo": """
<div class="indice"><b>En esta guía</b><ol>
<li><a href="#por-que">Por qué Maps importa tanto</a></li>
<li><a href="#crear">Crear y verificar tu ficha</a></li>
<li><a href="#completar">Qué completar para que Google te muestre</a></li>
<li><a href="#resenas">Reseñas: cómo pedirlas y cómo responderlas</a></li>
<li><a href="#errores">Errores comunes</a></li>
</ol></div>

<p>Muchos pacientes ya no preguntan a un conocido: abren Google, escriben su especialidad y su barrio, y eligen entre los primeros tres consultorios que aparecen en el mapa. Si tu consultorio no está ahí, para esa persona no existe, aunque tengas años de trayectoria.</p>

<h2 id="por-que">1. Por qué Maps importa tanto</h2>
<p>En las búsquedas con intención local («kinesiólogo en Rosario», «dentista cerca de mí»), Google muestra un bloque con mapa y tres fichas <strong>antes</strong> que las páginas web. Esas fichas salen del <strong>Perfil de Negocio de Google</strong>, que es gratis.</p>
<p>Según la ayuda oficial de Google, el orden depende de tres cosas:</p>
<ul>
<li><strong>Relevancia:</strong> qué tan bien coincide tu ficha con lo que se buscó. Por eso importa completarla bien.</li>
<li><strong>Distancia:</strong> qué tan cerca estás de quien busca o del lugar que nombró.</li>
<li><strong>Prominencia:</strong> qué tan conocido es tu consultorio, incluyendo la cantidad de reseñas, su puntuación y la presencia en la web.</li>
</ul>
<p>La distancia no la podés cambiar. Las otras dos, sí.</p>

<h2 id="crear">2. Crear y verificar tu ficha</h2>
<ol>
<li>Entrá a <strong>business.google.com</strong> con la cuenta de Google que vas a usar para el consultorio.</li>
<li>Escribí el nombre del consultorio tal como lo ven tus pacientes (sin agregar palabras de relleno como «el mejor» o «barato»: Google lo penaliza).</li>
<li>Elegí la <strong>categoría principal</strong> más precisa posible: «Psicólogo», «Dentista», «Kinesiólogo», «Nutricionista»… No pongas una genérica como «Servicio de salud» si existe la tuya.</li>
<li>Si atendés en un consultorio al que van los pacientes, cargá la dirección. Si atendés en tu casa y no querés mostrarla, o hacés solo consultas online, podés configurarlo para mostrar la <strong>zona de atención</strong> sin publicar la dirección.</li>
<li><strong>Verificá</strong> la ficha. Google te va a pedir una forma de comprobar que el consultorio es tuyo (un video corto, un llamado o un código, según el caso). Hasta que no esté verificada, no aparece bien.</li>
</ol>

<h2 id="completar">3. Qué completar para que Google te muestre</h2>
<p>Una ficha completa es la forma más directa de mejorar la relevancia. Revisá que tenga:</p>
<ul>
<li><strong>Horarios reales</strong>, incluidos los feriados. Una ficha con horarios desactualizados genera desconfianza.</li>
<li><strong>Teléfono y WhatsApp</strong> que alguien conteste.</li>
<li><strong>El link a tu web</strong> y, si tenés, <strong>el link para reservar turno</strong>. Así el paciente pasa de buscarte a reservar sin escribirte.</li>
<li><strong>Servicios</strong> con nombres que la gente busca: «limpieza dental», «primera entrevista», «terapia online», «rehabilitación de rodilla».</li>
<li><strong>Una descripción</strong> corta y clara: qué hacés, para quién y dónde. Sin promesas de resultados.</li>
<li><strong>Fotos reales:</strong> la fachada (para que te encuentren), la sala de espera y el consultorio. Nunca fotos de pacientes.</li>
</ul>
<div class="nota"><strong>Coherencia:</strong> el nombre, la dirección y el teléfono tienen que ser iguales en tu ficha, tu web, Instagram y cualquier directorio en el que aparezcas. Si en un lado dice «Calle 9 de Julio 1234» y en otro «9 de julio 1234 PB», Google tiene menos certeza de que sos el mismo consultorio.</div>

<h2 id="resenas">4. Reseñas: cómo pedirlas y cómo responderlas</h2>
<p>Las reseñas pesan en la prominencia y, sobre todo, en la decisión del paciente. Algunas reglas:</p>
<ul>
<li><strong>Pedilas a todos por igual</strong>, después de la consulta, con el link directo a tu ficha. Google no permite ofrecer descuentos o regalos a cambio de reseñas, ni pedirlas solo a quienes sabés que están contentos.</li>
<li><strong>No las escribas vos ni pidas que las inventen.</strong> Google las detecta y puede eliminarlas o sancionar la ficha.</li>
<li><strong>Respondé todas</strong>, las buenas y las malas, con calma y en pocas líneas.</li>
<li><strong>Al responder, no confirmes que la persona es tu paciente ni menciones nada de su atención.</strong> Ante una crítica: «Gracias por tu comentario. Nos gustaría conocer más; podés escribirnos al [teléfono]». El secreto profesional también corre en internet.</li>
</ul>

<h2 id="errores">5. Errores comunes</h2>
<ul>
<li><strong>Tener dos fichas</strong> del mismo consultorio (una vieja y una nueva). Reclamá la vieja y pedí unificarlas.</li>
<li><strong>Elegir mal la categoría</strong> o no agregar categorías secundarias si hacés más de una cosa.</li>
<li><strong>Crear la ficha y olvidarla.</strong> Publicar una novedad o una foto de vez en cuando muestra que el consultorio está activo.</li>
<li><strong>Mandar todo al WhatsApp.</strong> Si la ficha solo tiene un número, cada paciente nuevo te cuesta un ida y vuelta. Con un link de reserva, el turno queda tomado aunque estés atendiendo.</li>
</ul>
<p>Crear y completar la ficha lleva una o dos horas, una sola vez. Es probablemente la hora mejor invertida para que te encuentren pacientes nuevos en Rosario y alrededores.</p>
""",
    },
    {
        "slug": "recordatorios-automaticos-de-turnos",
        "corto": "Recordatorios automáticos",
        "corto_largo": "Recordatorios automáticos de turnos: cuándo mandarlos y qué decir",
        "titulo": "Recordatorios automáticos de turnos: cuándo y qué decir | NeoAtlantis",
        "descripcion": "Cuándo mandar los recordatorios de turno, por qué canal (email, WhatsApp o SMS), qué tienen que decir y qué nunca poner. Con textos de ejemplo para copiar.",
        "h1": "Recordatorios automáticos de turnos: cuándo mandarlos y qué decir",
        "bajada": "El recordatorio es la medida más simple contra los turnos vacíos. Cuándo mandarlo, por qué canal, qué escribir y cómo dejar de hacerlo a mano.",
        "fecha": "2026-10-16", "fecha_txt": "16 de octubre de 2026", "minutos": 6,
        "wa": "Hola NeoAtlantis, leí la guía de recordatorios y quiero consultar por mi consultorio.",
        "cta_titulo": "¿Cuántos turnos se te pierden hoy?",
        "cta_texto": "En 3 minutos, el autodiagnóstico gratis calcula cuánto se te escapa por mes en turnos vacíos y cuánto podrías recuperar con recordatorios.",
        "fuentes": [
            ("Gurol-Urganci I. y otros (2013). Mobile phone messaging reminders for attendance at healthcare appointments. Cochrane Database of Systematic Reviews.", "https://www.cochrane.org/evidence/CD007458_mobile-phone-messaging-reminders-attendance-healthcare-appointments"),
            ("Meta. Precios de la plataforma de WhatsApp Business.", "https://developers.facebook.com/docs/whatsapp/pricing"),
        ],
        "cuerpo": """
<div class="indice"><b>En esta guía</b><ol>
<li><a href="#cuando">Cuándo mandarlos</a></li>
<li><a href="#canal">Por qué canal</a></li>
<li><a href="#que-decir">Qué decir (con ejemplos)</a></li>
<li><a href="#nunca">Lo que nunca va en un recordatorio</a></li>
<li><a href="#automatico">Dejar de hacerlo a mano</a></li>
</ol></div>

<p>Muchos consultorios ya mandan recordatorios, pero a mano: alguien revisa la agenda del día siguiente y escribe uno por uno. Funciona mientras hay tiempo, y es lo primero que se deja de hacer en una semana cargada, justo cuando más falta hace.</p>

<h2 id="cuando">1. Cuándo mandarlos</h2>
<p>Una revisión de la Cochrane sobre ensayos clínicos encontró que <strong>los recordatorios por mensaje aumentan la asistencia</strong> frente a no mandar nada. Lo que mejor funciona en la práctica es combinar dos momentos:</p>
<ul>
<li><strong>Uno con tiempo, 24 horas antes</strong> (o hasta 72 si das turnos con mucha anticipación). Sirve para que quien no puede venir avise a tiempo y ese horario se pueda volver a ofrecer.</li>
<li><strong>Uno cercano, 2 horas antes.</strong> Es para el olvido de último momento.</li>
</ul>
<p>Si das turnos a varias semanas, un tercer aviso al momento de reservar (la confirmación escrita) cierra el círculo.</p>

<h2 id="canal">2. Por qué canal</h2>
<div class="tabla"><table>
<tr><th>Canal</th><th>A favor</th><th>A tener en cuenta</th></tr>
<tr><td>Email</td><td>Gratis, queda guardado, permite un botón para cancelar.</td><td>Algunos pacientes no lo miran seguido. Conviene pedir el email al reservar.</td></tr>
<tr><td>WhatsApp manual</td><td>Todos lo leen.</td><td>Alguien tiene que mandarlo uno por uno, todos los días.</td></tr>
<tr><td>WhatsApp automático</td><td>Todos lo leen y no depende de nadie.</td><td>Requiere la plataforma oficial de WhatsApp Business, con plantillas aprobadas por Meta y un costo por mensaje.</td></tr>
<tr><td>SMS</td><td>Llega a cualquier celular.</td><td>Tiene costo por mensaje y poco espacio para el texto.</td></tr>
</table></div>
<p>No hay un canal perfecto. Lo importante es que el recordatorio <strong>salga siempre</strong>, sin depender de que alguien se acuerde.</p>

<h2 id="que-decir">3. Qué decir (con ejemplos)</h2>
<p>Un buen recordatorio es corto y responde cuatro cosas: <strong>quién, cuándo, dónde y cómo cancelar</strong>.</p>
<div class="nota"><strong>24 horas antes:</strong><br>Hola, Laura. Te recordamos tu turno de mañana jueves 17 a las 10:30 con la Lic. Pérez, en Córdoba 1234, Rosario. Si no podés venir, cancelá acá así el horario queda para otro paciente: [botón Cancelar].</div>
<div class="nota"><strong>2 horas antes:</strong><br>Hola, Laura. Te esperamos hoy a las 10:30 en Córdoba 1234. ¡Hasta pronto!</div>
<p>El botón de cancelar parece ir en contra, pero <strong>reduce las ausencias</strong>: el paciente que no puede venir avisa en vez de desaparecer, y ese horario se puede volver a ocupar.</p>

<h2 id="nunca">4. Lo que nunca va en un recordatorio</h2>
<ul>
<li><strong>El motivo de la consulta</strong> ni ningún dato de salud. Un mensaje puede verlo otra persona en la pantalla del celular.</li>
<li><strong>El tipo de tratamiento</strong> cuando revela información sensible.</li>
<li><strong>Datos de pago</strong> o links a sitios que no sean los tuyos.</li>
</ul>
<p>Día, hora, profesional, dirección y cómo cancelar alcanzan.</p>

<h2 id="automatico">5. Dejar de hacerlo a mano</h2>
<p>Si tus turnos ya están en una agenda online, los recordatorios pueden salir solos: el sistema sabe quién tiene turno y a qué hora, y manda cada aviso en su momento. Si un paciente cancela, el horario vuelve a quedar libre en la agenda sin que tengas que tocar nada.</p>
<p>Si hoy das los turnos por WhatsApp o por teléfono, el primer paso es que queden <strong>escritos en un solo lugar</strong>. Sin eso, no hay forma de automatizar nada.</p>
""",
    },
    {
        "slug": "psicologo-web-o-instagram",
        "corto": "¿Web o Instagram?",
        "corto_largo": "¿Necesita web un psicólogo si ya tiene Instagram?",
        "titulo": "¿Necesita web un psicólogo si ya tiene Instagram? | NeoAtlantis",
        "descripcion": "Qué te da Instagram, qué no, y qué resuelve una web propia en un consultorio de psicología: cómo te encuentran en Google, primera consulta y confidencialidad.",
        "h1": "¿Necesita web un psicólogo si ya tiene Instagram?",
        "bajada": "Instagram sirve para que te conozcan. La web sirve para que te encuentren y te consulten. Qué hace bien cada uno y cuándo conviene sumar la web.",
        "fecha": "2026-10-16", "fecha_txt": "16 de octubre de 2026", "minutos": 5,
        "wa": "Hola NeoAtlantis, leí la guía de web o Instagram y quiero consultar por mi consultorio.",
        "cta_titulo": "¿Cómo te encuentra hoy un paciente?",
        "cta_texto": "El autodiagnóstico gratis te muestra en 3 minutos qué te falta para que te encuentren y te consulten. Sin compromiso.",
        "fuentes": [
            ("Google. Sugerencias para mejorar tu ranking local en Google (Ayuda de Perfil de Negocio de Google).", "https://support.google.com/business/answer/7091?hl=es-419"),
        ],
        "cuerpo": """
<div class="indice"><b>En esta guía</b><ol>
<li><a href="#instagram">Lo que Instagram hace bien</a></li>
<li><a href="#limites">Lo que Instagram no resuelve</a></li>
<li><a href="#web">Qué agrega una web propia</a></li>
<li><a href="#cuando">¿Cuándo conviene?</a></li>
</ol></div>

<p>Muchos psicólogos tienen una cuenta de Instagram cuidada, con contenido valioso y seguidores que los aprecian. La pregunta es razonable: si ya estoy ahí, ¿para qué una web?</p>

<h2 id="instagram">1. Lo que Instagram hace bien</h2>
<ul>
<li><strong>Mostrar tu forma de pensar y de trabajar</strong>, algo clave en psicología, donde el vínculo importa tanto.</li>
<li><strong>Mantenerte presente</strong> para quienes ya te siguen.</li>
<li><strong>Generar confianza</strong> antes del primer contacto.</li>
</ul>

<h2 id="limites">2. Lo que Instagram no resuelve</h2>
<ul>
<li><strong>No te encuentra quien no te conoce.</strong> Una persona que busca «psicólogo en Rosario» o «terapia online ansiedad» lo busca en Google, no en Instagram.</li>
<li><strong>La información importante se pierde.</strong> Modalidad, obras sociales, honorarios, horarios y cómo pedir la primera entrevista quedan dispersos entre historias destacadas y publicaciones.</li>
<li><strong>Todo termina en un mensaje directo</strong>, que tenés que responder vos, a veces en medio de una sesión.</li>
<li><strong>La cuenta no es tuya del todo.</strong> Depende de las reglas y los cambios de una plataforma.</li>
</ul>

<h2 id="web">3. Qué agrega una web propia</h2>
<ul>
<li><strong>Aparecer en Google.</strong> Una web, junto con tu ficha de Google Maps, es lo que permite que te encuentre alguien que hoy no sabe que existís. Google tiene en cuenta tu presencia en la web para ordenar los resultados locales.</li>
<li><strong>Toda la información en un lugar:</strong> enfoque, modalidad presencial u online, obras sociales, cómo es la primera entrevista.</li>
<li><strong>Pedir la primera entrevista sin escribirte:</strong> el paciente ve los horarios libres y reserva. Para alguien que duda en consultar, no tener que escribir un mensaje baja mucho la barrera.</li>
<li><strong>Confidencialidad:</strong> en la reserva solo se piden nombre y contacto, nunca el motivo de consulta.</li>
</ul>
<div class="nota"><strong>No es una cosa o la otra.</strong> Lo que mejor funciona es que se conecten: el link de la web en tu biografía de Instagram y el de Instagram en tu web. Instagram genera confianza; la web convierte esa confianza en una primera entrevista.</div>

<h2 id="cuando">4. ¿Cuándo conviene?</h2>
<p>Te conviene sumar una web si te pasa alguna de estas cosas:</p>
<ul>
<li>Querés pacientes nuevos que no te conocen por recomendación.</li>
<li>Respondés muchas veces por día las mismas preguntas por mensaje directo.</li>
<li>Atendés online y querés llegar a personas de otras ciudades.</li>
<li>Coordinar horarios te lleva más tiempo del que te gustaría.</li>
</ul>
<p>Si tu agenda está completa solo con derivaciones y te sobra el tiempo, quizás todavía no la necesites. Y está bien.</p>
""",
    },
    {
        "slug": "lista-de-espera-turnos-cancelados",
        "corto": "Lista de espera",
        "corto_largo": "Lista de espera: cómo llenar los turnos que se cancelan",
        "titulo": "Lista de espera: cómo llenar los turnos cancelados | NeoAtlantis",
        "descripcion": "Cómo armar una lista de espera en tu consultorio para que cada cancelación se convierta en un paciente atendido. Paso a paso, a mano y automática.",
        "h1": "Lista de espera: cómo llenar los turnos que se cancelan",
        "bajada": "Una cancelación con aviso no tiene por qué ser un horario vacío. Cómo armar una lista de espera simple, a mano o automática, para volver a ocupar ese lugar.",
        "fecha": "2026-10-16", "fecha_txt": "16 de octubre de 2026", "minutos": 5,
        "wa": "Hola NeoAtlantis, leí la guía de lista de espera y quiero consultar por mi consultorio.",
        "cta_titulo": "¿Cuántos horarios quedan vacíos por semana?",
        "cta_texto": "El autodiagnóstico gratis lo pasa a pesos en 3 minutos y te dice qué conviene mejorar primero.",
        "fuentes": [],
        "cuerpo": """
<div class="indice"><b>En esta guía</b><ol>
<li><a href="#idea">La idea</a></li>
<li><a href="#mano">Cómo hacerla a mano</a></li>
<li><a href="#reglas">Reglas para que funcione</a></li>
<li><a href="#auto">Cómo funciona automática</a></li>
</ol></div>

<p>Todo consultorio tiene los dos problemas a la vez: días completos donde alguien se queda sin turno y, en esos mismos días, cancelaciones que dejan un horario libre. La lista de espera une las dos cosas.</p>

<h2 id="idea">1. La idea</h2>
<p>Cuando un paciente quiere un día que está completo, en vez de darle un turno lejano y listo, se anota en la lista de ese día. Si alguien cancela, se le avisa a la lista y el primero que confirma se queda con el horario.</p>
<p>Funciona especialmente bien en especialidades con agenda llena y pacientes que preferirían venir antes: odontología, kinesiología, controles médicos.</p>

<h2 id="mano">2. Cómo hacerla a mano</h2>
<ol>
<li>Armá una planilla con cuatro columnas: <strong>nombre, contacto, día o franja que prefiere y fecha en que se anotó</strong>.</li>
<li>Cuando un día se llena, ofrecé anotar al paciente: «Te doy el turno del martes 28, y si se libera algo antes te aviso».</li>
<li>Cuando alguien cancela, escribí a los anotados <strong>de a uno o a todos a la vez</strong>, según tu preferencia (abajo te contamos las ventajas de cada forma).</li>
<li>Quien acepta, se queda con el horario y libera su turno original, que a su vez puede ocupar otro.</li>
</ol>

<h2 id="reglas">3. Reglas para que funcione</h2>
<ul>
<li><strong>Avisar a todos a la vez y que gane el primero</strong> es lo más rápido y lo más justo. Avisar de a uno respeta el orden, pero si el primero tarda en responder, el horario se pierde.</li>
<li><strong>Poné un plazo:</strong> «el primero que confirma en la próxima hora se lo queda».</li>
<li><strong>Limpiá la lista</strong> cada tanto: quien ya se atendió o consiguió turno, sale.</li>
<li><strong>Que cancelar sea fácil.</strong> La lista solo sirve si te enterás de la cancelación con tiempo, y eso pasa cuando el paciente puede cancelar con un toque desde el recordatorio.</li>
</ul>

<h2 id="auto">4. Cómo funciona automática</h2>
<p>A mano, la lista depende de que alguien esté atento justo cuando llega la cancelación. Automatizada, la secuencia es:</p>
<ol>
<li>El paciente cancela desde el recordatorio.</li>
<li>El horario se libera en la agenda.</li>
<li>El sistema avisa solo a los anotados para ese día.</li>
<li>El primero que reserva se queda con el lugar, y el resto ve que ya se ocupó.</li>
</ol>
<p>Vos solo ves que el horario se volvió a llenar.</p>
<div class="nota">Una cancelación con aviso no es el problema. El problema es no enterarse a tiempo o no tener a quién ofrecerle el lugar. Con recordatorios y lista de espera, se resuelven las dos cosas.</div>
""",
    },
    {
        "slug": "doctoralia-o-web-propia",
        "corto": "Doctoralia o web propia",
        "corto_largo": "Doctoralia o web propia: qué le conviene a tu consultorio",
        "titulo": "Doctoralia o web propia: qué conviene a tu consultorio | NeoAtlantis",
        "descripcion": "Diferencias entre estar en un directorio como Doctoralia y tener tu propia web con turnos online: a quién le habla cada uno, de quién son los datos y cómo combinarlos.",
        "h1": "Doctoralia o web propia: qué le conviene a tu consultorio",
        "bajada": "Un directorio te muestra entre muchos profesionales. Tu web te muestra solo a vos. No son lo mismo, y muchas veces conviene tener los dos.",
        "fecha": "2026-10-16", "fecha_txt": "16 de octubre de 2026", "minutos": 5,
        "wa": "Hola NeoAtlantis, leí la guía de Doctoralia y web propia y quiero consultar por mi consultorio.",
        "cta_titulo": "¿Qué te conviene a vos?",
        "cta_texto": "El autodiagnóstico gratis te muestra en 3 minutos dónde estás hoy y qué conviene sumar, con tus números.",
        "fuentes": [],
        "cuerpo": """
<div class="indice"><b>En esta guía</b><ol>
<li><a href="#directorio">Qué es un directorio</a></li>
<li><a href="#web">Qué es una web propia</a></li>
<li><a href="#comparacion">Comparación rápida</a></li>
<li><a href="#combinar">Cómo combinarlos</a></li>
</ol></div>

<p>Doctoralia y otras plataformas similares son conocidas, y muchos profesionales de la salud ya tienen su perfil ahí. La duda aparece cuando alguien ofrece una web propia: ¿hace falta, si ya estoy en la plataforma?</p>
<p>Esta guía no es contra ninguna plataforma. Es para que entiendas qué te da cada opción.</p>

<h2 id="directorio">1. Qué es un directorio</h2>
<p>Un directorio de profesionales es como una cartilla online: el paciente entra, busca una especialidad y una zona, y ve una lista de profesionales. Su gran ventaja es que <strong>la gente ya lo conoce</strong> y lo usa para buscar.</p>
<p>Lo que tenés que saber:</p>
<ul>
<li><strong>Aparecés junto a otros profesionales</strong> de tu especialidad y tu zona.</li>
<li><strong>Las reglas las pone la plataforma:</strong> cómo se ve tu perfil, en qué orden aparecés y cuánto cuesta cada plan.</li>
<li>Los pacientes que llegan por ahí <strong>conocen primero a la plataforma</strong> y después a vos.</li>
</ul>

<h2 id="web">2. Qué es una web propia</h2>
<p>Es tu espacio: tu nombre, tu enfoque, tus fotos, tus servicios y tu agenda de turnos. Cuando alguien entra, solo te ve a vos.</p>
<ul>
<li><strong>Tu marca</strong>, no la de un tercero.</li>
<li><strong>Los datos de tus pacientes quedan con vos.</strong></li>
<li>Con tu <strong>ficha de Google Maps</strong>, es lo que hace que te encuentren por tu nombre o por tu especialidad y zona.</li>
<li>Requiere que alguien la arme y la mantenga, y no trae visitas sola: necesita la ficha de Google y que la compartas.</li>
</ul>

<h2 id="comparacion">3. Comparación rápida</h2>
<div class="tabla"><table>
<tr><th></th><th>Directorio</th><th>Web propia</th></tr>
<tr><td>Quién te encuentra</td><td>Quien busca en la plataforma</td><td>Quien busca en Google o recibe tu link</td></tr>
<tr><td>Junto a quién aparecés</td><td>Otros profesionales de la zona</td><td>Solo vos</td></tr>
<tr><td>Quién pone las reglas</td><td>La plataforma</td><td>Vos</td></tr>
<tr><td>Turnos online</td><td>Sí, en la plataforma</td><td>Sí, en tu web</td></tr>
<tr><td>Si dejás de pagar</td><td>Depende del plan</td><td>Te llevás todo</td></tr>
</table></div>

<h2 id="combinar">4. Cómo combinarlos</h2>
<p>Para muchos profesionales, lo mejor es <strong>tener los dos</strong>:</p>
<ul>
<li>El directorio, para que te encuentren quienes buscan ahí.</li>
<li>La web propia y la ficha de Google, para que quien te busca por tu nombre, o quien te recomendó un colega, llegue directo a vos.</li>
<li>En tus tarjetas, en Instagram y en tu firma de WhatsApp, compartí el link de tu web.</li>
</ul>
<div class="nota">Cuidado con un detalle: si usás dos agendas (la del directorio y la de tu web), tienen que estar sincronizadas para que no se dé el mismo horario dos veces. Si no se pueden conectar, conviene elegir una sola como agenda principal.</div>
""",
    },
]
