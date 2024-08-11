import pytest

from pytest_bdd import scenario

from tests.step_definitions.common_steps import *
from tests.step_definitions.teams_steps import *


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.women
@scenario("../features/teams.feature", "All Women's Teams")
def test_all_womens_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.men
@scenario("../features/teams.feature", "All Men's Teams")
def test_all_mens_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.men
@pytest.mark.di
@scenario("../features/teams.feature", "Men\'s DI Teams by Conference ASUN")
def test_mens_di_teams_by_conference_asun():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.women
@pytest.mark.di
@scenario("../features/teams.feature", "Women's DI Teams")
def test_womens_di_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.women
@pytest.mark.dii
@scenario("../features/teams.feature", "Women's DII Teams")
def test_womens_dii_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.women
@pytest.mark.diii
@scenario("../features/teams.feature", "Women's DIII Teams")
def test_womens_diii_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.women
@pytest.mark.naia
@scenario("../features/teams.feature", "Women's NAIA Teams")
def test_womens_naia_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.women
@pytest.mark.njcaa
@scenario("../features/teams.feature", "Women's NJCAA Teams")
def test_womens_njcaa_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.men
@pytest.mark.di
@scenario("../features/teams.feature", "Men's DI Teams")
def test_mens_di_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.men
@pytest.mark.dii
@scenario("../features/teams.feature", "Men's DII Teams")
def test_mens_dii_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.men
@pytest.mark.diii
@scenario("../features/teams.feature", "Men's DIII Teams")
def test_mens_diii_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.men
@pytest.mark.naia
@scenario("../features/teams.feature", "Men's NAIA Teams")
def test_mens_naia_teams():
    pass


@pytest.mark.e2e
@pytest.mark.team
@pytest.mark.men
@pytest.mark.njcaa
@scenario("../features/teams.feature", "Men's NJCAA Teams")
def test_mens_njcaa_teams():
    pass

