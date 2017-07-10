from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='#(8a3qv469n_khn3gv6$t1(l0&74u)84pfu2bf78s6##@ntxdu')
DEBUG = env.bool('DJANGO_DEBUG', default=True)

# ALLOWED_HOSTS is the list of sites that Django will accept to make connection and requests.
# For local development when DEBUG is True, we can have this be empty, 
# however, when in production it must be set to a specific domain such as .example.com