# Utiliser une image de base Python 3
FROM python:3.8

# Mettre en place le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt et app.py dans le conteneur
COPY app.py .
COPY requirements.txt .

# Installer les dépendances avec pip
RUN pip install --no-cache-dir -r requirements.txt

# Lancer app.py quand le conteneur se lance
CMD [ "python", "app.py" ]
