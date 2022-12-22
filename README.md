
# Beginner guide to flask application
# Find at Medium blog
 - [Create your first Flask application - 1](https://medium.com/@Satyam_Mishra/create-your-first-flask-application-48a698b524ca)
 - [Structuring flask application for multiple apps - 2](https://medium.com/@Satyam_Mishra/structuring-flask-application-for-multiple-apps-part-2-79eefca094de)


# Structuring flask application for multiple apps
Flask, being a lightweight Python backend development framework, can be structured into really good and optimized applications that can even compete with Django (the high-level framework). Flask gives us the freedom to resize our projects and applications depending on our needs. Unlike Django, which is already scaled to produce huge apps right away, Flask should be properly structured to do the same.

( Blueprint meaning - blueprints in flask mean collection of application inside an complex application. For blueprints to work in flask we must add each collection to the main application. Each blueprints can contains it’s own files such as static, templates, and views. )

However, for the time being, we will not separate the static and template files.

As we completed the first part of this blog, in which we created three redirecting pages named "home," "about and "contact," Now we are going to structure those using blueprints.

For that, we will start by creating a new folder named "apps" in the main directory, something like below.

https://miro.medium.com/max/532/1*zM-VbW_rggX5u3qyQU3tQQ.webp

And then create **init.py and** **main.py** inside the apps folder.

**init.py`**

  

In init.py, we need to create a function that will collect and combine all the blueprints and create a single application from them.

```python
def create_app():
    """Create Flask application."""
    name = "Medium blog example"
    app = Flask(name, instance_relative_config=False)
```

Then add all the separate apps as a blueprint

```python
with app.app_context():
        # Import parts of our application
        from . import main
        
        # Register Blueprints
        app.register_blueprint(main.main)
        # returning app
        return app
```

So the final [init.py](http://init.py) should be something of this kind.

```python
# init.py

from flask import Flask
from . import config

def create_app():
    """Create Flask application."""
    name = "Medium blog example"
    app = Flask(name, instance_relative_config=False)
    # selecting config file for application to run
    # Basic config, Dev, and Prod
    app.config.from_object(config.ProdConfig)

    with app.app_context():
        # Import parts of our application
        from . import main
        
        # Register Blueprints
        app.register_blueprint(main.main)
        # returning app
        return app
```

That config.ProdConfig is a configuration file that will change the application's configuration to either production or development. This should be put in the apps folder. Just change config.ProdConfig to config.DevConfig while deploying your application.

Here’s the code for that file.

```python
# config.py

"""Flask configuration."""

class Config:
    """Base config."""
		# secret_key of your liking
    SECRET_KEY = 'jhsd]e[398XXXXXXXXXXXXXXXXXXXXXXX'

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
```

Rename app.py to wsgi.py and write the code to run our application.

```python
# wsgi.py

from apps import init

if __name__ == "__main__":
    app = init.create_app()
    app.run()
```

Now that all of the main files have been touched, only main.py remains, which will contain specific routes to itself.

Firstly, we must define the blueprint name inside main.py.

```python
from flask import Blueprint, render_template

# Blueprint Configuration adding to main app
main = Blueprint(
    'main', __name__,
)
```

and then we add the routes specific to this file.

In our case, I will just add all the routes from the last tutorial.

```python
@main.route("/")
def home():
    # you can return using this command:
    return render_template("home.html")

# same way you can create multiple points

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")
```

After editing, it should look like this:

```python
# main.py

from flask import Blueprint, render_template

# Blueprint Configuration adding to main app
main = Blueprint(
    'main', __name__,
)

@main.route("/")
def home():
    # you can return using this command:
    return render_template("home.html")

# same way you can create multiple points

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")
```

I have used several files from my last blog.

Now your file structure should look something like this:

https://miro.medium.com/max/498/1*jKnVEpsxjnN_D8AcFyiKGA.webp

Let’s try running our application now.

https://miro.medium.com/max/640/1*JbMqzl4czdaCZjxRjfmPkw.webp
https://miro.medium.com/max/640/1*FoTEYWvbl5rPLxiQErbsHg.webp

and our application still works the same, but is more developmentally clean and easy to recap.

# Authors
- [@Satyam Mishra](https://www.github.com/bedead)

# 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](http://satyammishra.ga/)
