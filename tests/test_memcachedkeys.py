from memcachedkeys import make_key


def test_short():
    """ Test short keys. These keys don't require sanitizing. """
    key = 'A' * 241
    full_key = 'prefix:1:%s' % key
    assert full_key == make_key(key, 'prefix', 1)


def test_long():
    """ Test long keys, which will need to be sanitized. """
    key = 'A' * 242
    hashed_key = '%s[3705915182]' % ('A' * 229)
    full_key = 'prefix:1:%s' % hashed_key
    assert full_key == make_key(key, 'prefix', 1)


def test_space():
    """ Test for spaces in keys, which will need to be sanitized. """
    assert make_key('hello world', 'prefix', '1') == 'prefix:1:helloworld[3468387874]'
