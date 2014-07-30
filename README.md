#  Askari [![Build Status](https://travis-ci.org/devton/askari-python.svg?branch=master)](https://travis-ci.org/devton/askari-python) [![Coverage Status](https://coveralls.io/repos/devton/askari-python/badge.png?branch=master)](https://coveralls.io/r/devton/askari-python?branch=master) [![Code Health](https://landscape.io/github/devton/askari-python/master/landscape.png)](https://landscape.io/github/devton/askari-python/master)

## Installation
First certify that you have the required stack:

 * Python >= 3.4
 * pip
 * PostgreSQL

After setting up your environment (using pyenv, brew, ports, apt-get or whatever floats your boat) you can run pip to install the requirements:

    pip install -r askari/requirements.txt -r askari/requirements_dev.txt

If you need to overide the default database settings just create a file ```askari/local_settings.py``` with the content:

```python
    from .settings import *


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'askari_development',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'diogo',
            'PASSWORD': '',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }
```

Then you can create a database called ```askari_development``` using the syncdb command and the database objects with the migrate:

    python ./manage.py syncdb --settings=askari.local_settings
    python ./manage.py migrate --settings=askari.local_settings

