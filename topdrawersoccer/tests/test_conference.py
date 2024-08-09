import pytest

from pytest_bdd import scenario

from topdrawersoccer.tests.step_definitions.common_steps import *
from topdrawersoccer.tests.step_definitions.conference_steps import *


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.di
@pytest.mark.men
@scenario("./features/conference.feature", "DI Men's Conferences")
def test_di_mens_conferences():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.dii
@pytest.mark.men
@scenario("./features/conference.feature", "DII Men's Conferences")
def test_dii_mens_conferences():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.diii
@pytest.mark.men
@scenario("./features/conference.feature", "DIII Men's Conferences")
def test_diii_mens_conferences():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.naia
@pytest.mark.men
@scenario("./features/conference.feature", "NAIA Men's Conferences")
def test_naia_mens_conferences():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.njcaa
@pytest.mark.men
@scenario("./features/conference.feature", "NJCAA Men's Conferences")
def test_njcaa_mens_conferences():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.di
@pytest.mark.women
@scenario("./features/conference.feature", "DI Women's Conferences")
def test_di_womens_conferences():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.dii
@pytest.mark.women
@scenario("./features/conference.feature", "DII Women's Conferences")
def test_dii_womens_conferences():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.diii
@pytest.mark.women
@scenario("./features/conference.feature", "DIII Women's Conferences")
def test_diii_womens_conferences():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.naia
@pytest.mark.women
@scenario("./features/conference.feature", "NAIA Women's Conferences")
def test_naia_womens_conferences():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.njcaa
@pytest.mark.women
@scenario("./features/conference.feature", "NJCAA Women's Conferences")
def test_njcaa_womens_conferences():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.lookup
@scenario("./features/conference.feature", "Lookup Conference By ID 1044")
def test_lookup_conference_by_id_1044():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.lookup
@scenario("./features/conference.feature", "Lookup Conference By ID 123")
def test_lookup_conference_by_id_123():
    pass


@pytest.mark.e2e
@pytest.mark.conference
@pytest.mark.lookup
@scenario('./features/conference.feature', "Lookup Men's Conference By Name - Big Ten")
def test_lookup_mens_conference_by_name_big_ten():
    pass

