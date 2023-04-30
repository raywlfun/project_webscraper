import re

from bs4 import BeautifulSoup
from Personal_Projects.Project_Webscraper.sample_html import html_page_information, write_to_html_file
import lxml
import os
import requests

from dataclasses import dataclass
import pandas as pd
import html5lib


# TODO: Encapsulate results of webscraped data to this dataclass
@dataclass
class ContinentData:
    name: str
    population: int
    mean_push_ups: int


# with open(write_to_html_file(html_page_information)) as file:
#     fabricated_html_data = file.read()


# Establish whether the input to be read is a filepath or url
def read_html_content(html_url_or_filepath: str) -> str:
    if os.path.isfile(html_url_or_filepath):
        with open(html_url_or_filepath, 'r') as file:
            html_content = file.read()
            print('FILE READ')
    else:
        try:
            web_response = requests.get(html_url_or_filepath, timeout=5)
            html_content = web_response.content
            print('URL READ')
        except requests.exceptions.InvalidSchema:
            print(f'Invalid URL @ {html_url_or_filepath}: failed to retrieve data')
            return None
    return html_content


def parse_html_content(html_content: str) -> BeautifulSoup:
    return BeautifulSoup(html_content, 'html.parser')


def find_statistics_divs(page_content: BeautifulSoup) -> list:
    return page_content.findAll('div', class_='Fabricated_statistics')



def get_website_contents(html_url_or_filepath: str):
    html_content = read_html_content(html_url_or_filepath)
    if html_content is not None:
        page_content = parse_html_content(html_content)
        content_body = find_statistics_divs(page_content)
        print(content_body)
        return content_body
    else:
        return None


raw_webscraped_data = get_website_contents('sample_page.html')


# Remove HTML tags from webscraped data

def clean_webscraped_data(webscraped_data: str) -> list:
    """
    Personal learning note: Using re(.findall, .sub) to extract all numeric strings / replace all occurrences of a string by the string replacement
    Personal research indicates this is a conventional way of removing html tags and unwanted formatting like commas, to acquire just the numerical data.
    re = regular expression --> Regex
    """
    cleaned_data = []
    numerical_strings = re.findall(r'\d+', webscraped_data)
    for numerical_string in numerical_strings:
        cleaned_numerical_string = re.sub(r'<.*?>', '', numerical_string)
        cleaned_data.append(int(cleaned_numerical_string)) # Convert str to int

    return cleaned_data

clean_webscraped_data(raw_webscraped_data)