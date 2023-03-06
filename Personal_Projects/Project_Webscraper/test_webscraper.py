from Project_Webscraper.webscraper import get_website_contents

# Remember to use 'assert' syntax
def test_get_website_content():
    assert get_website_contents('https://en.wikipedia.org/wiki/United_Kingdom')

def test_fail_get_website_content():
    assert get_website_contents('sample_fail_test')