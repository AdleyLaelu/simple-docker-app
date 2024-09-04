# simple-docker-app
Will Create and deploy a two-part web application: a backend written in Python (Flask) and a MySQL database. Will use Docker to containerize these two services and Docker Compose to orchestrate their deployment

# STEP 1 Creating the Dockerfile in the directory where you files are found

1)
  ``` `touch Dockerfile`

Use an official Python runtime as a parent image, This specifies the base image for the container, which is a lightweight Python 3.8 environment.
```FROM python:3.8-slim```

Set/Create the working directory in the container
`WORKDIR /app`

Copy the current directory contents into the container, This copies everything in your local directory (including app.py and requirements.txt) into the /app directory in the container
`COPY . /app`

Install any needed packages specified in requirements.txt, This installs the dependencies listed in requirements.txt inside the container
`RUN pip install --no-cache-dir -r requirements.txt`

Make port 5000 available to the outside world
`EXPOSE 5000`

Run app.py when the container launches
`CMD ["python", "app.py"]`
```
