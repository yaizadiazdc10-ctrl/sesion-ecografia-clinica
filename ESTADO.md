# Estado del proyecto

**Fase actual:** 3 — Investigación en curso (dos líneas en paralelo; primera entrega parcial publicada)

**Tema elegido:** decisión en dos pasos. El 2026-09-27 la usuaria eligió investigar **dos líneas combinadas**. Después de leerlas elegirá una (o una mezcla) para la charla:

- **Línea A (temas 3 + 4):** ecografía pulmonar y cardiaca en la disnea aguda y la insuficiencia cardiaca aguda. Del protocolo BLUE a la descongestión guiada por líneas B.
- **Línea B (temas 5 + 6):** el paciente en shock. Del tipo de shock con POCUS (RUSH y ecocardiografía) a la fluidoterapia guiada (VCI, medidas dinámicas y VExUS).

Alcance acordado: investigación **lo más extensa posible, solo texto**. Los recursos gráficos se buscarán cuando se elija la línea definitiva.

## Plan de investigación

Para cada línea (`docs/02-investigacion/a-disnea-ica/` y `docs/02-investigacion/b-shock-fluidos/`):

| # | Subtema | Preguntas |
|---|---------|-----------|
| 01 | Contexto y fundamento | Problema clínico, epidemiología, fisiopatología y bases físicas |
| 02 | Técnica y protocolos | Sondas, ventanas, secuencias (BLUE, 8/28 zonas, RUSH, VCI, VTI, VExUS), hallazgos |
| 03 | Precisión diagnóstica | Sensibilidad, especificidad y cocientes de probabilidad frente a la referencia y a la práctica habitual |
| 04 | Impacto clínico | Decisiones, tiempos y resultados; ensayos clínicos |
| 05 | Guías | Recomendaciones, clase y nivel, y diferencias entre sociedades |
| 06 | Integración en la práctica | Algoritmos: a quién, cuándo y cómo documentarlo |
| 07 | Limitaciones y errores | Falsos positivos y negativos, situaciones especiales, dependencia del operador |
| 08 | Formación y competencia | Curvas de aprendizaje, número de exploraciones, acreditación |
| 09 | Novedades y controversias | IA, estudios recientes, lagunas |
| 10 | Casos clínicos | 1–2 casos ilustrativos ficticios |


## Avance de la investigación (2026-09-27)

- **Línea A publicada:** 03 precisión diagnóstica, 04 impacto clínico, 08 formación, 09 novedades.
- **Línea A pendiente:** 01 contexto, 02 técnica, 05 guías, 06 práctica, 07 limitaciones, 10 casos.
- **Línea B publicada:** 01 contexto, 02 técnica, 04 impacto clínico, 07 limitaciones, 09 novedades.
- **Línea B pendiente:** 03 precisión diagnóstica, 05 guías, 06 práctica, 08 formación, 10 casos.
- Los subtemas pendientes aparecen como «En preparación» en la web.
- Al cerrar la sesión, varios agentes seguían escribiendo borradores en el scratchpad de la sesión (`inv/A`, `inv/B`), que es temporal. En la próxima sesión hay que **relanzar** los subtemas que falten con la skill `investigar-tema`: A-01, A-02, A-05, A-06, A-07, A-10, B-03, B-05, B-06, B-08 y B-10. Las páginas publicadas se reutilizan.
- Bibliografía: 410 referencias. Las nuevas se han comprobado con esummary de PubMed. `meyhoff2022` se ha unificado en `classic2022`, y `prager2023` se ha corregido a protocolo de estudio de cohortes.
- **Controversias destacadas** para decidir entre las líneas:
    - **Línea A:**
        - el ECA pragmático danés de 2026 (Ovesen) es negativo;
        - los metaanálisis de 2026 sobre el tratamiento guiado por líneas B discrepan en las hospitalizaciones y ninguno reduce la mortalidad;
        - los pilotos en fase aguda (BLUSHED-AHF, EPICC) son negativos.
    - **Línea B:**
        - SHoC-ED es negativo;
        - los metaanálisis de ecografía y mortalidad discrepan según la población;
        - CLASSIC, CLOVERS y ARISE FLUIDS son neutros;
        - VExUS solo tiene evidencia observacional.
