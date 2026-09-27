# Estado del proyecto

**Fase actual:** 3 — Investigación en curso (dos líneas en paralelo)

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
