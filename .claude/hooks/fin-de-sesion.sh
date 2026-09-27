#!/bin/bash
# Red de seguridad al cerrar Claude Code: commit + push de los cambios pendientes.
# Claude debería haber hecho ya un commit descriptivo; esto solo recoge lo que quede.

cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}" || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

if [ -n "$(git status --porcelain)" ]; then
  git add -A
  git commit -q -m "chore: guardado automático al cerrar la sesión ($(date '+%Y-%m-%d %H:%M'))"
fi

# Sube cualquier commit local que no esté en el remoto
if git rev-parse --abbrev-ref '@{u}' >/dev/null 2>&1; then
  if [ -n "$(git log '@{u}..HEAD' --oneline 2>/dev/null)" ]; then
    git push -q 2>&1 || echo "Aviso: no se pudo hacer push" >&2
  fi
fi
exit 0
