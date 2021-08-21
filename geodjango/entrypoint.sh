#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python3.8 manage.py flush --no-input
python3.8 manage.py makemigrations
python3.8 manage.py migrate
python3.8 manage.py shell -c "from world.data import load_hokkaido; load_hokkaido.run()"
python3.8 manage.py shell -c "from world.data import load_elementary_school; load_elementary_school.run()"
python3.8 manage.py shell -c "from world.data import load_public_facility; load_public_facility.run()"
python3.8 manage.py shell -c "from world.data import load_busstop; load_busstop.run()"
exec "$@"
