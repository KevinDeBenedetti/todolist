FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENV SECRET_KEY="temp_secret_key_for_build"

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "task_manager.wsgi:application", "--bind", "0.0.0.0:8000"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]