import pytest
from selene.support import shared
from selene.support.shared import browser, config
from selene import be, have


@pytest.fixture
def open_browser():
    browser = shared.browser.with_(window_width=2100)




