---
name: explorar-temas
description: Fase 1 del proyecto. Investigación exploratoria de temas de ecografía a pie de cama (POCUS) con respaldo en guías y protocolos vigentes, para generar una lista comparativa de candidatos que el usuario revisa y de la que elige el tema de la sesión clínica. Usar cuando se pida explorar, buscar o proponer temas, o cuando ESTADO.md indique fase 0/1.
---

# Explorar temas POCUS

Objetivo: entregar una **lista revisable de 8–12 temas POCUS candidatos**, cada uno justificado con guías o consensos vigentes, para que el usuario elija uno. **Tú no eliges el tema**: propones, comparas y, como mucho, recomiendas.

Lee antes [CLAUDE.md](../../../CLAUDE.md) (reglas de evidencia) y [ESTADO.md](../../../ESTADO.md). Si el usuario ha dado preferencias (servicio, audiencia, nivel, temas a evitar), respétalas y anótalas en ESTADO.md.

## 1. Barrido por áreas (en paralelo)

Lanza **subagentes en paralelo** (Agent, tipo `general-purpose`), uno por área. Áreas de partida (ajusta según las preferencias del usuario):

1. Cardiaca y hemodinámica (FoCUS, función VI/VD, derrame pericárdico, ecografía en parada cardiaca, VExUS/congestión venosa)
2. Pulmonar y pleural (líneas B, neumotórax, derrame, consolidación, protocolo BLUE, disnea aguda)
3. Shock y protocolos integrados (RUSH, FAST/eFAST, abordaje del paciente crítico o hipotenso)
4. Abdominal y renal (hidronefrosis, retención urinaria, vesícula, aorta abdominal, líquido libre)
5. Vascular (TVP de 2–3 puntos, accesos vasculares ecoguiados, valoración de volemia/VCI)
6. Procedimientos ecoguiados (toracocentesis, paracentesis, bloqueos nerviosos, punción lumbar)
7. Otros de interés emergente (ecografía gástrica prequirúrgica, nervio óptico/HTIC, musculoesquelético, POCUS en atención primaria)

Prompt para cada subagente (adáptalo al área):

> Investiga el estado actual del uso de POCUS en <área> para una sesión clínica de 20 minutos dirigida a médicos. Busca con WebSearch/WebFetch y PubMed (E-utilities, ver abajo) **guías, consensos y declaraciones de sociedades científicas de los últimos ~5 años** (ACEP, ESC, ERC, ESICM, EFSUMB, WINFOCUS, ASE, SEMES, SEMI, semFYC, SEMERGEN…) y revisiones sistemáticas/metaanálisis recientes. Devuelve 2–4 temas concretos y bien acotados (no "ecografía pulmonar" sino "ecografía pulmonar en la disnea aguda: protocolo BLUE y líneas B"). Para cada tema: (a) pregunta clínica que responde; (b) guías/consensos que lo respaldan con organismo, año, recomendación y nivel si existe, y URL; (c) 1–3 revisiones sistemáticas o estudios clave con PMID o DOI **verificados** (solo referencias que hayas visto en PubMed o en la web de la revista; nunca inventes); (d) cifras clave de rendimiento diagnóstico si existen; (e) novedad o controversia reciente; (f) disponibilidad de imágenes o infografías con licencia libre (Wikimedia Commons, artículos open access de PMC con CC BY, Radiopaedia). Responde en español, en Markdown estructurado.

### Búsqueda y verificación en PubMed (E-utilities)

```bash
# Buscar (devuelve PMIDs); filtra por fecha y tipo de publicación
curl -sg "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=20&sort=relevance&term=point-of-care+ultrasound+AND+(guideline[pt]+OR+systematic+review[pt]+OR+meta-analysis[pt])+AND+2021:2026[dp]"
# Verificar un PMID concreto: título, revista, año, DOI
curl -sg "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=12345678"
# Resumen (abstract)
curl -sg "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&rettype=abstract&retmode=text&id=12345678"
```

Espacia las llamadas (≤3 por segundo). Europe PMC (`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json`) sirve de alternativa y señala si el texto completo es open access.

## 2. Consolidar y verificar

- Une los resultados, elimina duplicados y solapamientos y deja entre **8 y 12 temas**.
- **Verifica tú mismo** con `esummary` al menos las referencias que sustentan cada tema. Si una no existe o no coincide con lo descrito, elimínala o márcala `[POR VERIFICAR]`.
- Puntúa cada tema de 1 a 5 en estos criterios:
  - **Respaldo en guías:** cuántas guías o consensos lo respaldan, lo recientes que son y la fuerza de sus recomendaciones.
  - **Relevancia clínica:** frecuencia e impacto en decisiones en la práctica habitual.
  - **Actualidad:** novedades o cambios de guías recientes que justifiquen presentarlo ahora.
  - **Viabilidad en 20 minutos:** que sea lo bastante acotado para contarlo bien.
  - **Material visual:** disponibilidad de imágenes, vídeos o infografías con licencia libre.
  - **Aplicabilidad:** la audiencia puede empezar a usarlo tras la charla.

## 3. Escribir la página de exploración

Sustituye el contenido de `docs/01-exploracion/index.md` por:

1. **Introducción breve**: metodología (fuentes consultadas, fecha de búsqueda, criterios).
2. **Tabla comparativa**: nº, tema, pregunta clínica, puntuación por criterio y total.
3. **Ficha por tema** (una sección `## N. Tema` por candidato): pregunta clínica, por qué ahora, guías que lo respaldan, evidencia clave con citas, cifras de rendimiento, recursos visuales disponibles, posible estructura de la charla en 3–4 bloques y riesgos (poca evidencia, demasiado amplio…).
4. **Recomendación**: tus 3 favoritos con una línea de justificación cada uno, dejando claro que la decisión es del usuario.

Añade todas las referencias usadas a `docs/05-fuentes/index.md`, en su sección y con el formato definido en CLAUDE.md, y enlázalas desde las fichas.

## 4. Cerrar

1. `mkdocs build --strict` (con `.venv/bin/mkdocs`) debe pasar.
2. Actualiza `ESTADO.md`: fase 2 (esperando elección), lista numerada corta de temas y entrada en la bitácora.
3. Commit y push (`exploracion: lista de temas candidatos POCUS`).
4. Presenta al usuario en el chat **la tabla resumida** (nº, tema y puntuación total) y pídele que elija por número. Puede combinar o acotar temas. Cuando elija, registra la decisión y su justificación en ESTADO.md y en una sección `## Tema elegido` al inicio de `docs/01-exploracion/index.md`.
