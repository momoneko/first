# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

DATABASES = {
    'default': {
        # Replace with database backend which you'll use
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
