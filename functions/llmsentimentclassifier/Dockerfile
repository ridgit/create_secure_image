# Utiliser une image légère Python 3.7 Alpine
FROM python:3.7-alpine

# Copier requirements.txt pour l'installation de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port 5000
EXPOSE 5000

# Exécuter app.py avec python
CMD ["python", "app.py"]
