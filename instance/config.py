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
    DATABASE_URL="postgres://ldgwxvtdhujucr:d8b43e6d977939322a641322dbd44f5a8a9a9f4d6d67a710bb7bb83fa01e6e26@ec2-54-243-46-32.compute-1.amazonaws.com:5432/d73r5i57ko6q1p"
    


app_configuration={
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'release': ReleaseConfig,
}
