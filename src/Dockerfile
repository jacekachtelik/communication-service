# Bazowy obrazy pythona
FROM python:3.9-slim

# Katalog roboczy
WORKDIR /app

# Kopiowanie plików
COPY requirements.txt requirements.txt

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie plików
COPY . .

# Uruchomienie aplikacji
CMD [ "uvicorn" , "api:app", "--host", "0.0.0.0", "--port", "8000" ]