"""
This module contains utility functions for extracting information from URLs.
"""

import re

from urllib.parse import urlparse, parse_qs


def extract_id_from_url(url: str) -> int:
    """
    Extracts the conference ID from the given URL.

    :param url: The URL containing the conference ID.
    :return: The extracted conference ID.
    """
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # Check for query parameters ending with 'Id'
    for key, value in query_params.items():
        if key.endswith('Id') and value[0].isdigit():
            return int(value[0])

    # Fallback to regex-based extraction
    match = re.search(r'[-](\d+)', url)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"ID not found in URL: {url}")


def extract_gender_from_url(url: str) -> str:
    """
    Extract the gender from a URL

    :param url: The URL to extract the gender from
    :return: the gender string
    """
    # https://www.topdrawersoccer.com/college-soccer/college-soccer-details/women/albany/clgid-6
    if '/women/' in url:
        return "Women's"
    elif '/men/' in url:
        return "Men's"
    else:
        raise ValueError(f"Gender not found in URL: '{url}'")


def extract_division_from_url(url: str) -> str:
    """
    Extract the division from a URL

    :param url: The URL to extract the division from
    :return: the division string
    """
    # https://www.topdrawersoccer.com/college/teams/?divisionName=di&divisionId=1
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    division_name = query_params.get('divisionName', [None])[0]

    if not division_name:
        raise ValueError(f"Division not found in URL: '{url}'")

    division_name = division_name.upper()

    return division_name

