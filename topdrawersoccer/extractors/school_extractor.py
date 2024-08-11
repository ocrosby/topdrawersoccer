from urllib.parse import urljoin
from typing import Optional

from bs4 import BeautifulSoup

from topdrawersoccer.config import ENDPOINT
from topdrawersoccer.utils.url import extract_id_from_url
from topdrawersoccer.models.conference import Conference
from topdrawersoccer.models.school import School
from topdrawersoccer.extractors.base_extractor import BaseExtractor


class SchoolExtractor(BaseExtractor):
    def __init__(self, url: str):
        super().__init__(url)

    def parse_page(self, html: str) -> list[School]:
        """
        This function parses the schools page.

        :param html: The HTML content of the schools page.
        """
        schools: list[School] = []

        soup = BeautifulSoup(html, 'html.parser')

        # Search for all divs with the class 'col-lg-6'
        for div in soup.find_all('div', class_='col-lg-6'):
            # Look for the h1 tag with class 'title-context'
            h1 = div.find('h1', class_='title-context')
            title = h1.text

            if title == "Conference Standings":
                table = div.find('table', class_=['table-striped', 'tds_table'])

                # Look for all rows in the table
                rows = table.find_all('tr')

                # Loop over all rows to extract the conference data
                for row in rows:
                    cols = row.find_all('td')
                    name = cols[1].text.strip()
                    resource = cols[1].find('a')['href']
                    sid = extract_id_from_url(resource)

                    school = School(
                        id=sid,
                        name=name,
                        url=urljoin(ENDPOINT, resource),
                        division=None,
                        conference_id=0,
                    )

                    schools.append(school)

        return schools

    def extract(self) -> list[School]:
        return self.parse_page(self.fetch_page())

    def get_schools(self, conference_id: int, division: str) -> list[School]:
        schools: list[School]

        schools = self.extract()

        for school in schools:
            school.conference_id = conference_id
            school.division = division

        return schools