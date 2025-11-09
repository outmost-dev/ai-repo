#!/bin/bash

# Auto-push script pentru ai-repo
# Execută totul automat fără întrebări

set -e  # Stop on any error

echo "🚀 Auto-push pornit..."
echo ""

# Navigate to repo root
cd /home/valim/ai-repo

# Check status
echo "📊 Verificare status..."
git status
echo ""

# Stage all changes
echo "➕ Adăugare modificări..."
git add .
echo ""

# Check if there are changes to commit
if git diff --staged --quiet; then
  echo "✅ Nu există modificări de comis."
  exit 0
fi

# Show what will be committed
echo "📝 Modificări de comis:"
git diff --staged --stat
echo ""

# Generate commit message based on changes
echo "💬 Generare mesaj commit..."
CHANGED_FILES=$(git diff --staged --name-only | head -5 | tr '\n' ', ' | sed 's/,$//')

if [ -n "$CHANGED_FILES" ]; then
  COMMIT_MSG="Actualizare: $CHANGED_FILES"
else
  COMMIT_MSG="Actualizare fișiere"
fi

echo "Mesaj: $COMMIT_MSG"
echo ""

# Commit
echo "💾 Commit..."
git commit -m "$COMMIT_MSG"
echo ""

# Push
echo "📤 Push la GitHub..."
git push

echo ""
echo "✅ Toate modificările au fost push-uite cu succes!"
