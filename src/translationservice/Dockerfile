FROM python:3.10-slim

# Set environment variables to disable buffering and support UTF-8 encoding
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /translationservice

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the service port 
EXPOSE 8080

CMD ["python", "server.py"]
