# from __future__ import annotations # In lieu of using Optional type hint, import this to use | syntax
from typing import List, Optional

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


def read_html_content(html_url_or_filepath: str) -> Optional[str]:
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


def find_statistics_divs(page_content: BeautifulSoup) -> List[str]:
    return page_content.findAll('div', class_='Fabricated_statistics')


def extract_numerical_data_from_statistics_divs(divs: List[str]) -> List[int]:
    numerical_data = []

    for div in divs:
        numerical_string = re.findall(r'\d+', str(div))  # Convert div from beautifulsoup object to str
        numerical_data.extend(int(content_string) for content_string in numerical_string)
    return numerical_data


def clean_webscraped_data(page_content: BeautifulSoup) -> List[int]:
    """
    Personal learning note: Using re(.findall, .sub) to extract all numeric strings / replace all occurrences of a string by the string replacement
    Personal research indicates this is a conventional way of removing html tags and unwanted formatting like commas, to acquire just the numerical data.
    re = regular expression --> Regex
    """

    statistics_divs = find_statistics_divs(page_content)

    cleaned_data = extract_numerical_data_from_statistics_divs(statistics_divs)

    return cleaned_data


html_content = read_html_content('sample_page.html')
raw_webscraped_data = parse_html_content(html_content)
cleaned_data = clean_webscraped_data(raw_webscraped_data)

print(cleaned_data)

# TODO: Reformat html data cleaning to also return relevant data pertaining to ContinentData dataclass.
#  Currently, it only returns the numerical data