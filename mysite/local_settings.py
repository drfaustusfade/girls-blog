
# local postgres
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'postgres',
    'USER': 'postgres',
    'HOST': 'db',
    'PORT': '5432',
    }
}

# # heroku settings
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DEBUG = True
