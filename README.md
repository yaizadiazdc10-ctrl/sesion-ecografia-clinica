# Sesión clínica POCUS

Preparación de una sesión clínica de 20 minutos sobre ecografía a pie de cama (POCUS): exploración de temas, investigación basada en guías actuales, recursos gráficos, web de consulta y presentación PowerPoint.

- **Web:** MkDocs Material, desplegada en Netlify en cada push a `main`.
- **Presentación:** `presentacion/`, generada con `python-pptx` a partir de la síntesis.
- **Reglas del proyecto:** ver [CLAUDE.md](CLAUDE.md). **Estado:** ver [ESTADO.md](ESTADO.md).

## Uso local

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r scripts/requirements.txt
mkdocs serve   # http://127.0.0.1:8000
```
