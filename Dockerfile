# Starts a custom Docker image based on a Alpine Linux-based Python Docker image
FROM python:3.8-alpine

# Changes working directory to /app (similar to UNIX `mkdir ./app && cd ./app`)
WORKDIR /app

# Copies the current directory to the container current directory
COPY . .

# Installs python dependancies
RUN pip install -r requirements.txt

# Definies the environment variables for Flask
ENV FLASK_APP=solidvault

# Exposes the container's port 5000
EXPOSE 5000

# Defines the entrypoint for the Docker app
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]

