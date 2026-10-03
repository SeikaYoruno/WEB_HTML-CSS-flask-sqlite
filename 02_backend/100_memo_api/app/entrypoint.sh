#!/bin/sh
set -e

flask db upgrade
python -c "from app import init_db; init_db()"   # メモが1件も無ければ初期データを入れる

exec gunicorn --bind 0.0.0.0:5085 app:app
