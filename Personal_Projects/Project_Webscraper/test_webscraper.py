import pytest
from Project_Webscraper.webscraper import (
    get_website_contents,
    create_sample_html_page,
    process_html_data,
)

# Remember to use 'assert' syntax


def test_get_website_content():
    assert get_website_contents('https://en.wikipedia.org/wiki/United_Kingdom')

def test_fail_get_website_content():
    assert get_website_contents('sample_fail_test')


def test_create_html_page():
    pass


# TODO: patch get website content function; add side effect and simulate 3x instances of different html data
@pat
def test_process_html_data():
    pass