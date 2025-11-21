# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Api-Nueva-main folder
COPY Api-Nueva-main ./Api-Nueva-main

# Expose port
EXPOSE 8080

# Run the application from Api-Nueva-main directory
CMD ["sh", "-c", "cd Api-Nueva-main && uvicorn api.app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]