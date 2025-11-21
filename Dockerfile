FROM python:3.12-slim

WORKDIR /app

# Copiar requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar TODO el contenido de Api-Nueva-main
COPY Api-Nueva-main/ ./

# Exponer puerto
EXPOSE 8080

# Ejecutar la aplicación
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]