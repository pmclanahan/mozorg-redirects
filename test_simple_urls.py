"""Test urls from the simple 301 and 410 text files in the .com repo."""

from base import assert_response
from map_301 import URLS_301_MAP
from map_410 import URLS_410


def test_410s():
    for url in URLS_410:
        yield assert_response, url, 410


def test_301s():
    for url, dest in URLS_301_MAP:
        yield assert_response, url, 200, dest
