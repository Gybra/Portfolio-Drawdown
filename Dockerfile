# Usa un'immagine base leggera di Python
FROM python:3.11-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia il file requirements.txt e installa le dipendenze
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice dell'applicazione
COPY app.py ./
COPY inc/ ./inc

# Espone la porta 3031
EXPOSE 3031

# Comando per avviare l'app Flask
CMD ["python", "app.py"]