- **Pendientes [POR VERIFICAR]** más relevantes: textos literales de SSC 2026, ESICM 2025 y ACEP 2023, y cifras de formación de SEMI y EACVI (ver cada página).

## Temas candidatos

Ver [docs/01-exploracion/index.md](docs/01-exploracion/index.md). La puntuación va sobre 30.

1. POCUS en la parada cardiaca (ERC/ILCOR 2025) — 26
2. Derrame pericárdico y taponamiento (ESC 2025) — 27
3. Disnea aguda: protocolo BLUE y abordaje multiórgano — 24
4. Líneas B en la insuficiencia cardiaca aguda — 26
5. Shock indiferenciado: RUSH y ecocardiografía como primera prueba — 22
6. Fluidos en el shock séptico: VCI, medidas dinámicas y VExUS — 24
7. TVP: ecografía de compresión en 2–3 puntos — 28
8. Cólico renal: hidronefrosis y cuándo evitar el TC — 26
9. Bloqueo PENG / fascia ilíaca en la fractura de cadera — 23
10. Ecografía gástrica y agonistas GLP-1 — 21

Recomendación de Claude: 7, 4 y 1. La decisión es de la usuaria. Hay otros 14 temas descartados en [otros-temas.md](docs/01-exploracion/otros-temas.md).

## Próximos pasos

- [x] Crear las skills del proyecto: `explorar-temas`, `investigar-tema`, `sintetizar-presentacion`
- [x] Lanzar la exploración de temas POCUS (fase 1, skill `explorar-temas`)
- [ ] Revisar la lista de temas en la web y elegir uno (fase 2). Se pueden combinar o acotar
- [ ] Registrar la decisión en este archivo y en una sección `## Tema elegido` al inicio de `docs/01-exploracion/index.md`
- [ ] Opcional: indicar la audiencia concreta (servicio o nivel), para ajustar la relevancia
- [ ] Pendientes marcados [POR VERIFICAR] en las fichas, que se resolverán en la fase 3 para el tema elegido:
  - texto literal de guías de pago (ESICM 2025, AAGBI, NICE, AHA 2025);
  - licencias de algunas imágenes de Commons

## Bitácora de sesiones

| Fecha | Resumen |
|-------|---------|
| 2026-09-27 | Creación del repositorio, harness (CLAUDE.md), web MkDocs, configuración de Netlify y hook de commit + push al cerrar la sesión. |
| 2026-09-27 | Skills `explorar-temas`, `investigar-tema` y `sintetizar-presentacion`. Generador de PPTX (`scripts/build_pptx.py`), estilo de diagramas y exportación a PDF con PowerPoint, probados con una presentación de prueba. |
| 2026-09-27 | Rediseño de la web: paleta rosa oro, tipografía Instrument Serif/Sans, cabecera clara translúcida, portada con hero ecográfico y recorrido por fases, tarjetas de secciones. Eliminados el enlace a GitHub y el selector de modo oscuro (sigue al sistema). |
| 2026-09-27 | Estilo sobrio para la presentación y los diagramas (blanco y negro + acento morado, tipografía Aptos), documentado en las skills y en CLAUDE.md. El rosa oro queda solo para la web. |
| 2026-09-27 | **Fase 1 completada.** Barrido en paralelo de 7 áreas POCUS. Resultado: 10 temas candidatos, cada uno con su ficha (guías, evidencia, cifras, controversias, material visual, estructura de la charla y comentario), una tabla comparativa, una guía de elección según la audiencia y una recomendación. Además, 14 temas descartados en fichas breves. Bibliografía de 119 referencias verificadas en PubMed. Portada en fase 2. |
| 2026-09-27 | **Fase 3 (parcial).** Decisión: investigar dos líneas combinadas, A (temas 3 + 4) y B (temas 5 + 6), solo texto. Se lanzaron 8 agentes en paralelo. Se publican 9 de los 20 subtemas (4 de la línea A y 5 de la línea B), con índices y navegación. La bibliografía pasa de 119 a 410 referencias verificadas. El resto de subtemas quedan «En preparación» y hay que relanzarlos en la próxima sesión. |
