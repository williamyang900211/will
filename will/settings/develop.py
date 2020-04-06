from .base import *  # NOQA
DEBUG = True
SECRET_KEY= 'riad4=+&#p=)-$mm(1^)x^u*bb1uj+6mj1y+8mm(!aypvk@ga)'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}