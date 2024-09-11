#!/bin/bash

rm db.sqlite3
rm -rf ./digestapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations digestapi
python3 manage.py migrate digestapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

python manage.py loaddata categories.json
python manage.py loaddata books.json
python manage.py loaddata reviews.json
