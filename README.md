# simple-docker-app
Will Create and deploy a two-part web application: a backend written in Python (Flask) and a MySQL database. Will use Docker to containerize these two services and Docker Compose to orchestrate their deployment

# 1) Creating the Dockerfile in the directory where you files are found

```
$ touch Dockerfile
```


```
Use an official Python runtime as a parent image, This specifies the base image for the container, which is a lightweight Python 3.8 environment.
$ FROM python:3.8-slim
```


```
Set/Create the working directory in the container
$ WORKDIR /app
```


```
Copy the current directory contents into the container, This copies everything in your local directory (including app.py and requirements.txt) into the /app directory in the container
COPY . /app`
```

```
Install any needed packages specified in requirements.txt, This installs the dependencies listed in requirements.txt inside the container 
$ RUN pip install --no-cache-dir -r requirements.txt`
```

```
Make port 5000 available to the outside world
$ EXPOSE 5000
```

```
Run app.py when the container launches
$ CMD ["python", "app.py"]
```
`docker build -t flask-app .`
```
docker build: This command tells Docker to build an image.
-t flask-app: This tags your image with the name flask-app. You can change this name to whatever you prefer.
.: The dot specifies that Docker should look for the Dockerfile in the current directory.
```


```
To install docker : sudo apt install docker.io
                    sudo systemctl start docker
                    sudo systemctl enable docker
                    sudo systemctl status docker
                    sudo usermod -aG docker $USER
                    docker run hello-world
```
                    
```
Run the container using the following command:
docker run -p 5000:5000 flask-app
```

# 1) Set Up Docker Compose to Link Flask and MySQL
```
Service Orchestration: Docker Compose handles the orchestration of multiple containers.
It makes sure that the MySQL service is up before the Flask app tries to connect, which is handled by the depends_on directive in Docker Compose.

Networking Made Easy: Compose automatically sets up networking between the containers, so you don’t have to configure the networking manually.
The Flask app can connect to the MySQL service using the service name (db), which Docker Compose resolves for you.

Simplicity: Instead of manually running docker run commands for both MySQL and Flask,
Docker Compose allows you to start everything with one command (docker-compose up), which is more efficient for development and production.

Environment Variables: With Compose, it's easy to define environment variables (e.g., for the MySQL password, database name)
in the docker-compose.yml file, and they’ll automatically be passed to the containers
```
