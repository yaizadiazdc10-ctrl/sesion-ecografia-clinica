"""Árbol de decisión simplificado del protocolo BLUE.

Fuente: Lichtenstein DA, Mezière GA. Chest 2008;134:117-25 (PMID 18403664);
Lichtenstein DA. Chest 2015 / revisión 2014 (PMID 24401163). Simplificación docente propia.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import matplotlib.pyplot as plt  # noqa: E402

from _cajas import caja, flecha  # noqa: E402
from estilo import PALETA, aplicar_estilo, guardar  # noqa: E402

aplicar_estilo()
fig, ax = plt.subplots(figsize=(13, 7.3))
ax.set_xlim(0, 13)
ax.set_ylim(0, 7.3)
ax.axis("off")

caja(ax, 6.5, 6.7, 3.6, 0.8, "¿Deslizamiento pleural?", pregunta=True, size=16)
caja(ax, 4.6, 5.2, 3.8, 0.8, "¿Líneas B anteriores?", pregunta=True, size=15)
caja(ax, 10.6, 5.2, 3.4, 0.8, "Perfil A′ · ¿punto pulmón?", pregunta=True, size=15)
caja(ax, 1.5, 3.5, 2.8, 1.0, "Perfil B\nEdema hemodinámico", destacada=True, size=15, negrita=True)
caja(ax, 4.6, 3.5, 2.8, 1.0, "Perfil A/B · C\nNeumonía", size=15)
caja(ax, 7.7, 3.5, 2.8, 0.8, "Perfil A · ¿TVP?", pregunta=True, size=15)
caja(ax, 10.6, 3.5, 2.6, 0.8, "Neumotórax", size=15)
caja(ax, 6.3, 1.9, 2.2, 0.8, "TEP", size=15)
caja(ax, 9.1, 1.9, 2.4, 0.8, "¿PLAPS?", pregunta=True, size=15)
caja(ax, 7.8, 0.55, 2.4, 0.8, "Neumonía", size=15)
caja(ax, 10.4, 0.55, 2.4, 0.8, "EPOC / asma", size=15)

flecha(ax, (5.8, 6.3), (4.9, 5.6), "Sí", lado="izquierda")
flecha(ax, (7.3, 6.3), (10.0, 5.6), "No", lado="derecha")
flecha(ax, (3.6, 4.8), (1.9, 4.0), "Bilaterales, difusas", lado="izquierda", destacada=True)
flecha(ax, (4.6, 4.8), (4.6, 4.0), "Asimétricas\no consolidación", lado="derecha")
flecha(ax, (5.6, 4.8), (7.3, 3.9), "No: líneas A", lado="derecha")
flecha(ax, (10.6, 4.8), (10.6, 3.9), "Sí", lado="derecha")
flecha(ax, (7.2, 3.1), (6.5, 2.3), "Sí", lado="izquierda")
flecha(ax, (8.2, 3.1), (8.9, 2.3), "No", lado="derecha")
flecha(ax, (8.7, 1.5), (8.1, 0.95), "Sí", lado="izquierda")
flecha(ax, (9.5, 1.5), (10.1, 0.95), "No", lado="derecha")

ax.text(0, 0.0, "Simplificado de Lichtenstein 2008 (BLUE) · Diseñado en UCI con operadores expertos",
        fontsize=11, color=PALETA["suave"])
guardar(fig, "lus-arbol-blue")
