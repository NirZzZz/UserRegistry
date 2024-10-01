FROM python:3.9-slim
RUN apt-get update && \
    apt-get install -y mariadb-server && \
    apt install -y netcat-traditional && \
    rm -rf /var/lib/apt/lists/* \
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt