import re

from urllib.parse import urljoin
from typing import Optional

from bs4 import BeautifulSoup

from topdrawersoccer.models.conference import Conference
from topdrawersoccer.extractors.base_extractor import BaseExtractor

ENDPOINT = "https://www.topdrawersoccer.com"
DIVISIONS = ["DI", "DII", "DIII", "NAIA", "NJCAA"]

def extract_conference_id(url: str) -> int:
    """
    Extracts the conference ID from the given URL.

    :param url: The URL containing the conference ID.
    :return: The extracted conference ID.
    """
    match = re.search(r'cfid-(\d+)', url)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"Conference ID not found in URL: {url}")


def get_url_by_division(division: str) -> str:
    """
    This function returns the URL for the transfer tracker by division.

    :param division: The division of the transfer tracker.
    :return: The URL for the transfer tracker.
    """
    url = None

    if division == "DI":
        url = urljoin(ENDPOINT, url="/college-soccer/college-conferences/di/divisionid-1")
    elif division == "DII":
        url = urljoin(ENDPOINT, url="/college-soccer/college-conferences/dii/divisionid-2")
    elif division == "DIII":
        url = urljoin(ENDPOINT, url="/college-soccer/college-conferences/diii/divisionid-3")
    elif division == "NAIA":
        url = urljoin(ENDPOINT, url="/college-soccer/college-conferences/naia/divisionid-4")
    elif division == "NJCAA":
        url = urljoin(ENDPOINT, url="/college-soccer/college-conferences/njcaa/divisionid-5")
    else:
        raise ValueError(f"Unsupported division: {division}")

    return url


class ConferenceExtractor(BaseExtractor):
    division: str

    def __init__(self, division: str):
        super().__init__(get_url_by_division(division))
        self.division = division

    def parse_page(self, html: str) -> list[Conference]:
        """
        This function parses the transfer tracker page.

        :param html: The HTML content of the transfer tracker page.
        """
        soup = BeautifulSoup(html, 'html.parser')
        conferences_list = []

        # Search for all divs with the class 'col-lg-6'
        for div in soup.find_all('div', class_='col-lg-6'):
            # Look for the h1 tag with class 'title-context'
            h1 = div.find('h1', class_='title-context')
            title = h1.text

            if "Men's" in title:
                gender = "Men's"
            elif "Women's" in title:
                gender = "Women's"
            else:
                continue

            # Look for a table with the classes 'table-striped tds_table'
            table = div.find('table', class_=['table-striped', 'tds_table'])

            # Look for all rows in the table
            rows = table.find_all('tr')

            # Loop over all rows to extract the conference data
            for row in rows[1:]:
                cols = row.find_all('td')
                name = cols[0].text.strip()
                resource = cols[0].find('a')['href']
                cid = extract_conference_id(resource)

                conference = Conference(
                    id=cid,
                    name=name,
                    url=urljoin(ENDPOINT, resource),
                    division=self.division,
                    gender=gender
                )

                conferences_list.append(conference)

        # Sort the conferences by name
        conferences_list.sort(key=lambda x: x.name)

        return conferences_list

    def extract(self) -> list[Conference]:
        """
        This function extracts the transfer tracker data.

        :return: The transfer tracker data.
        """
        return self.parse_page(self.fetch_page())

    def get_all_conferences(self) -> list[Conference]:
        """
        This function returns all conferences for the given division.

        :return: The list of conferences.
        """
        return self.extract()

    def get_male_conferences(self) -> list[Conference]:
        """
        This function returns all male conferences for the given division.

        :return: The list of male conferences
        """
        return [conference for conference in self.extract() if conference.gender == "Men's"]

    def get_female_conferences(self) -> list[Conference]:
        """
        This function returns all female conferences for the given division.

        :return: The list of female conferences
        """
        return [conference for conference in self.extract() if conference.gender == "Women's"]

    def get_conferences_by_gender(self, gender: str) -> list[Conference]:
        """
        This function returns all conferences for the given division and gender

        :param gender: The gender of the conference
        :return: The list of conferences
        """

        if gender == "Men's":
            return self.get_male_conferences()
        elif gender == "Women's":
            return self.get_female_conferences()
        else:
            raise ValueError(f"Unsupported gender {gender}!")

    @staticmethod
    def lookup_conference_by_id(cid: int) -> Optional[Conference]:
        """
        This function looks up a conference by its ID.

        :param cid: The ID of the conference.
        :return: The conference with the given ID.
        """
        for division in DIVISIONS:
            extractor = ConferenceExtractor(division)
            for conference in extractor.extract():
                if conference.id == cid:
                    return conference

        return None

    @staticmethod
    def lookup_conference_by_name(gender: str, name: str) -> Optional[Conference]:
        """
        This function looks up a conference by its name.
        """
        for division in DIVISIONS:
            extractor = ConferenceExtractor(division)
            for conference in extractor.extract():
                if not conference:
                    continue

                if conference.gender != gender:
                    continue

                if conference.name != name:
                    continue

                return conference

        return None
