"""Flask configuration."""


class Config:
    """Base config."""
    SECRET_KEY = '}][}[[.&6s'


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
