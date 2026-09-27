"""Estilo común para todos los diagramas del proyecto (misma paleta sobria que la presentación).

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

# Estilo sobrio y elegante: blanco y negro con escala de grises y un único acento morado.
# El acento se reserva para lo que hay que mirar (el dato clave, la rama del algoritmo que importa).
# El rosa oro es solo de la web: no se usa en diagramas ni en la presentación.
PALETA = {
    "primario": "#111111",   # trazos y texto principal
    "acento": "#5B3F8C",     # morado sobrio, con moderación
    "acento_suave": "#E9E4F2",  # relleno tenue del acento (cajas destacadas)
    "texto": "#1A1A1A",
    "suave": "#707070",      # texto secundario, ejes
    "linea": "#D4D4D4",      # rejillas y filetes
    "fondo_alt": "#F5F5F5",  # cajas neutras
    # Semántica sin semáforo: se distingue por tono/forma, no por rojo-verde
    "positivo": "#5B3F8C",
    "alerta": "#707070",
    "negativo": "#111111",
}
# Series: negro, grises y morado al final para la serie que se quiere destacar
SERIES = ["#111111", "#707070", "#A8A8A8", "#5B3F8C", "#D4D4D4"]


def aplicar_estilo():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Avenir Next", "Arial", "DejaVu Sans"],
        "font.size": 14,
        "axes.titlesize": 18,
        "axes.titleweight": "normal",
        "axes.titlelocation": "left",
        "axes.titlepad": 14,
        "axes.titlecolor": PALETA["primario"],
        "axes.labelcolor": PALETA["texto"],
        "axes.edgecolor": PALETA["suave"],
        "axes.linewidth": 0.8,
        "axes.grid": False,
        "grid.color": PALETA["linea"],
        "grid.linewidth": 0.6,
        "lines.linewidth": 1.8,
        "legend.frameon": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.prop_cycle": plt.cycler(color=SERIES),
        "xtick.color": PALETA["suave"],
        "ytick.color": PALETA["suave"],
        "xtick.labelcolor": PALETA["texto"],
        "ytick.labelcolor": PALETA["texto"],
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
