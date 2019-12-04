import re
from hashlib import md5

from pyhashxx import hashxx

from memcachedkeys.pkgmeta import *


bad_key_chars = re.compile(r'[\u0000-\u001f\s]+')
MAX_LENGTH = 250


def make_key_md5(key, key_prefix, version):
    """
    Makes a memcached-safe cache key using md5. Use as a KEY_FUNCTION

    """
    clean_key = bad_key_chars.sub('', key)
    version_str = str(version)
    full_key = ':'.join([key_prefix, version_str, clean_key])

    if clean_key != key or len(full_key) > MAX_LENGTH:
        hashed_key = md5(key).hexdigest()
        abbrev_keylen = MAX_LENGTH - len(hashed_key) - len('::[]') - len(key_prefix) - len(version_str)
        new_key = '%s[%s]' % (clean_key[:abbrev_keylen], hashed_key)
        full_key = ':'.join([key_prefix, version_str, new_key])

    return full_key


def make_key(key, key_prefix, version):
    """
    Makes a memcached-safe cache key using pyhashxx. Use as a KEY_FUNCTION

    """
    clean_key = bad_key_chars.sub('', key)
    full_key = '%s:%s:%s' % (key_prefix, version, clean_key)

    if clean_key != key or len(full_key) > MAX_LENGTH:
        hashed_key = str(hashxx(key))
        abbrev_keylen = MAX_LENGTH - len(hashed_key) - 4 - len(key_prefix) - len(str(version))
        new_key = '%s[%s]' % (clean_key[:abbrev_keylen], hashed_key)
        full_key = '%s:%s:%s' % (key_prefix, version, new_key)

    return full_key
