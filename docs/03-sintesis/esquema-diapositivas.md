# Esquema de diapositivas

Guion definitivo de la presentación, diapositiva a diapositiva. Está dividido en **4 bloques independientes**, cada uno con su tiempo, contenido, visual, fuente y notas del orador, para poder **repartir** la preparación o los retoques.

!!! info "Cómo usar este esquema"
    - **Una idea por diapositiva:** ≤ 6 puntos y ≤ 12 palabras por punto. Cifras grandes en lugar de párrafos.
    - **Estilo del PPT:** sobrio, en blanco y negro con un único acento morado (`#5B3F8C`). Tipografía Aptos. Sin degradados ni iconos decorativos. El rosa oro es solo de la web.
    - **Las fuentes van en el pie** de cada diapositiva. Lo que se dice va en las **notas del orador**.
    - **Visuales:**
        - los **diagramas propios** están en `docs/assets/diagramas/` y se regeneran con los scripts de `scripts/diagramas/`;
        - las **imágenes ecográficas** están en `docs/assets/img/`, con sus licencias en [créditos](../04-recursos/creditos.md).
    - El PowerPoint se construye desde `presentacion/diapositivas.yaml` con `scripts/build_pptx.py`. El `.pptx` resultante es editable para los retoques finales.

## Reparto por bloques

| Bloque | Diapositivas | Tiempo | Tema | Visuales |
|---|:--:|:--:|---|---|
| **A** | 1–5 | 4,5 min | Apertura y fundamento | Espectro de aireación; imagen real de líneas B |
| **B** | 6–11 | 7 min | Técnica y diagnóstico | 8 zonas; árbol BLUE; LUS frente a Rx; probabilidad pre y postest |
| **C** | 12–16 | 5 min | Diferencial y descongestión | TVP femoral; congestión residual en 8 zonas; *forest plot* |
| **D** | 17–21 | 3,5 min | Integración y cierre | Algoritmo práctico; tabla de guías; cardiogénico frente a no cardiogénico |

**Total: 20 minutos** con 21 diapositivas (la bibliografía no cuenta en el tiempo).

---

## Bloque A · Apertura y fundamento (4,5 min)

### 1 · Portada — 0,5 min
- **Título:** Ecografía pulmonar en la disnea aguda y la insuficiencia cardiaca aguda.
- **Subtítulo:** Del protocolo BLUE a la descongestión guiada por líneas B.
- **Notas:** objetivo de la sesión: «que mañana podáis usar el ecógrafo ante un paciente con disnea y saber qué mirar, qué concluir y qué no».

