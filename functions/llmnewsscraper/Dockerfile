#**Remarque**: Ce Dockerfile utilise l'image Python 3.9 comme base, 
#installe les dépendances du fichier requirements.txt, expose le port 5000 pour Flask et exécute app.py quand le conteneur démarre. 
FROM python:3.9-slim-buster

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
