FROM python:3.11.5

USER 0

WORKDIR /usr/app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python manage.py collectstatic --no-input

CMD gunicorn Comics.wsgi --bind 0.0.0.0:8000 --workers 3