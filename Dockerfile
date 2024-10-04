FROM python:3.9-slim
RUN apt-get update && \
    apt-get install -y mariadb-server && \
    apt install -y netcat-traditional && \
    rm -rf /var/lib/apt/lists/* \
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
EXPOSE ${REST_PORT} ${WEB_PORT}
CMD ["bash", "-c", "python3 create_table.py & python3 rest_app.py & python3 web_app.py"]