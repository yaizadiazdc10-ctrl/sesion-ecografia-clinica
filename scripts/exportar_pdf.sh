#!/bin/bash
# Exporta un .pptx a PDF con Microsoft PowerPoint (para revisar visualmente las diapositivas).
# Uso: scripts/exportar_pdf.sh presentacion/sesion-clinica.pptx
# La primera vez macOS pedirá permiso para que la terminal controle PowerPoint.
set -euo pipefail

PPTX="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
PDF="${PPTX%.pptx}.pdf"

osascript <<EOF
tell application "Microsoft PowerPoint"
  open POSIX file "$PPTX"
  delay 2
  save active presentation in POSIX file "$PDF" as save as PDF
  close active presentation saving no
end tell
EOF

echo "PDF: $PDF"
