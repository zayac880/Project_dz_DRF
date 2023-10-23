FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt
COPY . .
COPY ./migrate.sh /migrate
RUN sed -i 's/\r$//g' /migrate
RUN chmod u+x /migrate

EXPOSE 8000
ENTRYPOINT ["/migrate"]
