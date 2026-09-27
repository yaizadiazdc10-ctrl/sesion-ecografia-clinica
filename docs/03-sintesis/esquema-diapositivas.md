# Esquema de diapositivas

Guion de la presentación diapositiva a diapositiva, pensado para **repartir** la preparación del PowerPoint. Está dividido en **4 bloques independientes**, cada uno con su tiempo, contenido, visual, fuente y notas del orador.

!!! info "Cómo usar este esquema"
    - **Una idea por diapositiva:** ≤ 6 puntos por diapositiva y ≤ 12 palabras por punto. Cifras grandes en lugar de párrafos.
    - **Estilo del PPT:** sobrio, en blanco y negro con un único acento morado (`#5B3F8C`). Tipografía Aptos. Sin degradados ni iconos decorativos. El rosa oro es solo de la web.
    - **Las fuentes van en el pie** de cada diapositiva. Lo que se dice va en las **notas del orador**.
    - **«Visual»** indica qué imagen o diagrama hace falta. Las imágenes se buscarán con licencia compatible en la fase de recursos. Los diagramas propios se generarán con scripts.
    - Al final, todo se unifica en `presentacion/diapositivas.yaml` para construir el `.pptx` con el script del proyecto.

## Reparto por bloques

| Bloque | Diapositivas | Tiempo | Tema | Qué hay que preparar |
|---|:--:|:--:|---|---|
| **A** | 1–5 | 5 min | Apertura y fundamento | Caso 1, datos del problema, física de las líneas A y B |
| **B** | 6–11 | 7 min | Técnica y diagnóstico | Ajustes, 8 zonas, BLUE, precisión, resolución del caso 1 |
| **C** | 12–16 | 5,5 min | Diferencial y descongestión | Caso 3, caso 2, evidencia del tratamiento guiado |
| **D** | 17–20 | 2,5 min | Guías, errores y cierre | Tabla de guías, errores frecuentes, mensajes, bibliografía |

---

## Bloque A · Apertura y fundamento (5 min)

### 1 · Portada — 0,5 min
- **Título:** Ecografía pulmonar en la disnea aguda y la insuficiencia cardiaca aguda.
- **Subtítulo:** Del protocolo BLUE a la descongestión guiada por líneas B.
- Autora, servicio y fecha.
- **Visual:** ninguno, o una imagen ecográfica de líneas B, sobria.
- **Notas:** presentación breve y objetivo de la sesión: «que mañana podáis usar el ecógrafo ante un paciente con disnea».

