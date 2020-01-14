from project.app import app


# gunicorn --bind 0.0.0.0:5000 'project:load_app("dick")'
# gunicorn --bind 0.0.0.0:5000 'project:load_app()'
def my_app(x):
    print(x)
    app.run()


def load_app(x):
    return my_app(x)
