import string
import http.client

from typing import Optional
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from topdrawersoccer.models.transfer import Transfer

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
    :return:
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
    :return:
    """
    name_field = name_field.strip()

    if len(name_field) == 0:
        return ""

    tokens = name_field.split(" ")
    name = " ".join(tokens[1:])

    return name


def extract_player_id(player_url: str) -> int:
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


class TransferExtractor:
    url: str

    def __init__(self, url = None):
        if url is None:
            url = DEFAULT_URL

        self.url = url

    def fetch_page(self):
        url_parts = urlparse(self.url)
        conn = http.client.HTTPSConnection(url_parts.netloc)
        conn.request("GET", url_parts.path)
        response = conn.getresponse()

        if response.status != 200:
            raise Exception(f"Failed to fetch page, status code: {response.status}")

        html = response.read().decode('utf-8')
        conn.close()
        return html

    def parse_page(self, html):
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

    def extract(self):
        html = self.fetch_page()
        return self.parse_page(html)

    def get_transfer_colleges(self) -> list[str]:
        college_transfer_players = self.get_transfer_players()

        college_names = set()
        for current_transfer in college_transfer_players:
            college_name = current_transfer.incoming_college_name
            if college_name not in college_names:
                college_names.add(college_name)

            college_name = current_transfer.outgoing_college_name
            if college_name not in college_names:
                college_names.add(college_name)

        return list(college_names)

    def get_outgoing_transfer_colleges(self) -> list[str]:
        college_transfer_players = self.get_transfer_players()

        college_names = set()
        for current_transfer in college_transfer_players:
            college_name = current_transfer.outgoing_college_name
            if college_name not in college_names:
                college_names.add(college_name)

        return list(college_names)

    def get_incoming_transfer_colleges(self) -> list[str]:
        college_transfer_players = self.get_transfer_players()

        college_names = set()
        for current_transfer in college_transfer_players:
            college_name = current_transfer.incoming_college_name
            if college_name not in college_names:
                college_names.add(college_name)

        return list(college_names)

    def get_transfer_players(self) -> list[Transfer]:
        html = self.fetch_page()
        return self.parse_page(html)


if __name__ == "__main__":
    extractor = TransferExtractor()
    transfers = extractor.extract()
    for transfer in transfers:
        print(transfer)
