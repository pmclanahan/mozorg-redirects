"""Test urls from the simple 301 and 410 text files in the .com repo."""

from base import assert_response


# uses pytest fixtures found in conftest.py

def test_simple_maps(simple_url):
    if isinstance(simple_url, basestring):
        # if a single value, it's a 410
        assert_response(simple_url, 410)
    else:
        # otherwise it's a tuple and is a redirect
        assert_response(simple_url[0], 200, simple_url[1])
