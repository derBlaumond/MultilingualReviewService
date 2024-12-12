# Stage 1: Use an official lightweight Python image as a base
FROM python:3.10-slim

# Set environment variables to disable buffering and support UTF-8 encoding
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the service port (adjust if different)
EXPOSE 8080

# Command to run the application (replace app.py with the entry point of your service)
CMD ["python", "app.py"]
