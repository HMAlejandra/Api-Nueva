# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt from root
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the api directory to /app
COPY api/ .

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "run.py"]