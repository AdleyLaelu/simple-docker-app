
# 1: Creating the Dockerfile in the directory where you files are found

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
Connection fails because MsQL was not linked to Flask
```
![Capture d’écran 2024-09-04 195518](https://github.com/user-attachments/assets/355f7528-1259-4722-b4bd-e92ec502a7d6)


# 2: Set Up Docker Compose to Link Flask and MySQL
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
`nano docker-compose.yml`
```
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      - MYSQL_HOST=db
      - MYSQL_USER=root
      - MYSQL_PASSWORD=rootpassword
      - MYSQL_DB=test_db

  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: test_db
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
```
```
version: '3': Specifies the version of Docker Compose you're using.
services: Defines the services that will run (in this case, web and db).
web: This is your Flask application.
build: .: This tells Docker to build the Flask app using the Dockerfile in the current directory.
ports: Maps port 5000 inside the container to port 5000 on your machine.
depends_on: Ensures that the db service (MySQL) starts before the web service.
environment: Passes environment variables to the Flask app so it can connect to the MySQL database.
db: This is the MySQL database service.
image: Uses the official MySQL 5.7 image from Docker Hub.
environment: Sets environment variables for MySQL (root password and database name).
volumes: Ensures data persistence by storing the database files in a volume called db_data.
volumes: Defines a named volume (db_data) to persist the MySQL database files.
```
# 3: Modify the Flask App to Use Docker Networking
`nano app.py`
```
In your app.py, ensure that the host is set to db, which refers to the MySQL service defined in docker-compose.yml:
connection = mysql.connector.connect(
    host='db',  # 'db' refers to the MySQL service name in Docker Compose
    user='root',
    password='rootpassword',
    database='test_db'
)
```
# 4: Run the Application with Docker Compose
```
Now, with docker-compose.yml set up, you can bring up both the Flask app and the MySQL service by running:
`docker-compose up`
This command will start both containers (Flask and MySQL), and they should be able to communicate with each other.
```
```
Once both containers are running, open your browser and go to http://localhost:5000.
The Flask app should now be able to connect to the MySQL database successfully
```
But you will see empty messag []
```
```
# 5: Add Data to the Database via the /add-message Route
```
You need to initialize the database and ensure the messages table is created by running:
curl http://localhost:5000/init-db
```
`Open a New Terminal:
Navigate to Your Project Directory 
cd ~/simple-docker-app`

```
In the new terminal, run the following command to initialize the database and create the table:

curl http://localhost:5000/init-db
```
```
After initializing the database, you can add a message using the following curl command:
curl -X POST http://localhost:5000/add-message -H "Content-Type: application/json" -d '{"content":"Hello from Docker!"}'
```
![Capture d’écran 2024-09-04 201538](https://github.com/user-attachments/assets/d4f0c13f-01a4-473b-8376-5d80144ff6f3)