### 2 · Caso 1: «La radiografía no lo aclara» — 1,5 min
- Varón de 74 años, HTA, DM, EPOC leve. Disnea de 4 días, ortopnea.
- SpO₂ 88 %, FR 28, sibilancias y crepitantes basales.
- Rx AP en decúbito: «¿redistribución o infiltrado basal?».
- NT-proBNP pendiente (60–90 min).
- **Pregunta a mano alzada:** ¿probabilidad de ICA < 25 %, 25–75 % o > 75 %?
- **Visual:** radiografía dudosa (imagen por buscar) o tabla de constantes.
- **Fuente:** caso ficticio docente ([10 · Casos](../02-investigacion/a-disnea-ica/10-casos.md#caso-1)).
- **Notas:** no dar la respuesta; se retoma en la diapositiva 10. Mencionar que el residente plantea salbutamol y antibiótico «por si acaso».

### 3 · El problema — 1 min
- Disnea aguda: **≈ 5 %** de las urgencias; la IC es la 2.ª causa.
- Tras un ingreso por ICA: **hasta el 45 %** reingresa o muere en un año.
- Ausencia de crepitantes: LR− de solo **0,51**.
- Radiografía normal en **1 de cada 5** ICA.
- **Visual:** tres cifras grandes.
- **Fuente:** Kelly 2017; Gargani 2023; Wang 2005; Collins 2006.
- **Notas:** la clínica y la Rx fallan justo cuando más las necesitamos. Si el tratamiento inicial es inapropiado, la mortalidad se duplica en el anciano (25 % frente a 11 %; Ray 2006).

### 4 · Del aire al agua: líneas A y líneas B — 1 min
- El pulmón aireado solo produce **artefactos**.
- **Líneas A:** reverberación de la pleura; pulmón aireado.
- **Líneas B:** septos engrosados y agua extravascular.
- Espectro: líneas A → líneas B → confluentes → consolidación.
- **Visual:** diagrama propio del espectro de aireación, o dos clips (líneas A y líneas B).
- **Fuente:** Demi 2023; Lichtenstein 1997.
- **Notas:** explicar en 30 s por qué el agua cambia el artefacto. Las líneas B reflejan el agua pulmonar mejor que la presión de enclavamiento.

### 5 · Qué es (y qué no es) una línea B — 1 min
- Nace de la pleura y llega al fondo sin atenuarse.
- Se mueve con el deslizamiento y **borra las líneas A**.
- **≥ 3 por espacio intercostal** = zona positiva.
- Cardiogénico: bilateral, homogéneo, **pleura fina**.
- No cardiogénico: parcheado, **pleura irregular**, consolidaciones.
- **Visual:** clip de línea B anotado, con una comparación de pleura fina frente a irregular.
- **Fuente:** Volpicelli 2012; Gargani 2023; Copetti 2008.
- **Notas:** adelantar que las líneas B no son sinónimo de IC. Diferenciar las líneas Z, que no llegan al fondo.

---

## Bloque B · Técnica y diagnóstico (7 min)

### 6 · Configura el equipo para el pulmón — 1 min
- Preset pulmonar o abdominal.
- **Sin armónicos, sin filtros, sin compuesto**.
- Foco en la pleura, índice mecánico bajo.
- Sonda: convexa o microconvexa (versátil); lineal para la pleura.
- Para seguir a un paciente: **misma sonda, preset y postura**.
- **Visual:** foto del panel del ecógrafo o una comparación con y sin armónicos (por buscar).
- **Fuente:** Demi 2023; Gargani 2023; Platz 2015.
- **Notas:** es el error técnico más frecuente; los filtros «limpian» precisamente las líneas B.

### 7 · El protocolo de 8 zonas — 1,5 min
- 4 zonas por hemitórax: anterior y lateral, superior e inferior.
- Contar en el peor punto de cada zona; clips de unos 6 s.
- Confluentes: % de pantalla dividido entre 10.
- **Edema:** ≥ 3 líneas B por zona en **≥ 2 zonas por lado**, bilateral.
- **Visual:** diagrama propio del tórax con las 8 zonas y el criterio de positividad.
- **Fuente:** Gargani 2023 (EACVI); Buessler 2020.
- **Notas:** es el protocolo que recomienda la EACVI. Aclarar que 4, 8 y 28 zonas tienen umbrales distintos y no intercambiables.

### 8 · El protocolo BLUE en un vistazo — 1,5 min
- 3 puntos por hemitórax, más el punto PLAPS.
- **Perfil B:** edema hemodinámico.
- **Perfil A:** buscar TVP (TEP) o pensar en EPOC/asma.
- **Perfil A′ + punto pulmón:** neumotórax.
- **Perfil A/B, C o PLAPS:** neumonía.
- **Visual:** árbol de decisión BLUE como diagrama propio (sobrio, rama clave en morado).
- **Fuente:** Lichtenstein 2008; Lichtenstein 2014.
- **Notas:** acertó el 90,5 % en su estudio original de UCI. Anticipar que en urgencias rinde peor para el TEP (diapositiva 12).

### 9 · ¿Cuánto rinde? LUS frente a Rx frente a péptidos — 1,5 min
- **Ecografía pulmonar:** sensibilidad del 88–92 %, especificidad del 90–92 % · LR+ 7,4 · LR− 0,16.
- **Radiografía:** sensibilidad del 73–77 % · LR+ 4,8 · mala para descartar.
- **NT-proBNP < 300 pg/ml:** LR− 0,09, para descartar.
- LUS + clínica mejora más el diagnóstico que Rx + NT-proBNP (AUC 0,95 frente a 0,87).
- **Visual:** tabla sobria o gráfico de barras de sensibilidad (LUS frente a Rx), con la LUS en morado.
- **Fuente:** Maw 2019; Chiu 2022; Martindale 2016; Pivetta 2019.
- **Notas:** el péptido sirve para descartar y la ecografía confirma y descarta. Pulmón y corazón a la vez suben la especificidad al 96 % (Popat 2026).

### 10 · Resolución del caso 1 — 1 min
- **Pulmón:** patrón B en 7 de 8 zonas, pleura fina, derrame bilateral.
- **Corazón:** FEVI visual muy reducida.
- Probabilidad: **40 % → ≈ 83 %** con el patrón B.
- **Decisión:** diurético i.v. sin esperar al péptido; sin antibiótico.
- **Visual:** clips del caso (patrón B y FoCUS), o un diagrama de probabilidad pretest y postest.
- **Fuente:** Martindale 2016; Popat 2026; McDonagh 2021 (diurético en la ICA con sobrecarga, I C).
- **Notas:** recuperar la votación de la diapositiva 2. Las sibilancias eran «asma cardial». Pedir después una ecocardiografía reglada. El cálculo de Bayes es propio.

### 11 · Mensaje 1 — 0,5 min (diapositiva de mensaje, fondo negro)
- **«Patrón para diagnosticar»:** líneas B difusas y bilaterales + FoCUS confirman la ICA mejor que la Rx.
- **Notas:** pausa y silencio.

---

## Bloque C · Diferencial y descongestión (5,5 min)

### 12 · Caso 3: pulmón normal, paciente que no respira bien — 1,5 min
- Disnea aguda con **perfil A** bilateral.
- Siguiente paso: **compresión venosa** (vena femoral no compresible) y VD dilatado.
- Perfil A + TVP → TEP (**especificidad del 99 %**).
- Perfil A **sin** TVP **no** descarta el TEP (BLUE en urgencias: sensibilidad del 46 %).
- Solo el enfoque multiórgano llega a una **sensibilidad del 90 %**.
- **Visual:** perfil A frente a vena no compresible (clips por buscar).
- **Fuente:** Lichtenstein 2008; Bekgoz 2019; Nazerian 2014.
- **Notas:** variante opcional: líneas B **focales** con consolidación y pleura irregular son neumonía (Padrao 2025; Copetti 2008).

### 13 · Mensaje 2 — 0,5 min (diapositiva de mensaje)
- **«Perfil A: mira las piernas y el corazón»**.

### 14 · Caso 2: «Mañana se va de alta» — 1,5 min
- ICA en mejoría; «seco» a la auscultación.
- **Líneas B residuales** en ambos hemitórax (8 zonas: ≥ 1 zona positiva por lado).
- **Hasta el 41 %** de los «secos» tiene congestión ecográfica.
- Líneas B al alta: **HR 2,32** de reingreso o muerte.
- ESC: descartar la congestión antes del alta (**I C**) y revisar a 1–2 semanas.
- **Visual:** tabla de ingreso frente a prealta, o un diagrama de las 8 zonas con las zonas positivas marcadas.
- **Fuente:** Rivas-Lasarte 2020; Suhardi 2025; McDonagh 2021; Gargani 2023.
- **Notas:** preguntar a la audiencia: «¿la dais de alta?». El hallazgo cambia el plan de alta (diurético y revisión precoz).

### 15 · ¿Guiar el diurético por las líneas B? — 1,5 min
- **Consulta y tras el alta:** visitas urgentes por IC **RR 0,31–0,38**.
- Hospitalización por IC: resultados **discordantes** entre metaanálisis.
- Mortalidad: **sin efecto**.
- **Durante el ingreso:** pilotos negativos (BLUSHED-AHF).
- **Pronóstico ≠ beneficio:** faltan ECA de calidad.
- **Visual:** *forest plot* simplificado de los metaanálisis de 2026 (diagrama propio).
- **Fuente:** Al-Sagban 2026; Chotalia 2026; Bagheri 2026; Mhanna 2022; Pang 2021.
- **Notas:** Al-Sagban usa efectos fijos y tiene una carta crítica publicada. Ensayos en marcha: ICARUS y ABDOPOCUS-HF (España).

### 16 · Mensaje 3 — 0,5 min (diapositiva de mensaje)
- **«Número para seguir la evolución, y al alta»**.

---

## Bloque D · Guías, errores y cierre (2,5 min)

### 17 · Qué dicen las guías — 1 min
- **ESC 2021:** LUS «se puede considerar», sin clase. Congestión antes del alta: **I C**.
- **EACVI 2023:** LUS «apropiada»; protocolo de 8 zonas.
- **ACP 2021 · SCCM 2024:** condicional, certeza baja (GRADE).
- **SEMI 2025 · SEMI/SEC/S.E.N. 2024:** posicionamiento y escala de congestión.
- **Laguna:** guiar el diurético durante el ingreso no tiene recomendación.
- **Visual:** tabla sobria de sociedades.
- **Fuente:** McDonagh 2021; Gargani 2023; Qaseem 2021; Díaz-Gómez 2025; Tung-Chen 2025; Llàcer 2024.
- **Notas:** **verificar antes la guía ESC 2026 de IC**, que puede cambiar esta diapositiva.

### 18 · Errores frecuentes y cómo empezar mañana — 1 min
- Líneas B **≠** IC: SDRA, neumonía, fibrosis, COVID-19.
- Una zona aislada no es edema.
- Sin líneas B no se descarta la IC (obesidad, IC derecha, EPOC).
- Sin deslizamiento no hay por qué pensar en neumotórax: busca el punto pulmón.
- **Empezar:** 5–20 exploraciones supervisadas para las líneas B; documentar zonas y clips.
- **Visual:** lista de comprobación a dos columnas («errores» y «cómo empezar»).
- **Fuente:** Copetti 2008; Chiem 2015; Johannessen 2023; Lichtenstein 2014; Russell 2020.
- **Notas:** la integración clínica es lo que más tarda. Mencionar la formación de la SEMI si hay residentes.

### 19 · Cierre: los tres mensajes — 0,5 min (diapositiva de mensaje)
- 1 · Patrón para diagnosticar.
- 2 · Perfil A: mira las piernas y el corazón.
- 3 · Número para seguir, y al alta.
- **Notas:** volver al caso 1: «con 5 minutos y un ecógrafo, este paciente habría recibido su diurético una hora antes».

### 20 · Bibliografía — fuera de tiempo
- Unas 10–12 referencias clave:
    - Gargani 2023, Demi 2023, McDonagh 2021, Qaseem 2021;
    - Lichtenstein 2008, Maw 2019, Martindale 2016, Pivetta 2019;
    - Szabó 2023, Al-Sagban 2026, Rivas-Lasarte 2020, Suhardi 2025.
- La bibliografía completa, en la [web del proyecto](../05-fuentes/index.md).

---

## Material visual que habrá que conseguir

| Diapositiva | Visual | Tipo |
|:--:|---|---|
| 4 | Espectro de aireación: líneas A → B → confluentes → consolidación | Diagrama propio |
| 5 | Clip o imagen de línea B anotada; pleura fina frente a irregular | Imagen con licencia |
| 7 | Tórax con las 8 zonas y el criterio de positividad | Diagrama propio |
| 8 | Árbol BLUE | Diagrama propio (existe un original CC0 en Commons, como referencia) |
| 9 | Sensibilidad de LUS frente a Rx | Gráfico propio |
| 10 | Patrón B y FoCUS con FEVI deprimida | Imagen con licencia |
| 12 | Perfil A y vena no compresible | Imagen con licencia (hay TVP en CC0 en Commons) |
| 14 | 8 zonas con congestión residual | Diagrama propio (reutiliza el de la diapositiva 7) |
| 15 | *Forest plot* simplificado de los metaanálisis de 2026 | Gráfico propio |
