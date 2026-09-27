---
name: investigar-tema
description: Fases 3 y 4 del proyecto. Investigación en profundidad del tema POCUS elegido (PubMed, guías, sociedades científicas, revisiones sistemáticas y estudios clave), con toda la información documentada y referenciada en la web, más la búsqueda y descarga de imágenes e infografías con licencia libre. Usar cuando haya un tema elegido en ESTADO.md y se pida investigar, ampliar información o buscar recursos gráficos.
---

# Investigar el tema elegido

Objetivo: reunir **la mayor cantidad posible de información verificada**, con fuentes y estudios, sobre el tema elegido, y dejarla organizada en la web. También reunir material gráfico reutilizable. Esta fase alimenta la síntesis: aquí se documenta **todo**; recortar para 20 minutos se hace después.

**Precondición:** `ESTADO.md` tiene un **tema elegido**. Si no, para y usa la skill `explorar-temas` o pregunta al usuario.

Lee antes [CLAUDE.md](../../../CLAUDE.md) (reglas de evidencia y de imágenes), [ESTADO.md](../../../ESTADO.md) y la ficha del tema en `docs/01-exploracion/index.md`.

## 1. Plan de subtemas

Divide el tema en subtemas (ajústalos al tema). Plantilla:

| # | Subtema | Preguntas que responde |
|---|---------|------------------------|
| 01 | Contexto y fundamento | Problema clínico, epidemiología, por qué la ecografía aporta, bases físicas o fisiopatológicas imprescindibles |
| 02 | Técnica y protocolo | Sonda, preset, ventanas, secuencia del protocolo, hallazgos normales y patológicos, cuantificación |
| 03 | Precisión diagnóstica | Sensibilidad, especificidad, LR+/LR−, comparación con la prueba de referencia y con la práctica habitual (Rx, clínica, TC) |
| 04 | Impacto clínico | Efecto en decisiones, tiempos, resultados en el paciente, ensayos clínicos |
| 05 | Qué dicen las guías | Recomendaciones de cada guía o consenso, clase y nivel de evidencia, y diferencias entre sociedades |
| 06 | Integración en la práctica | Algoritmos de decisión, a quién, cuándo, cómo documentarlo |
| 07 | Limitaciones y errores | Falsos positivos y negativos, artefactos, situaciones especiales, dependencia del operador |
| 08 | Formación y competencia | Curva de aprendizaje, nº de exploraciones recomendadas, programas de acreditación |
| 09 | Novedades y controversias | Estudios recientes, IA, áreas de incertidumbre, líneas de investigación |
| 10 | Casos clínicos | 1–2 casos ilustrativos que puedan abrir la charla (ficticios o de fuentes open access, sin datos identificables) |

Escribe el plan en ESTADO.md antes de empezar.

## 2. Investigación (en paralelo)

Lanza **subagentes en paralelo** (Agent, `general-purpose`), agrupando subtemas afines (3–5 agentes). Cada prompt debe incluir: el tema exacto, los subtemas y preguntas asignados, las reglas de evidencia de CLAUDE.md y este bloque:

> Fuentes: PubMed vía E-utilities (esearch → esummary → efetch para abstracts), Europe PMC, Cochrane Library, webs de las sociedades (ACEP, ESC, ERC, ESICM, EFSUMB, WINFOCUS, ASE, SEMES, SEMI, semFYC…) y artículos open access en PMC. Prioriza guías vigentes y RS/MA de los últimos 5 años, e incluye estudios fundacionales aunque sean anteriores (señálalo). Para cada dato: cifra exacta + cita con PMID/DOI **que hayas verificado en PubMed o en la web de la revista**. Nunca inventes una referencia ni una cifra; si no encuentras el dato, dilo. Devuelve Markdown en español con: hallazgos por pregunta, tabla de estudios clave (autor/año, diseño, n, población, resultado principal, PMID/DOI) y lista de referencias completa. Señala las controversias y la calidad de la evidencia.

