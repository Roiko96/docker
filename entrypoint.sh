#!/usr/bin/env sh
set -e

# תעדוף: משתנה סביבה MODE, ואם לא הוגדר — הפרמטר הראשון
MODE="${MODE:-$1}"

if [ "$MODE" = "web" ]; then
  exec python app.py
elif [ "$MODE" = "cli" ] || [ -z "$MODE" ]; then
  exec python main.py
else
  # מאפשר להריץ כל פקודה אחרת למתקדמים
  exec "$@"
fi
