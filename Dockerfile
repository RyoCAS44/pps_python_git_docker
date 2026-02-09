# ---------- Fase 1: resolución de dependencias ----------
FROM python:3.13-slim AS builder

WORKDIR /app

# Copiamos solo lo necesario para instalar dependencias
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------- Fase 2: ejecución ----------
FROM python:3.13-slim

WORKDIR /app

# Copiamos las dependencias ya instaladas desde la fase builder
COPY --from=builder /usr/local /usr/local

# Copiamos el código de la aplicación
COPY app.py bayeta.py frases.txt ./

EXPOSE 5000

CMD ["python", "app.py"]