Búsquedas útiles en PubMed (añade `AND 2020:2026[dp]` para acotar a lo reciente):

```bash
curl -sg "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=30&sort=relevance&term=<términos>+AND+(systematic+review[pt]+OR+meta-analysis[pt])"
curl -sg "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=<pmid1>,<pmid2>"
curl -sg "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&rettype=abstract&retmode=text&id=<pmid>"
```

## 3. Verificación

Antes de escribir nada en la web:

- Comprueba con `esummary` **todos** los PMID citados (título, año y revista deben coincidir). Para los DOI sin PMID, comprueba que `https://doi.org/<doi>` resuelve.
- Contrasta las cifras clave (S/E, LR, n) con el abstract (`efetch`).
- Elimina o marca `[POR VERIFICAR]` todo lo que no cuadre, y resuelve las contradicciones entre agentes.

## 4. Escribir en la web

- Un archivo por subtema: `docs/02-investigacion/NN-slug.md` (p. ej. `03-precision-diagnostica.md`). Usa encabezados claros, tablas de estudios, admonitions (`!!! tip "Perla clínica"`, `!!! warning "Error frecuente"`) y citas enlazadas a la bibliografía.
- `docs/02-investigacion/index.md`: resumen ejecutivo del tema (10–15 líneas), índice de subtemas y una **tabla de evidencia** con los estudios clave.
- Diagramas simples (algoritmos, flujos) pueden ir como bloques ` ```mermaid ` en la web. Los que irán en la presentación se generan como PNG en la fase de síntesis, con el estilo sobrio de la presentación (blanco y negro + acento morado; ver la skill `sintetizar-presentacion`), no con el rosa oro de la web.
- `docs/05-fuentes/index.md`: todas las referencias con el formato de CLAUDE.md, clasificadas por tipo.
- Añade cada página nueva al `nav` de `mkdocs.yml`.

## 5. Recursos gráficos

Busca imágenes para la presentación: planos ecográficos normales y patológicos, colocación de la sonda, infografías de protocolos y algoritmos de guías.

- **Wikimedia Commons**, con su API:
  ```bash
  curl -s "https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=20&gsrsearch=<términos>+ultrasound&prop=imageinfo&iiprop=url|extmetadata"
  ```
  Toma la licencia (`LicenseShortName`), el autor (`Artist`) y la URL de `extmetadata`.
- **PMC open access**: figuras de artículos con licencia CC BY o CC BY-NC. Comprueba la licencia en la página del artículo.
- **Radiopaedia**: casos con licencia CC BY-NC-SA, válidos para uso docente no comercial. Cita el caso y el autor.
- Las infografías de sociedades se usan **solo** si su licencia lo permite. Si no, enlázalas en la web sin descargarlas.

Por cada imagen descargada:

1. Guárdala en `docs/assets/img/<tema>-<descripcion>.<ext>` (con `curl -L -o`, usando la URL original a resolución suficiente).
2. Comprueba que es una imagen válida (`file <ruta>`) y mírala con Read para confirmar que muestra lo esperado.
3. Añade una fila en `docs/04-recursos/creditos.md`: archivo, descripción, autor, URL de origen y licencia.
4. Añádela a la galería de `docs/04-recursos/index.md`, agrupada por categoría, con pie descriptivo: `![desc](../assets/img/archivo.png){ loading=lazy }`.

Objetivo orientativo: 10–20 imágenes útiles, sin datos identificables de pacientes.

## 6. Cerrar

1. `.venv/bin/mkdocs build --strict` debe pasar.
2. Actualiza `ESTADO.md`: fase 5 (lista para síntesis), resumen de lo investigado, lagunas pendientes y bitácora.
3. Commit y push (`investigacion: <resumen>`).
4. Informa al usuario: subtemas cubiertos, nº de referencias verificadas, nº de imágenes y cualquier laguna o controversia relevante.
