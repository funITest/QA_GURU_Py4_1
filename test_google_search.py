import pytest
from selene.support import shared
from selene import be, have, browser
from selene.support.conditions.be import existing


@pytest.fixture
def open_browser():
    shared.browser.with_(window_width=1920, window_height=1080)


def test_google_search(open_browser):
    browser.open('https://www.google.com/search?q=yashaka%2Fselene')
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_google_search(open_browser):
    browser.open('https://www.google.com/search?q=12345678234567890323456789098765432134567898')
    browser.element('#appbar').should(have.text('Результатов: примерно 0'))
    browser.element('#res').should(have.text(' ничего не найдено. '))
