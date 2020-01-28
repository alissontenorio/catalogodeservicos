import os


class Config(object):
    #print('test2e')
    #SECRET_KEY = os.environ.get(str(os.urandom(32))) or 'you-will-never-guess'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    WTF_CSRF_SECRET_KEY = "a csrf secret key"