"""
This module contains the TransferExtractor class, which is responsible for extracting transfer tracker data from the
"""

import string

from typing import Optional
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from topdrawersoccer.models.transfer import Transfer
from topdrawersoccer.extractors.base_extractor import BaseExtractor

ENDPOINT = "https://www.topdrawersoccer.com"
DEFAULT_URL = urljoin(ENDPOINT, "/college-soccer-articles/2024-womens-division-i-transfer-tracker_aid52845")


def replace_nbsp(text: str) -> str:
    """
    Replaces non-breaking space characters with regular spaces.

    :param text: The input text.
    :return: The cleaned text.
    """
    text = text.replace('\u00A0', ' ')
    text = text.replace('\xa0', ' ')

    return text


def get_position(name_field: str) -> Optional[str]:
    """
    This function extracts the position from the name field.

    :param name_field:
    :return: The position.
    """
    name_field = name_field.strip()
    name_field = replace_nbsp(name_field)

    if len(name_field) == 0:
        return None

    tokens = name_field.split(" ")
    position = tokens[0]

    return position


def get_name(name_field: str) -> Optional[str]:
    """
    This function extracts the name from the name field.

    :param name_field:
    :return: The name.
    """
    name_field = name_field.strip()

    if len(name_field) == 0:
        return ""

    tokens = name_field.split(" ")
    name = " ".join(tokens[1:])

    return name


def extract_player_id(player_url: str) -> int:
    """
    This function extracts the player ID from the player URL.

    :param player_url: The player URL.
    :return: The player ID.
    """
    if player_url:
        return int(player_url.split('/')[-1].split('-')[-1])
    return 0


def get_last_name(full_name: str) -> str:
    """
    This function extracts the last name from the full name.

    :param full_name:
    :return:
    """
    return full_name.split(" ")[-1]


def remove_non_printable_chars(text: str) -> str:
    """
    Removes non-printable characters from the given text.

    :param text: The input text.
    :return: The cleaned text.
    """
    return ''.join(filter(lambda x: x in string.printable, text))


class TransferExtractor(BaseExtractor):
    def __init__(self, url: str = None):
        super().__init__(url or DEFAULT_URL)

    def parse_page(self, html) -> list[Transfer]:
        """
        This function parses the transfer tracker page.

        :param html: The HTML content of the transfer tracker page.
        :return: The transfer tracker data.
        """
        soup = BeautifulSoup(html, 'html.parser')
        transfer_list = []

        # Example: Assume transfers are listed in a table with the class 'transfer-table'
        table = soup.find('table', {'border': '5'})
        rows = table.find_all('tr')[1:]  # Skip the header row

        for row in rows:
            cols = row.find_all('td')

            name_field = cols[0].text.strip()
            name_field = replace_nbsp(name_field)

            if len(name_field) == 0:
                continue

            position = get_position(name_field)
            player_name = get_name(name_field)
            player_url = cols[0].find('a')['href'] if cols[0].find('a') else None

            if player_url:
                player_id = extract_player_id(player_url)
            else:
                player_id = 0

            from_team = cols[1].text.strip()
            from_team_url = cols[1].find('a')['href'] if cols[1].find('a') else None

            to_team = cols[2].text.strip()
            to_team_url = cols[2].find('a')['href'] if cols[2].find('a') else None

            current_transfer = Transfer(
                id=player_id,
                url=urljoin(ENDPOINT, player_url) if player_url else None,
                name=player_name,
                position=position,
                outgoing_college_name=from_team,
                outgoing_college_url=urljoin(ENDPOINT, from_team_url) if from_team_url else None,
                incoming_college_name=to_team,
                incoming_college_url=urljoin(ENDPOINT, to_team_url) if to_team_url else None,
            )

            transfer_list.append(current_transfer)

        # Sort the transfer list by last name, then by first name
        transfer_list.sort(key=lambda x: (get_last_name(x.name), x.name))

        return transfer_list

    def extract(self) -> list[Transfer]:
        """
        This function extracts the transfer tracker data.

        :return: The transfer tracker data.
        """
        return self.parse_page(self.fetch_page())

    def get_transfer_colleges(self) -> list[str]:
        """
        This function returns the transfer colleges.

        :return: The transfer colleges.
        """
        college_transfer_players = self.get_transfer_players()

        college_names = set()
        for current_transfer in college_transfer_players:
            college_name = current_transfer.incoming_college_name
            if college_name not in college_names:
                college_names.add(college_name)

            college_name = current_transfer.outgoing_college_name
            if college_name not in college_names:
                college_names.add(college_name)

        college_name_list = list(college_names)
        college_name_list.sort()

        return college_name_list

    def get_outgoing_transfer_colleges(self) -> list[str]:
        """
        This function returns the outgoing transfer colleges.

        :return: The outgoing transfer colleges.
        """
        college_transfer_players = self.get_transfer_players()

        college_names = set()
        for current_transfer in college_transfer_players:
            college_name = current_transfer.outgoing_college_name
            if college_name not in college_names:
                college_names.add(college_name)

        college_name_list = list(college_names)
        college_name_list.sort()

        return college_name_list

    def get_incoming_transfer_colleges(self) -> list[str]:
        """
        This function returns the incoming transfer colleges.

        :return: The incoming transfer colleges.
        """
        college_transfer_players = self.get_transfer_players()

        college_names = set()
        for current_transfer in college_transfer_players:
            college_name = current_transfer.incoming_college_name
            if college_name not in college_names:
                college_names.add(college_name)

        college_name_list = list(college_names)
        college_name_list.sort()

        return college_name_list

    def get_transfer_players(self) -> list[Transfer]:
        """
        This function returns the transfer players.

        :return: The transfer players.
        """
        return self.parse_page(self.fetch_page())
