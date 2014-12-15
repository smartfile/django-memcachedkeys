=============================
django-memcachedkeys
=============================

Memcached has some weird rules about its keys. Ignore them and you'll get an
error like "MemcachedKeyCharacterError: Control characters not allowed". So
install this.


Quickstart
----------

Install django-memcachedkeys::

    pip install django-memcachedkeys

Then use it in your settings file::

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'KEY_PREFIX': 'whatever',
            'KEY_FUNCTION': 'memcachedkeys.make_key',
        }
    }
    
By default, pyhashxx is used to sanitize keys. To use a different backend::

    'KEY_FUNCTION': 'memcachedkeys.make_key_md5',
