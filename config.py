import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '03c56480246d027a6919de61f2b8727c'
