from urllib.parse import urljoin

from bs4 import BeautifulSoup

from topdrawersoccer.config import ENDPOINT
from topdrawersoccer.utils.url import extract_id_from_url, extract_gender_from_url, extract_division_from_url
from topdrawersoccer.extractors.base_extractor import BaseExtractor
from topdrawersoccer.models.team import Team

DIVISION_TO_URL_MAP = {
    "DI": "https://www.topdrawersoccer.com/college/teams/?divisionName=di&divisionId=1",
    "DII": "https://www.topdrawersoccer.com/college/teams/?divisionName=dii&divisionId=2",
    "DIII": "https://www.topdrawersoccer.com/college/teams/?divisionName=diii&divisionId=3",
    "NAIA": "https://www.topdrawersoccer.com/college/teams/?divisionName=naia&divisionId=4",
    "NJCAA": "https://www.topdrawersoccer.com/college/teams/?divisionName=njcaa&divisionId=5"
}

from topdrawersoccer.config import DIVISIONS


class TeamExtractor(BaseExtractor):
    def __init__(self, url: str):
        super().__init__(url)

    def parse_page(self, html: str) -> list[Team]:
        """
        This function parses the team page.

        :param html: The HTML content of the team page.
        """
        soup = BeautifulSoup(html, 'html.parser')
        teams: list[Team] = []

        # Search for all divs with the classes 'col-lg-6', 'col-12', 'minitable'
        target_divs = soup.find_all('div', class_=['col-lg-6', 'col-12', 'minitable'])
        for target_div in target_divs:
            # Look for the caption tag with classes 'header', 'table-caption--top'
            caption = target_div.find('caption', class_=['header', 'table-caption--top'])
            if not caption:
                continue

            # Look for the anchor tag inside the caption tag
            anchor = caption.find('a')
            if not anchor:
                continue

            target_table = target_div.find('table', class_=['table-striped', 'tds_table'])
            if not target_table:
                continue

            conference_name = anchor.text.strip()
            conference_href = anchor.get('href').strip()
            conference_url = urljoin(ENDPOINT, conference_href)
            conference_id = extract_id_from_url(conference_url)

            # Look for all rows in the target table
            rows = target_table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                target_cell = cols[0]

                team_name = target_cell.text.strip()
                anchor = target_cell.find('a')
                if not anchor:
                    continue

                team_url = urljoin(ENDPOINT, anchor.get('href').strip())
                team_id = extract_id_from_url(team_url)
                team_gender = extract_gender_from_url(team_url)

                team_division = extract_division_from_url(self.url)

                current_team = Team(
                    id=team_id,
                    name=team_name,
                    url=team_url,
                    gender=team_gender,
                    division=team_division,
                    conference_id=conference_id
                )

                teams.append(current_team)

        return teams

    def extract(self):
        """
        This function extracts the teams from the page.
        """
        return self.parse_page(self.fetch_page())

    def get_all_teams(self) -> list[Team]:
        """
        This function returns the teams from the page.

        :return: The list of teams.
        """
        return self.extract()

    def get_womens_teams(self) -> list[Team]:
        all_teams = self.get_all_teams()

        return [team for team in all_teams if team.gender == "Women's"]

    def get_mens_teams(self) -> list[Team]:
        all_teams = self.get_all_teams()

        return [team for team in all_teams if team.gender == "Men's"]

    @staticmethod
    def all_teams():
        """
        This function returns all the teams.
        """
        all_teams = []

        for division in DIVISIONS:
            division_url = DIVISION_TO_URL_MAP[division]
            division_extractor = TeamExtractor(division_url)
            division_teams = division_extractor.get_all_teams()
            all_teams.extend(division_teams)

        return all_teams


    @staticmethod
    def teams_by_gender_and_division(gender: str, division: str):
        if gender == "Women's":
            return TeamExtractor(DIVISION_TO_URL_MAP[division]).get_womens_teams()
        elif gender == "Men's":
            return TeamExtractor(DIVISION_TO_URL_MAP[division]).get_mens_teams()
        else:
            raise ValueError(f"Unsupported gender '{gender}'!")


if __name__ == "__main__":
    teams = TeamExtractor.all_teams()
    for team in teams:
        print(team)

