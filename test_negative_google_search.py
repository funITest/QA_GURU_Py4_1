import pytest
from selene.support.shared import browser, config
from selene import be, have

@pytest.fixture
def open():
    browser.open('https://google.com')

@pytest.fixture
def brauser_size(open):
    config.browser_size = 1920, 1080

@pytest.fixture
def brauser_search(brauser_size, open):
    browser.element('[title="Поиск"]').should(be.blank).type('yashaka/selene').press_enter()


#def test_google_search(brauser_search, brauser_size, open):
 #   browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative_google_search(brauser_search, brauser_size, open):
    browser.element('[id="search"]').should(have.text('minecraft'))