### 2 · Caso 1: «La radiografía no lo aclara» — 1 min
- Varón de 74 años, HTA, DM, EPOC leve. Disnea de 4 días, ortopnea.
- SpO₂ 88 %, FR 28, sibilancias y crepitantes basales.
- Rx AP en decúbito: «¿redistribución o infiltrado basal?».
- NT-proBNP pendiente (60–90 min).
- **Pregunta a mano alzada:** ¿probabilidad de ICA < 25 %, 25–75 % o > 75 %?
- **Visual:** solo texto (tabla de constantes opcional).
- **Fuente:** caso ficticio docente ([10 · Casos](../02-investigacion/a-disnea-ica/10-casos.md#caso-1)).
- **Notas:** no dar la respuesta; se retoma en la diapositiva 10. El residente plantea salbutamol y antibiótico «por si acaso». Es la situación típica en la que la clínica y la Rx no deciden.

### 3 · El problema: la clínica y la radiografía fallan — 1 min
- Disnea aguda: **≈ 5 %** de las urgencias; la IC es la 2.ª causa.
- Tras un ingreso por ICA: **hasta el 45 %** reingresa o muere en un año.
- Ausencia de crepitantes: LR− de solo **0,51**.
- Radiografía normal en **1 de cada 5** ICA.
- **Visual:** tabla de cuatro cifras.
- **Fuente:** Kelly 2017; Gargani 2023; Wang 2005; Collins 2006.
- **Notas:**
    - En el anciano con insuficiencia respiratoria, el tratamiento inicial es inapropiado en uno de cada tres casos, y la mortalidad pasa del 11 % al 25 % (Ray 2006).
    - En España, más de uno de cada cinco pacientes reingresa en 30 días (Fernández-Gassó 2017).

### 4 · Del aire al agua: líneas A y líneas B — 1 min
- **Visual (diapositiva de imagen):** diagrama `lus-espectro-aireacion.png`: líneas A → líneas B → confluentes → consolidación.
- **Pie:** «Cuanto menos aire y más agua, más líneas B».
- **Fuente:** Demi 2023; Lichtenstein 1997.
- **Notas:**
    - El pulmón aireado no se «ve»: solo produce artefactos.
    - La pleura reverbera y da las **líneas A** (pulmón normal).
    - Cuando los septos subpleurales se engrosan de agua aparecen las **líneas B**. Si confluyen, tenemos el «pulmón blanco»; si se pierde todo el aire, la consolidación.
    - Las líneas B reflejan el agua pulmonar extravascular mejor que la presión de enclavamiento.

### 5 · Qué es (y qué no es) una línea B — 1 min
- Nace de la pleura y llega al fondo de la pantalla.
- Se mueve con el deslizamiento y **borra las líneas A**.
- **≥ 3 por espacio intercostal** = zona positiva.
- No es sinónimo de insuficiencia cardiaca.
- **Visual:** imagen ecográfica real de líneas B (derecha).
- **Fuente:** Volpicelli 2012; Gargani 2023; imagen: ver créditos.
- **Notas:** las líneas Z (cortas, no llegan al fondo) y las líneas E (de enfisema subcutáneo) no son líneas B. Uno o dos por espacio pueden ser normales en las bases.

---

## Bloque B · Técnica y diagnóstico (7 min)

### 6 · Configura el equipo para el pulmón — 1 min
- Preset pulmonar o abdominal.
- **Sin armónicos, sin filtros, sin compuesto**.
- Foco en la pleura, índice mecánico bajo.
- Convexa o microconvexa; lineal para la pleura.
- Para seguir a un paciente: **misma sonda, preset y postura**.
- **Visual:** imagen real de pulmón normal con líneas A, si está disponible.
- **Fuente:** Demi 2023; Gargani 2023; Platz 2015.
- **Notas:** es el error técnico más frecuente, porque los filtros «limpian» precisamente las líneas B. La sonda sectorial es motivo de desacuerdo entre consensos: la EACVI la acepta y el consenso internacional no la recomienda.

### 7 · El protocolo de 8 zonas — 1,5 min
- **Visual (diapositiva de imagen):** diagrama `lus-8-zonas.png`, con el mapa del tórax y la receta de exploración.
- **Fuente:** Gargani 2023 (consenso EACVI); Buessler 2020.
- **Notas:**
    - Son 4 zonas por hemitórax: anterior superior e inferior, y lateral superior e inferior.
    - Se cuenta en el peor espacio de cada zona, con clips de unos 6 s.
    - Las líneas B confluentes se cuentan como el porcentaje de pantalla dividido entre 10.
    - **Edema = ≥ 3 líneas B por zona en ≥ 2 zonas por hemitórax, bilateral.**
    - Los protocolos de 4, 8 y 28 zonas tienen umbrales distintos y **no intercambiables**.

### 8 · El protocolo BLUE en un vistazo — 1,5 min
- **Visual (diapositiva de imagen):** diagrama `lus-arbol-blue.png`, con la rama del perfil B en morado.
- **Fuente:** Lichtenstein 2008; Lichtenstein 2014.
- **Notas:**
    - Tres puntos por hemitórax y siete perfiles.
    - **Perfil B** (líneas B anteriores bilaterales con deslizamiento) = edema hemodinámico.
    - El **perfil A** obliga a mirar las piernas (TEP) y el punto PLAPS (neumonía).
    - El **perfil A′** (sin deslizamiento) con punto pulmón = neumotórax.
    - Acertó el 90,5 % en su estudio original de UCI, con operadores expertos. En urgencias rinde peor para el TEP: lo vemos en el caso 3.

### 9 · ¿Cuánto rinde? Ecografía frente a Rx frente a péptidos — 1,5 min
- **Ecografía:** sensibilidad **88 %** frente al 73 % de la Rx.
- Patrón B: **LR+ 7,4** · LR− 0,16.
- **NT-proBNP < 300:** LR− 0,09, para descartar.
- LUS + clínica mejora más el diagnóstico que Rx + NT-proBNP.
- **Visual:** gráfico `lus-rendimiento-lus-vs-rx.png` (derecha).
- **Fuente:** Maw 2019; Martindale 2016; Pivetta 2019.
- **Notas:**
    - El péptido sirve para **descartar**; la ecografía **confirma y descarta**.
    - En el ECA de Pivetta, añadir la ecografía a la clínica dio un AUC de 0,95, frente a 0,87 con Rx y NT-proBNP.
    - Pulmón y corazón a la vez suben la especificidad al 96 % (Popat 2026).
    - La VCI aislada no sirve para diagnosticar la ICA (Squizzato 2021).

### 10 · Resolución del caso 1 — 1 min
- **Pulmón:** patrón B en 7 de 8 zonas, pleura fina.
- Derrame pleural bilateral pequeño.
- **FoCUS:** FEVI visual muy reducida.
- Diurético i.v. sin esperar al péptido; sin antibiótico.
- **Visual:** gráfico `lus-probabilidad-bayes.png`: 40 % → ≈ 83 % (derecha).
- **Fuente:** Martindale 2016; Popat 2026; Køber 2026 (ESC).
- **Notas:**
    - Recuperar la votación de la diapositiva 2. Las sibilancias eran «asma cardial».
    - Con una probabilidad pretest del 40 %, el patrón B la eleva a ≈ 83 %. Es un cálculo propio con el LR+ de 7,4.
    - Después, ecocardiografía reglada y NT-proBNP con el punto de corte por edad.

### 11 · Mensaje 1 — 0,5 min (diapositiva de mensaje, fondo negro)
- **«Patrón para diagnosticar»**.
- **Subtexto:** líneas B difusas y bilaterales + FoCUS confirman la ICA mejor que la radiografía.

---

## Bloque C · Diferencial y descongestión (5 min)

### 12 · Caso 3: pulmón normal, paciente que no respira bien — 1 min
- Disnea aguda con **perfil A** bilateral.
- Compresión venosa: **vena femoral no compresible**.
- Perfil A + TVP → TEP (**especificidad del 99 %**).
- Perfil A **sin** TVP **no** descarta el TEP.
- Multiórgano (pulmón, corazón y venas): sensibilidad del **90 %**.
- **Visual:** imagen real de TVP femoral no compresible (derecha).
- **Fuente:** Lichtenstein 2008; Bekgoz 2019; Nazerian 2014.
- **Notas:**
    - En urgencias, la sensibilidad del BLUE para el TEP cae al 46 % (Bekgoz 2019).
    - Variante opcional: líneas B **focales** con consolidación y pleura irregular son neumonía, no edema (Padrao 2025; Copetti 2008).

### 13 · Mensaje 2 — 0,5 min (diapositiva de mensaje)
- **«Perfil A: mira las piernas y el corazón»**.

### 14 · Caso 2: «Mañana se va de alta» — 1,5 min
- ICA en mejoría; «seco» a la auscultación.
- **Hasta el 41 %** de los «secos» tiene congestión ecográfica.
- Líneas B al alta: **HR 2,32** de reingreso o muerte.
- **ESC 2026:** descartar la congestión antes del alta (**I C**).
- Objetivo de la ESC con LUS: **< 5 líneas B**.
- **Visual:** diagrama `lus-8-zonas-congestion-residual.png` (derecha).
- **Fuente:** Rivas-Lasarte 2020; Suhardi 2025; Køber 2026; Gargani 2023.
- **Notas:**
    - Preguntar a la audiencia: «¿la dais de alta?».
    - La ESC 2026 incluye por primera vez la LUS entre las herramientas de descongestión al alta: óptimo < 5 líneas B (28 u 8 zonas), aceptable < 15 (28 zonas).
    - Con el protocolo de 8 zonas de la EACVI, la congestión residual es ≥ 1 zona positiva en cada hemitórax. Hay que decir siempre qué protocolo se usa.
    - El hallazgo cambia el plan de alta: diurético y revisión a 1–2 semanas.

### 15 · ¿Guiar el diurético por las líneas B? — 1,5 min
- **Visual (diapositiva de imagen):** diagrama `lus-forest-metaanalisis.png`.
- **Pie:** «Menos visitas urgentes, hospitalización discutida, mortalidad sin cambios».
- **Fuente:** Mhanna 2022; Al-Sagban 2026; Chotalia 2026; Bagheri 2026.
- **Notas:**
    - Los ensayos son sobre todo ambulatorios o tras el alta.
    - Durante el ingreso, los pilotos fueron negativos (BLUSHED-AHF, DMP-Plus), y la ESC 2026 guía el diurético por el sodio urinario (IIb B1), no por las líneas B.
    - Al-Sagban usa efectos fijos y tiene una carta crítica publicada.
    - Pronóstico no es beneficio. Ensayos en marcha: ICARUS y ABDOPOCUS-HF (España).

### 16 · Mensaje 3 — 0,5 min (diapositiva de mensaje)
- **«Número para seguir la evolución, y al alta»**.

---

## Bloque D · Integración y cierre (3,5 min)

### 17 · Algoritmo práctico — 1 min
- **Visual (diapositiva de imagen):** diagrama `lus-algoritmo-disnea.png`.
- **Fuente:** Qaseem 2021 (ACP); Gargani 2023; Lichtenstein 2008; Martindale 2016. Es una síntesis docente propia.
- **Notas:**
    - A quién: disnea aguda **con incertidumbre diagnóstica**. La ACP lo sugiere de forma condicional y con certeza baja.
    - Cuándo: lo antes posible, idealmente antes del diurético.
    - Aplicar el POCUS por sistema a toda disnea no acortó la estancia (Ovesen 2026). El beneficio es llegar antes al diagnóstico y al tratamiento correcto (Szabó 2023).

### 18 · Qué dicen las guías — 1 min
- **ESC 2026:** LUS en el algoritmo diagnóstico y al alta, **sin clase propia**.
- **ESC 2026:** descartar la congestión antes del alta, **I C**.
- **EACVI 2023:** LUS «apropiada»; protocolo de 8 zonas.
- **ACP 2021 · SCCM 2024:** condicional, certeza baja (GRADE).
- **SEMI 2025 · SEMI/SEC/S.E.N. 2024:** posicionamiento y escala de congestión.
- **Visual:** tabla sobria.
- **Fuente:** Køber 2026; Gargani 2023; Qaseem 2021; Díaz-Gómez 2025; Tung-Chen 2025; Llàcer 2024.
- **Notas:** la laguna: ninguna guía recomienda con clase guiar el diurético por las líneas B durante el ingreso. La ESC 2026 cambia la terminología a «IC descompensada».

### 19 · Errores frecuentes y cómo empezar — 1 min
- Líneas B **≠** IC: SDRA, neumonía, fibrosis, COVID-19.
- Una zona aislada no es edema.
- Sin líneas B no se descarta la IC (obesidad, IC derecha, EPOC).
- Sin deslizamiento ≠ neumotórax: busca el punto pulmón.
- **Empezar:** 5–20 exploraciones supervisadas.
- **Visual:** diagrama `lus-cardiogenico-vs-no.png` (derecha).
- **Fuente:** Copetti 2008; Chiem 2015; Johannessen 2023; Lichtenstein 2014; Russell 2020.
- **Notas:**
    - En la EPOC, la sensibilidad de la LUS para una IC concurrente es solo del 17 %.
    - Para seguir a un paciente, no cambies nada del protocolo.
    - La integración clínica es lo que más tarda en aprenderse. Documentar zonas, método y clips.

### 20 · Cierre: los tres mensajes — 0,5 min (diapositiva de mensaje)
- 1 · Patrón para diagnosticar.
- 2 · Perfil A: mira las piernas y el corazón.
- 3 · Número para seguir, y al alta.
- **Notas:** volver al caso 1: «con 5 minutos y un ecógrafo, este paciente habría recibido su diurético una hora antes» (el diagnóstico se adelanta unos 60 min según Szabó 2023).

### 21 · Bibliografía — fuera de tiempo
- Unas 12 referencias clave:
    - Gargani 2023, Demi 2023, Køber 2026 (ESC), Qaseem 2021 (ACP);
    - Lichtenstein 2008, Maw 2019, Martindale 2016, Pivetta 2019;
    - Szabó 2023, Al-Sagban 2026, Rivas-Lasarte 2020, Suhardi 2025.
- La bibliografía completa, en la [web del proyecto](../05-fuentes/index.md).

---

## Inventario de visuales

Hay más imágenes disponibles en [Recursos](../04-recursos/index.md) para sustituir o añadir: consolidación con broncograma, derrame pleural, modo M, punto pulmón, VI dilatado en PLAX y apical 4 cámaras, y VCI. Sus licencias están en [créditos](../04-recursos/creditos.md).

| Diapositiva | Archivo | Tipo | Estado |
|:--:|---|---|---|
| 4 | `diagramas/lus-espectro-aireacion.png` | Diagrama propio | ✅ |
| 5 | `img/lus-lineas-b.jpg` (Safai Zadeh 2024, CC BY 4.0) | Imagen con licencia | ✅ |
| 6 | `img/lus-lineas-a.jpg` (Foutzitzi 2025, CC BY 4.0; pediátrica) | Imagen con licencia | ✅ |
| 7 | `diagramas/lus-8-zonas.png` | Diagrama propio | ✅ |
| 8 | `diagramas/lus-arbol-blue.png` | Diagrama propio | ✅ |
| 9 | `diagramas/lus-rendimiento-lus-vs-rx.png` | Gráfico propio | ✅ |
| 10 | `diagramas/lus-probabilidad-bayes.png` | Gráfico propio | ✅ |
| 12 | `img/lus-tvp-femoral-no-compresible.png` (J. Heilman, CC BY-SA 4.0) | Imagen con licencia | ✅ |
| 14 | `diagramas/lus-8-zonas-congestion-residual.png` | Diagrama propio | ✅ |
| 15 | `diagramas/lus-forest-metaanalisis.png` | Gráfico propio | ✅ |
| 17 | `diagramas/lus-algoritmo-disnea.png` | Diagrama propio | ✅ |
| 19 | `diagramas/lus-cardiogenico-vs-no.png` | Diagrama propio | ✅ |
