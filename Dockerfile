FROM python:3.10.13-slim-bullseye

#RUN adduser --system --no-create-home anon

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ .

EXPOSE 8000

#RUN chown -R anon /app

#USER anon
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
