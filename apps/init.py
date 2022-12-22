# @author Satyam Mishra

from flask import Flask
from . import config


def create_app():
    """Create Flask application."""
    name = "Beginner guide to flask application."
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
