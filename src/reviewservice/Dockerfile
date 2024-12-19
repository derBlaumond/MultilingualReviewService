# FROM python:3.9-slim

# WORKDIR /reviewservice
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY . .

# EXPOSE 8080
# CMD ["python", "-m", "reviewservice.server"]
# #CMD ["python", "server.py"]
FROM python:3.12.6-slim@sha256:ad48727987b259854d52241fac3bc633574364867b8e20aec305e6e7f4028b26 AS base

FROM base AS builder

# Install necessary tools for building dependencies
RUN apt-get -qq update \
    && apt-get install -y --no-install-recommends \
        wget g++ \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM base
# Enable unbuffered logging
ENV PYTHONUNBUFFERED=1

# Set working directory for the application
WORKDIR /reviewservice

# Copy Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/ /usr/local/lib/python3.12/

# Copy the application code
COPY . .

ENV PYTHONPATH=/reviewservice
# Set environment variables (if needed)
ENV PORT "8080"
EXPOSE 8080

# Run the application
CMD ["python", "-m", "server"]

