#Ce Dockerfile commence avec une image Python 3.8,
#crée un répertoire de travail, copie le fichier requirements.txt dans l'image et installe les packages nécessaires. 
#Ensuite, il copie le fichier app.py et enfin, il définit la commande par défaut pour exécuter l'application Flask.
FROM python:3.8

WORKDIR /textanalyzer

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
