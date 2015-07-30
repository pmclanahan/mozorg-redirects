from itertools import chain

import pytest

from map_301 import URLS_301_MAP
from map_410 import URLS_410


@pytest.fixture(params=chain(URLS_410, URLS_301_MAP))
def simple_url(request):
    return request.param
