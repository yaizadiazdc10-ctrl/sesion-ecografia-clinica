"""Algoritmo práctico de la disnea aguda con incertidumbre diagnóstica (síntesis docente).

Basado en docs/02-investigacion/a-disnea-ica/06-practica.md: Qaseem A et al., Ann Intern Med 2021
(PMID 33900792, ACP: POCUS si hay incertidumbre); Gargani L et al. 2023 (PMID 37450604);
Lichtenstein DA 2008 (PMID 18403664); Nazerian P et al. 2014 (PMID 24092475, multiórgano en TEP);
Martindale JL et al. 2016 (PMID 26910112, NT-proBNP para descartar). Síntesis propia, no protocolo validado.
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

caja(ax, 6.5, 6.75, 6.6, 0.75, "Disnea aguda con incertidumbre diagnóstica", pregunta=True, size=16)
caja(ax, 6.5, 5.6, 5.6, 0.75, "Ecografía pulmonar (8 zonas) + FoCUS", pregunta=True, size=16)
flecha(ax, (6.5, 6.37), (6.5, 5.98))

# tres ramas
caja(ax, 2.2, 4.1, 3.6, 0.95, "Líneas B bilaterales,\ndifusas, pleura fina", size=14)
caja(ax, 6.5, 4.1, 3.6, 0.95, "Perfil A\n(pulmón seco)", size=14)
caja(ax, 10.8, 4.1, 3.6, 0.95, "Líneas B focales,\nconsolidación", size=14)
flecha(ax, (5.2, 5.22), (2.9, 4.58))
flecha(ax, (6.5, 5.22), (6.5, 4.58))
flecha(ax, (7.8, 5.22), (10.1, 4.58))

caja(ax, 2.2, 2.55, 3.6, 1.05, "+ FEVI deprimida, AI dilatada\no VCI pletórica", pregunta=True, size=14)
caja(ax, 6.5, 2.55, 3.6, 1.05, "Compresión venosa\ny VD en la FoCUS", pregunta=True, size=14)
caja(ax, 10.8, 2.55, 3.6, 1.05, "Neumonía probable", size=15)
flecha(ax, (2.2, 3.62), (2.2, 3.08), destacada=True)
flecha(ax, (6.5, 3.62), (6.5, 3.08))
flecha(ax, (10.8, 3.62), (10.8, 3.08))

caja(ax, 2.2, 0.95, 3.6, 1.2, "ICA muy probable\nDiurético\nEcocardiografía reglada", destacada=True, size=14, negrita=True)
caja(ax, 5.35, 1.0, 2.2, 1.0, "TVP o VD dilatado:\nvía del TEP", size=13)
caja(ax, 7.65, 1.0, 2.2, 1.0, "Normal:\nEPOC/asma, otras", size=13)
flecha(ax, (2.2, 2.02), (2.2, 1.57), destacada=True)
flecha(ax, (6.0, 2.02), (5.5, 1.52))
flecha(ax, (7.0, 2.02), (7.5, 1.52))

ax.text(9.2, 1.35, "Integrar siempre con la clínica", ha="left", fontsize=13, color=PALETA["texto"])
ax.text(9.2, 0.95, "NT-proBNP para descartar · Rx según caso", ha="left", fontsize=12, color=PALETA["suave"])
ax.text(9.2, 0.55, "Documentar zonas y clips · reevaluar", ha="left", fontsize=12, color=PALETA["suave"])
ax.text(0, 0.0, "Síntesis docente basada en ACP 2021, EACVI 2023, BLUE 2008 y Martindale 2016 · "
        "Un perfil A sin TVP no descarta el TEP", fontsize=11, color=PALETA["suave"])
guardar(fig, "lus-algoritmo-disnea")
