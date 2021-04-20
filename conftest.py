from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose user's language")

@pytest.fixture(scope="function")
def browser(request):
    language_test=request.config.getoption("language")
    options=Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_test})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()