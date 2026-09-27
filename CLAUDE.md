# Sesión clínica POCUS — Harness del proyecto

## Objetivo

Preparar una **sesión clínica de 20 minutos** sobre un tema de **ecografía a pie de cama (POCUS)** en la práctica clínica, basada en **protocolos y guías clínicas vigentes**. El resultado final son dos entregables:

1. **Web** (MkDocs Material → Netlify) con todo el trabajo estructurado: exploración de temas, investigación, síntesis, recursos gráficos y fuentes.
2. **Presentación PowerPoint** (`presentacion/`) con el contenido sintetizado para la charla, imágenes descargadas y diagramas generados por scripts.

Idioma de todo el contenido: **español**. Audiencia de la charla: médicos y residentes (nivel clínico, no técnico-ecográfico avanzado salvo que el tema lo exija).

## Flujo de trabajo (fases)

El estado actual del proyecto vive en [ESTADO.md](ESTADO.md). **Léelo al empezar cada sesión** y actualízalo al terminar.

| Fase | Qué se hace | Skill | Salida principal |
|------|-------------|-------|------------------|
| 1. Exploración | Investigación exploratoria de temas POCUS candidatos con respaldo de guías recientes | `explorar-temas` | `docs/01-exploracion/` |
| 2. Elección | El usuario revisa la lista y **elige** el tema. Claude no elige por él | — (decisión humana) | `ESTADO.md` → tema elegido |
| 3. Investigación | Búsqueda profunda (PubMed, guías, sociedades) con fuentes y estudios | `investigar-tema` | `docs/02-investigacion/`, `docs/05-fuentes/` |
| 4. Recursos | Buscar y descargar infografías/imágenes con licencia compatible; generar diagramas con scripts | `investigar-tema` / `sintetizar-presentacion` | `docs/assets/`, `docs/04-recursos/` |
| 5. Síntesis | Guion y estructura de una charla de 20 min | `sintetizar-presentacion` | `docs/03-sintesis/` |
| 6. Presentación | Generar el `.pptx` y revisarlo en PowerPoint | `sintetizar-presentacion` | `presentacion/*.pptx` |

No saltes fases: no se investiga a fondo sin tema elegido, y no se sintetiza sin investigación documentada.

## Reglas de evidencia (obligatorias)

- **Toda afirmación clínica lleva cita.** Nada de datos sin fuente (sensibilidad, especificidad, recomendaciones, puntos de corte…).
- **Prioridad de fuentes:**
  1. Guías y consensos internacionales vigentes (p. ej. ACEP, WINFOCUS, ESC, ERC, ESICM, ASE, EFSUMB, SEMES/SEMI/SEMERGEN/semFYC y otras sociedades españolas).
  2. Revisiones sistemáticas y metaanálisis (Cochrane, PubMed).
  3. Ensayos clínicos y estudios de precisión diagnóstica relevantes.
  4. Revisiones narrativas y material docente solo como apoyo, nunca como única fuente de un dato.
- **Vigencia:** prioriza publicaciones de los últimos 5 años; si una guía clave es más antigua, indica si sigue vigente o si hay actualización. Registra siempre el año.
- **Identificadores verificables:** para artículos, PMID y/o DOI; para guías, organismo, año y URL. **Nunca inventes una referencia**: si no puedes verificarla (abrirla o encontrarla en PubMed), no la uses o márcala como `[POR VERIFICAR]`.
- **Nivel de evidencia:** cuando la guía lo indique, recoge clase de recomendación y nivel de evidencia.
- Distingue claramente **evidencia** de **opinión de experto** y señala controversias o lagunas.

## Reglas de recursos gráficos

- Descarga solo imágenes con licencia que permita reutilización docente: **dominio público, Creative Commons** (CC BY, CC BY-SA, CC BY-NC para uso docente no comercial) o material explícitamente autorizado. Fuentes preferentes: Wikimedia Commons, Radiopaedia (respetando su licencia CC BY-NC-SA), artículos open access (PMC) con licencia CC.
- Cada imagen descargada se registra en [docs/04-recursos/creditos.md](docs/04-recursos/creditos.md): archivo, título, autor, fuente (URL), licencia.
- Nombres de archivo en minúsculas, con guiones, descriptivos: `docs/assets/img/<tema>-<descripcion>.png`.
- Los **diagramas propios** se generan con scripts de Python en `scripts/` (matplotlib u otras librerías) y se guardan en `docs/assets/diagramas/`. El script debe poder regenerar la figura.
- No incluir imágenes con datos identificables de pacientes.
- **Dos identidades visuales:** la **web** usa la paleta rosa oro (`docs/stylesheets/extra.css`); la **presentación y los diagramas** son sobrios y elegantes: blanco y negro con grises y un único acento **morado** (`#5B3F8C`) usado con moderación. El rosa oro no se usa nunca en el `.pptx` ni en los diagramas.

