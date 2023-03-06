from bs4 import BeautifulSoup
import lxml
import requests

def get_website_contents(website_url: str):
    web_response = requests.get(website_url, timeout=5)
    website_content = BeautifulSoup(web_response.content, 'html.parser')
    content_body = website_content.findAll('div', class_="mw-content-container")
    print(content_body)
    return content_body

