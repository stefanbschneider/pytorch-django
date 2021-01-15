""" Production Settings """
# default: use settings from main settings.py if not overwritten
from .settings import *


############
# SECURITY #
############

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = ['pytorch-django.herokuapp.com']
