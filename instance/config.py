# instance/config.py
import os
class Config():
    DEBUG=False
    SECRET_KEY=os.getenv("JWT_SECRET_KEY") 

class DevelopmentConfig(Config):
    """Enable our debug mode to True in development in order to auto restart our server on code changes"""
    DEBUG = True
    DATA_BASE_URL=os.getenv("DATABASE_URL")

    

class TestingConfig(Config):
    """Testing app configurations"""
    TESTING = True
    DEBUG = True
    DATABASE_URL=os.getenv("TEST_DATABASE_URL")
    
    
class ReleaseConfig(Config):
    """Releasing app configurations"""
    DEBUG = False
    TESTING = False


app_configuration={
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'release': ReleaseConfig,
}
