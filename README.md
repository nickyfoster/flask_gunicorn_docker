# Flask Gunicorn Docker Template

This is a template project that helps you easily build and deploy Python services using Flask, Gunicorn, and Docker.

##Getting Started

To get started, clone the repository and install required python modules :
```
git clone https://github.com/nickyfoster/flask-gunicorn-docker-template.git
cd flask-gunicorn-docker-template
pip install -r requirements.txt
```

## Customizing the app

To customize the app, simply edit the app.py file and add your desired routes and functionality. 
You can also add additional Python packages to the **requirements.txt** file and they will be installed when the Docker image is built.

## Build the Docker image
To build your project simply run `build.sh`

## Run the Docker container
For both starting and restarting use `restart.sh`

This will start the app in a Docker container and make it available at http://localhost:5000.


## License

[MIT](https://choosealicense.com/licenses/mit/)
