# Utilise l'image officielle Python légère
FROM python:3.11-slim

# Définir un répertoire de travail
WORKDIR /app

# Copier les fichiers de la fonction dans le conteneur
COPY . .

# Exposer le port par défaut de Flask
EXPOSE 5000

# Définir les variables d'environnement (optionnel mais recommandé)
ENV HOST=0.0.0.0
ENV PORT=5000

# Commande pour lancer l'application Flask
CMD ["python", "app.py"]
