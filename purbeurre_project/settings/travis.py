#settings for Travis
import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['46.101.143.60']

SECRET_KEY = os.environ.get('SECRET_KEY', "Q'F?Z'L2?fbgT_-HH${TaZB4")