## Estructura del repositorio

```
CLAUDE.md                 ← este harness
ESTADO.md                 ← fase actual, tema elegido, próximos pasos, bitácora de sesiones
mkdocs.yml                ← configuración de la web
docs/                     ← contenido de la web (todo en Markdown)
  index.md
  01-exploracion/         ← temas candidatos y criterios de elección
  02-investigacion/       ← investigación del tema elegido (un .md por subtema)
  03-sintesis/            ← guion de la charla de 20 min, mensajes clave
  04-recursos/            ← galería de imágenes, diagramas y créditos
  05-fuentes/             ← bibliografía completa
  assets/img/             ← imágenes descargadas
  assets/diagramas/       ← figuras generadas por scripts
  assets/brand/           ← logo e imagen de portada (generados por scripts/web/graficos_web.py)
  stylesheets/extra.css   ← estilo de la web (paleta rosa oro, tipografía, portada)
overrides/                ← plantillas de Material: main.html (fuentes), home.html (portada)
scripts/
  build_pptx.py           ← genera el .pptx desde presentacion/diapositivas.yaml
  exportar_pdf.sh         ← exporta el .pptx a PDF con PowerPoint (revisión visual)
  diagramas/estilo.py     ← paleta y estilo comunes para los diagramas
  diagramas/*.py          ← un script por diagrama → docs/assets/diagramas/
  web/graficos_web.py     ← gráficos de identidad de la web (SVG)
presentacion/             ← diapositivas.yaml (guion) y .pptx final
.claude/skills/           ← skills del proyecto
.claude/hooks/            ← hooks (commit + push al cerrar sesión)
```

## Convenciones de contenido (Markdown)

- Todo el contenido de la web es Markdown dentro de `docs/`. Si añades una página, añádela también al `nav` de `mkdocs.yml`.
- Cita en el texto con el formato `[Autor, año](../05-fuentes/index.md#clave)` o nota al pie `[^clave]`, y añade la entrada correspondiente en `docs/05-fuentes/index.md`.
- Formato de cada referencia en la bibliografía:
  `- <a id="clave"></a>**Autor A, Autor B, et al.** Título. *Revista*. Año;Vol(N):págs. PMID: xxxx · DOI: [xxxx](https://doi.org/xxxx) · Tipo: guía | RS/MA | ECA | observacional | revisión`
- Estética de la web: paleta rosa oro definida en `docs/stylesheets/extra.css` (variables `--pc-*`); el modo claro/oscuro sigue al sistema, sin selector ni enlace al repositorio. La fase mostrada en la portada se cambia con `fase_actual` en el front matter de `docs/index.md`.
- Usa admonitions de Material (`!!! note`, `!!! warning`, `!!! tip`) para perlas clínicas, errores frecuentes y mensajes clave.

## Entorno técnico

- Python 3 con entorno virtual en `.venv/` (no se sube a git).
  - Web: `pip install -r requirements.txt` → `mkdocs serve` (local) / `mkdocs build` (Netlify).
  - Scripts: `pip install -r scripts/requirements.txt` (python-pptx, matplotlib, etc.).
- Netlify construye automáticamente con `netlify.toml` en cada push a `main`.
- PowerPoint para macOS está instalado: puede abrirse con `open presentacion/<archivo>.pptx` para revisar el resultado.
- Antes de hacer commit, comprueba que la web compila: `mkdocs build --strict`.

## Regla de fin de sesión: commit + push

**Al terminar cada sesión de trabajo** (o cuando el usuario indique que terminamos):

1. Actualiza `ESTADO.md` (fase, avances, próximos pasos, entrada en la bitácora con fecha).
2. Verifica que la web compila (`mkdocs build --strict`).
3. Haz `git add -A`, commit con un mensaje descriptivo en español (`tipo: resumen`, p. ej. `investigacion: añadir evidencia sobre protocolo BLUE`) y `git push origin main`.

Como red de seguridad, el hook `SessionEnd` ([.claude/hooks/fin-de-sesion.sh](.claude/hooks/fin-de-sesion.sh)) hace commit y push automático de cualquier cambio pendiente al cerrar Claude Code.
