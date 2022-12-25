# Flask Gunicorn Docker Template

This is a template project that helps you easily build and deploy Python services using Flask, Gunicorn, and Docker.
Getting Started

To get started, clone the repository and install the dependencies:
```
git clone https://github.com/nickyfoster/flask-gunicorn-docker-template.git
cd flask-gunicorn-docker-template
pip install -r requirements.txt
```

Next, you will need to create a **.env** file with the following contents:

FLASK_APP=app
FLASK_ENV=development

This specifies the Flask app and the environment in which it should run.
Running the app locally

To run the app locally, simply use the Flask development server:

flask run

This will start the server at http://localhost:5000.
Building and deploying the app with Docker

To build and deploy the app using Docker, you'll need to have Docker installed on your machine. Then, run the following commands:

# Build the Docker image
docker build -t <your_username>/flask-gunicorn-docker-template .

# Run the Docker container
docker run -p 5000:5000 <your_username>/flask-gunicorn-docker-template

This will start the app in a Docker container and make it available at http://localhost:5000.
Customizing the app

To customize the app, simply edit the app.py file and add your desired routes and functionality. You can also add additional Python packages to the requirements.txt file and they will be installed when the Docker image is built.
Credits

This template project was created by <your_name>.