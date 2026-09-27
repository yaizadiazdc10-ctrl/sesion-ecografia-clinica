"""Estilo común para todos los diagramas del proyecto (misma paleta que la presentación).

Uso en un script de diagrama:
    from estilo import aplicar_estilo, guardar, PALETA
    aplicar_estilo()
    fig, ax = plt.subplots(figsize=(12, 6.75))   # 16:9
    ...
    guardar(fig, "nombre-descriptivo")           # → docs/assets/diagramas/nombre-descriptivo.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "docs" / "assets" / "diagramas"

PALETA = {
    "primario": "#0F766E",
    "acento": "#06B6D4",
    "texto": "#1F2937",
    "suave": "#6B7280",
    "fondo_alt": "#F0FDFA",
    "positivo": "#16A34A",
    "alerta": "#F59E0B",
    "negativo": "#DC2626",
}
SERIES = ["#0F766E", "#06B6D4", "#F59E0B", "#8B5CF6", "#DC2626", "#64748B"]


def aplicar_estilo():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.size": 14,
        "axes.titlesize": 18,
        "axes.titleweight": "bold",
        "axes.titlecolor": PALETA["primario"],
        "axes.labelcolor": PALETA["texto"],
        "axes.edgecolor": PALETA["suave"],
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.prop_cycle": plt.cycler(color=SERIES),
        "xtick.color": PALETA["texto"],
        "ytick.color": PALETA["texto"],
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    })


def guardar(fig, nombre):
    SALIDA.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA / f"{nombre}.png"
    fig.savefig(ruta, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"Guardado {ruta.relative_to(RAIZ)}")
    return ruta
