# Estado del proyecto

**Fase actual:** 6 — Presentación definitiva 1.1 (tema «Dividendo») generada, revisada en PDF y publicada. Pendiente: retoques de la usuaria

**Tema elegido:** **ecografía pulmonar y cardiaca en la disnea aguda y la insuficiencia cardiaca aguda. Del protocolo BLUE a la descongestión guiada por líneas B** (línea A, que combina los temas 3 y 4).

- Se investigaron dos líneas y, tras leer la primera entrega, la usuaria eligió la A.
- La línea B (shock y fluidos) se descartó y se retiró de la web; queda en los commits `b1af0df` y `7c35766`.

## Investigación (completa)

`docs/02-investigacion/a-disnea-ica/` tiene los 10 subtemas publicados:

1. contexto;
2. técnica;
3. precisión diagnóstica;
4. impacto clínico;
5. guías;
6. práctica;
7. limitaciones;
8. formación;
9. novedades;
10. casos clínicos.

La bibliografía tiene 348 referencias citadas, verificadas en PubMed. Solo texto: aún no hay recursos gráficos.

## Síntesis preliminar

`docs/03-sintesis/` contiene:

- **`index.md`:** los 3 mensajes clave, la estructura de 20 min en 4 bloques, lo pendiente de verificar y las preguntas previsibles.
- **`resumen-ampliado.md`:** lectura de preparación de 11 apartados con cifras referenciadas.
- **`esquema-diapositivas.md`:** 20 diapositivas repartidas en 4 bloques (A 1–5, B 6–11, C 12–16, D 17–20), con el contenido, el visual, la fuente, el tiempo y las notas de cada una, más la lista de visuales necesarios.

Los mensajes clave son:

1. Patrón para diagnosticar.
2. Perfil A: mira las piernas y el corazón.
3. Número para seguir la evolución, y al alta.

## Presentación (versión 1.0, 2026-09-28)

- **Archivos:**
    - `presentacion/diapositivas.yaml` es el guion;
    - `presentacion/sesion-clinica.pptx` es el PowerPoint, también descargable desde la web en `docs/assets/presentacion/`.
- **Contenido:** 21 diapositivas en 20 minutos, en 4 bloques (A 1–5, B 6–11, C 12–16, D 17–21), con notas del orador y la fuente en el pie.
- **Diagramas propios:** 10, en `docs/assets/diagramas/lus-*.png`, generados por `scripts/diagramas/*.py` con el estilo sobrio de la presentación:
    - espectro de aireación;
    - 8 zonas (mapa, edema y congestión residual);
    - árbol BLUE;
    - rendimiento de la ecografía frente a la Rx;
    - probabilidad pre y postest;
    - *forest plot* de los metaanálisis;
    - algoritmo práctico;
    - cardiogénico frente a no cardiogénico.
- **Imágenes con licencia:** 17 en `docs/assets/img/lus-*`, registradas en `creditos.md`. La presentación usa 3: líneas B, líneas A y TVP no compresible.
- **ESC 2026 verificada** con las diapositivas oficiales de la ESC:
    - la LUS aparece en el algoritmo diagnóstico y al alta (< 5 líneas B), sin clase propia;
    - descartar la congestión antes del alta sigue siendo I C;
    - el diurético se guía por el sodio urinario (IIb B1).

    El mensaje 3 y la diapositiva de guías ya están actualizados.

## Próximos pasos

- [x] Exportar a PDF y revisar las diapositivas visualmente (hecho el 2026-09-28; el PDF está publicado en la web). Nota anterior: PowerPoint devuelve el error −9074 al abrir por AppleScript, probablemente por un diálogo o un permiso pendiente. Cuando se resuelva: `scripts/exportar_pdf.sh presentacion/sesion-clinica.pptx` → revisar → copiar el PDF a `docs/assets/presentacion/` y enlazarlo desde la síntesis
- [ ] Retoques de la usuaria sobre el `.pptx`
- [ ] Opcional: sustituir las imágenes pediátricas (líneas A) por imágenes de adulto
- [ ] Opcional: descargar a más resolución las imágenes de Commons, que están a unos 500 px por un bloqueo 429
- [ ] Pendientes de lectura completa: texto completo de la ESC 2026, enunciados de Volpicelli 2026, SEMI 2025 y la carta de Kumar 2026

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
| 2026-09-27 | **Elección definitiva: línea A.** Línea B descartada y retirada de la web. Se completan con 4 agentes los 6 subtemas pendientes de la línea A (01, 02, 05, 06, 07 y 10) y se verifican 258 referencias nuevas; la bibliografía queda en 348. **Síntesis preliminar:** 3 mensajes clave, resumen ampliado y esquema de 20 diapositivas en 4 bloques para repartir. |
| 2026-09-28 | **Presentación definitiva 1.0.** Síntesis revisada (ESC 2026 verificada con las diapositivas oficiales; mensaje 3 y guías actualizados). Esquema ampliado a 21 diapositivas con el algoritmo práctico. 10 diagramas propios con scripts y 17 imágenes con licencia libre (créditos y galería en Recursos). PPTX generado y publicado para descarga; exportación a PDF pendiente porque PowerPoint está bloqueado. |
| 2026-09-28 | **Presentación 1.1, tema «Dividendo».** A petición de la usuaria, el PPTX pasa al tema «Dividendo» de PowerPoint. La plantilla se genera desde `Dividend.thmx` con `scripts/plantilla_desde_thmx.py`, y `build_pptx.py` gana un modo de plantilla que usa los diseños del tema. Los diagramas tienen una variante granate en `diagramas/dividendo/`. Se mantienen todo el contenido, los recursos y las notas. PowerPoint vuelve a exportar: el PDF se ha revisado y está publicado en la web junto al PPTX. |
