# utiliser une image Python en tant que base
FROM python:3.8-alpine

# définir le répertoire de travail
WORKDIR /app

# copier le fichier requirements.txt
COPY . .

# installer les dépendances
RUN pip install -r requirements.txt

# définir les variables d'environnement
ENV FLASK_APP=solidvault

# exposer le port 5000
EXPOSE 5000

# définir le point d'entrée de l'application
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]

