---
name: sintetizar-presentacion
description: Fases 5 y 6 del proyecto. Sintetiza la investigación del tema POCUS en el guion de una sesión clínica de 20 minutos, genera diagramas con scripts de Python y construye la presentación PowerPoint (.pptx) con notas del orador, revisándola visualmente con PowerPoint. Usar cuando la investigación esté documentada y se pida sintetizar, preparar la charla o generar/actualizar el PowerPoint.
---

# Sintetizar y generar la presentación

Objetivo: convertir la investigación en una **charla de 20 minutos clara y memorable**, publicar el guion en la web y generar un `.pptx` profesional con imágenes, diagramas propios y notas del orador.

**Precondición:** `docs/02-investigacion/` contiene la investigación del tema elegido (ver ESTADO.md). Si no, usa `investigar-tema`.

Lee antes [CLAUDE.md](../../../CLAUDE.md), [ESTADO.md](../../../ESTADO.md), toda `docs/02-investigacion/`, `docs/04-recursos/` y `docs/05-fuentes/index.md`.

## 1. Mensajes clave

Antes de pensar en diapositivas, define **3 mensajes para llevar a casa**: lo que la audiencia debe recordar y aplicar mañana. Cada uno debe estar respaldado por una guía o por evidencia sólida de la investigación. Todo lo que no sirva a estos mensajes se queda en la web y no entra en la charla.

## 2. Estructura de 20 minutos

A razón de 1 diapositiva por minuto aproximadamente: **16–20 diapositivas** de contenido más portada y bibliografía. Estructura orientativa:

| Bloque | Tiempo | Contenido |
|--------|--------|-----------|
| Apertura | 2 min | Portada y caso clínico o pregunta que engancha |
| El problema | 2–3 min | Por qué importa: limitaciones del abordaje clásico, datos de impacto |
| Técnica / protocolo | 5–6 min | Cómo se hace: sonda, ventanas, hallazgos (imágenes reales y diagramas) |
| Evidencia | 4–5 min | Rendimiento diagnóstico e impacto clínico. Qué dicen las guías (clase/nivel) |
| Integración | 3 min | Algoritmo práctico, errores frecuentes y limitaciones |
| Cierre | 2 min | Resolución del caso, los 3 mensajes clave y bibliografía |

Reglas de diseño: una idea por diapositiva, ≤6 puntos y ≤12 palabras por punto, cifras grandes en lugar de párrafos, imagen o diagrama siempre que se pueda, y la fuente de cada dato en el pie. Lo que se dice va en las **notas del orador**, no en la diapositiva.

## 3. Guion en la web

Escribe `docs/03-sintesis/index.md` con:

1. Los 3 mensajes clave (admonition `!!! success`).
2. Estructura por bloques con tiempos.
3. **Guion diapositiva a diapositiva**: número, título, contenido visible, visual, fuente, tiempo y texto hablado (notas del orador).
4. Preguntas previsibles del público con respuesta breve y referenciada.
5. Enlace de descarga del .pptx una vez generado (copia el .pptx a `docs/assets/` para que se sirva desde la web).

## 4. Diagramas con scripts

Para algoritmos, esquemas de protocolo, comparativas de sensibilidad y especificidad o gráficos de resultados de estudios:

- Un script por diagrama en `scripts/diagramas/<nombre>.py`, usando el estilo común:
  ```python
  import sys; from pathlib import Path
  sys.path.insert(0, str(Path(__file__).parent))
  from estilo import aplicar_estilo, guardar, PALETA, SERIES
  import matplotlib.pyplot as plt
  aplicar_estilo()
  fig, ax = plt.subplots(figsize=(12, 6.75))  # 16:9
  ...
  guardar(fig, "nombre-descriptivo")  # → docs/assets/diagramas/nombre-descriptivo.png
  ```
- Los datos de los gráficos salen **de la investigación** y el script cita la fuente en un comentario. Texto en español y legible a distancia (≥14 pt).
- Ejecuta con `.venv/bin/python scripts/diagramas/<nombre>.py` y **mira el PNG resultante** con Read antes de darlo por bueno.
- Añade los diagramas a la galería de `docs/04-recursos/index.md`, en la sección "Diagramas propios".

## 5. Generar el PowerPoint

Escribe el guion estructurado en `presentacion/diapositivas.yaml` y constrúyelo con [scripts/build_pptx.py](../../../scripts/build_pptx.py). Los tipos disponibles son `portada`, `seccion`, `contenido` (con `imagen` opcional), `imagen`, `dos_columnas`, `tabla`, `mensaje` y `referencias`. El docstring del script explica los campos.

```yaml
titulo: "Título de la sesión"
subtitulo: "Subtítulo"
autora: "Yaiza Díaz del Castillo"
fecha: "Mes Año"
archivo: sesion-clinica.pptx
diapositivas:
  - tipo: portada
  - tipo: contenido
    titulo: "…"
    puntos: ["…", {texto: "…", sub: ["…"]}]
    imagen: docs/assets/img/…png
    fuente: "Autor et al., Revista 2024"
    notas: |
      Texto que se dice en esta diapositiva.
  - tipo: mensaje
    texto: "Mensaje clave"
```

```bash
.venv/bin/python scripts/build_pptx.py presentacion/diapositivas.yaml
```

Si hace falta un tipo de diapositiva nuevo, amplía `build_pptx.py` manteniendo el estilo existente.

## 6. Revisión visual con PowerPoint

1. Exporta a PDF con PowerPoint: `scripts/exportar_pdf.sh presentacion/sesion-clinica.pptx`.
2. Renderiza las páginas a PNG (pypdfium2) en el scratchpad, en cuadrículas de 6–9 diapositivas, y **revísalas con Read**. Busca texto desbordado o cortado, imágenes pixeladas o mal encuadradas, diapositivas recargadas y fuentes ausentes.
3. Corrige en el YAML o en los scripts y regenera hasta que esté limpio.
4. Comprueba el tiempo: suma los minutos del guion (objetivo 18–20 min).
5. Abre el resultado para el usuario con `open presentacion/sesion-clinica.pptx`.

El PDF exportado se puede conservar en `presentacion/` como copia de consulta.

## 7. Cerrar

1. `.venv/bin/mkdocs build --strict` debe pasar.
2. Actualiza `ESTADO.md`: fase 6 completada o pendiente de revisión, cambios solicitados por el usuario y bitácora.
3. Commit y push (`presentacion: <resumen>`).
4. Resume al usuario: nº de diapositivas, duración estimada, mensajes clave y enlace a la web.
