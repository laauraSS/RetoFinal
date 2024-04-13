import os


class Config:
    # Secret key for the Flask app
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Add other configuration variables as needed


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI + "/mydatabase"


class ProductionConfig(Config):
    DEBUG = False
    # Add other production configurations here

class TestingConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI + "/testmydatabase"
    

# Dictionary to map environment names to configuration classes
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    # Add other environments if needed
    "testing": TestingConfig,
}
