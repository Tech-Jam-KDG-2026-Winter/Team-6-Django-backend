#!/usr/bin/env bash
set -euo pipefail

# Paths should stay consistent with repo layout.
ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)
FRONTEND_DIR="$ROOT_DIR/Team-6-React-frontend/Team-6-react-frontend"
BACKEND_DIR="$ROOT_DIR/Team-6-Django-backend-feature-auth-goal-api"
TEMPLATES_DIR="$BACKEND_DIR/backend/templates/app"
STATIC_DIR="$BACKEND_DIR/backend/static/app"
BACKEND_PYTHON="$BACKEND_DIR/venv/bin/python"
if [ ! -x "$BACKEND_PYTHON" ]; then
  BACKEND_PYTHON="python3"
fi

echo "[1/5] Installing frontend dependencies"
npm --prefix "$FRONTEND_DIR" install

echo "[2/5] Building React app"
npm --prefix "$FRONTEND_DIR" run build

echo "[3/5] Copying build artifacts"
mkdir -p "$TEMPLATES_DIR"
mkdir -p "$STATIC_DIR/assets"
cp "$FRONTEND_DIR/dist/index.html" "$TEMPLATES_DIR/index.html"
rm -rf "$STATIC_DIR/assets"
mkdir -p "$STATIC_DIR/assets"
cp -R "$FRONTEND_DIR/dist/assets/." "$STATIC_DIR/assets/" || true

echo "[4/5] Collecting static files"
cd "$BACKEND_DIR"
$BACKEND_PYTHON manage.py collectstatic --noinput

echo "[5/5] Done. React is now wired into Django under /app and /static/app"
