# Estado del proyecto

**Fase actual:** 2 — Esperando la elección del tema

**Tema elegido:** _pendiente_

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
