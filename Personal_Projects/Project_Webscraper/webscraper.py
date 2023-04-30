from bs4 import BeautifulSoup
import lxml
import requests

from dataclasses import dataclass
import pandas as pd

@dataclass
class StatisticsData:
    demographic_count: int
    demographic_percentage: float
    demographic_label: str


    pass


# @dataclass
# class SampleHTML:
#
#     def __init__(self):


def get_website_contents(website_url: str):
    web_response = requests.get(website_url, timeout=5)
    website_content = BeautifulSoup(web_response.content, 'html.parser')
    content_body = website_content.findAll('div', class_="mw-content-container")
    print(content_body)
    return content_body


def create_sample_html_page():
    pass


def process_html_data():
    pass


def visualise_processed_statistics_data():
    pass