# Base image with Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the service code into the container
COPY . .

# Expose the port the service listens on
EXPOSE 8080

# Command to run the translation service
CMD ["python", "server.py"]
