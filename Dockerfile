FROM python:3.9-slim
    WORKDIR /app
    COPY . .
    RUN install -r requirements.txt
    EXPOSE 500
    CMD ["python","app.py"]