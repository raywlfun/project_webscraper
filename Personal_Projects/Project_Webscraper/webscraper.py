from bs4 import BeautifulSoup
from Personal_Projects.Project_Webscraper.sample_html import html_page_information, write_to_html_file
import lxml
import requests

from dataclasses import dataclass
import pandas as pd


# TODO: Encapsulate results of webscraped data to this dataclass
@dataclass
class ContinentData:
    name: str
    population: int
    mean_push_ups: int


with open(write_to_html_file(html_page_information)) as file:
    fabricated_html_data = file.read()


def get_website_contents(html_url_or_filepath: str):
    try:
        web_response = requests.get(html_url_or_filepath, timeout=5)
        page_content = BeautifulSoup(web_response.content, 'html.parser')
    except requests.exceptions.InvalidSchema:
        page_content = BeautifulSoup(html_url_or_filepath, 'html.parser')
        print('No web response')
    content_body = page_content.findAll('div', class_="Fabricated_statistics")
    print(content_body)
    return content_body


get_website_contents(fabricated_html_data)


def create_sample_html_page():
    pass


def process_html_data():
    pass


def visualise_processed_statistics_data():
    pass
