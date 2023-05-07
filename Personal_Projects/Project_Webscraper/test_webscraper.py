from io import StringIO
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
from Personal_Projects.Project_Webscraper.webscraper import (
    read_html_content,
    parse_html_content,
    find_statistics_divs,
    clean_webscraped_data,
)

TEST_HTML_DATA = '''
    <html>
        <head>
            <title>Test HTML page</title>
        </head>
        <body>
            <div class="Fabricated_statistics">
                <p> This is some content </p>
            </div>
        </body>
    </html>
'''


# TODO: Mock requests.get with @patch, mock its return value, assert the result == expected result
@patch('requests.get')
def test_read_html_content_if_url(mock_request_get):
    """
    Because the requests.get call is being mocked, look to return the correct type of the contents being webscraped
    In this case, requests.get should return the contents of a webpage as bytes, so we try to encode the test html data
    :param mock_request_get:
    :return:
    """

    # Instantiate the mocked requests.get
    mock_response = Mock()

    # Encode typing to bytes
    mock_response.content = TEST_HTML_DATA.encode()
    mock_request_get.return_value = mock_response

    html_content = read_html_content('https://example.com')
    decoded_html_content = html_content.decode()
    print(decoded_html_content)
    assert decoded_html_content is not None, 'Failed to read content from URL'
    assert decoded_html_content == TEST_HTML_DATA, 'HTML CONTENT does not match test html data'


@patch('builtins.open')
def test_read_html_content_if_file(mock_file_open):
    """
    mock the file open function
    :param mock_file_open:
    :return:
    """
    mock_file_open.return_value = StringIO(TEST_HTML_DATA)

    html_content = read_html_content('sample_page.html')
    assert html_content is not None
    assert html_content == TEST_HTML_DATA
    mock_file_open.assert_called_with('sample_page.html', 'r')


def test_parse_html_content():
    html_content = parse_html_content(TEST_HTML_DATA)

    assert html_content is not None, 'Failed to parse HTML content'
    assert isinstance(html_content, BeautifulSoup), 'PARSED HTML is returned as a BeautifulSoup Object'
    # Verify structure of the html page
    title_html_tag = html_content.find('title')
    div_html_tag = html_content.find('div', class_='Fabricated_statistics')
    if div_html_tag:
        paragraph_html_tag = html_content.find('p')
    else:
        paragraph_html_tag = None

    assert title_html_tag is not None and title_html_tag.text == 'Test HTML page', 'Title tag content does not match TEST HTML Page'
    assert div_html_tag is not None, 'Div tag for class Fabricated_statistics is not found'
    assert paragraph_html_tag is not None and paragraph_html_tag.text == ' This is some content ', 'Paragraph tag content does not match'

# TODO: Test functions for: find_statistics_divs, extract_numerical_data_from_statistics_divs
# TODO: Test function for clean_webscraped_data?
#  Assess whether this is necessary, as it's essentially a calling function. Seems like a good idea (integration test?)

