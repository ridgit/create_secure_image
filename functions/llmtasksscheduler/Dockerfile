# Utiliser une image Python 3 légère
FROM python:3.8-slim-buster

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copier requirements.txt et installer les dépendances nécessaires
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copier le code source dans le conteneur
COPY app.py .

# Exécuter l'application
CMD ["python", "app.py"]
