web:python manage.py runserver
web:python manage.py collectstatic --noinput;
web: gunicorn apocalypse.wsgi --log-file -
heroku ps:scale web=1
