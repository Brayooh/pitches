import os
from dotenv import load_dotenv as ld

ld()


class Config:
    # SQLALCHEMY_DATABASE_URI = "postgresql://brayooh:brian@localhost/pitch"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'qwertyuiop'

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    DEBUG = True
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://brayooh:brian@localhost/pitch"

    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://brayooh:brian@localhost/pitch"

    

config_options = {
   'development': DevConfig,
   'production': ProdConfig,
   'test': TestConfig
}




