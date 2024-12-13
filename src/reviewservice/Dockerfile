FROM python:3.9-slim

WORKDIR /reviewservice
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8080
CMD ["python", "server.py"]
# FROM python:3.12.6-slim@sha256:ad48727987b259854d52241fac3bc633574364867b8e20aec305e6e7f4028b26 AS base

# FROM base AS builder

# RUN apt-get -qq update \
#     && apt-get install -y --no-install-recommends \
#         wget g++ \
#     && rm -rf /var/lib/apt/lists/*

# # get packages
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# FROM base
# # Enable unbuffered logging
# ENV PYTHONUNBUFFERED=1

# # get packages
# WORKDIR /reviewservice

# # Grab packages from builder
# COPY --from=builder /usr/local/lib/python3.12/ /usr/local/lib/python3.12/

# # Add the application
# COPY . .

# # set listen port
# ENV PORT "8080"
# EXPOSE 8080

# ENTRYPOINT ["python", "server.py"]
