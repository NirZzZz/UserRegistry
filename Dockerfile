FROM python:3.9-slim
RUN apt-get update && \
    apt-get install mariadb-server -y && \
    apt install -y netcat-traditional && \
    rm -rf /var/lib/apt/lists/* \
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000 5001
CMD ["bash", "-c", "python3 rest_app.py & python3 web_app.py"]