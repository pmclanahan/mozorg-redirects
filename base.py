from urlparse import urljoin

import requests
from decouple import config


BASE_URL = config('MOZORG_URL', 'https://www.mozilla.org')


def assert_response(url, status_code=200, location=None):
    """
    Request a url and assert things about the response.
    :param url: the URL to test. relative url will be added to BASE_URL.
    :param status_code: expected response code.
    :param location: expected location header if redirect.
    """
    full_url = urljoin(BASE_URL, url)
    print 'Test URL:', full_url
    resp = requests.head(full_url, allow_redirects=True)
    assert resp.status_code == status_code
    if location:
        assert resp.url == location
