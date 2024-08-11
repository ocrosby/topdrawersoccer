import pytest

from pytest_bdd import scenario


from tests.step_definitions.common_steps import *
from tests.step_definitions.transfer_steps import *


@pytest.mark.e2e
@pytest.mark.transfer
@scenario('../features/transfer.feature', 'Colleges')
def test_colleges():
    pass


@pytest.mark.e2e
@pytest.mark.transfer
@scenario('../features/transfer.feature', 'Outgoing Colleges')
def test_outgoing_colleges():
    pass


@pytest.mark.e2e
@pytest.mark.transfer
@scenario('../features/transfer.feature', 'Incoming Colleges')
def test_incoming_colleges():
    pass


@pytest.mark.e2e
@pytest.mark.transfer
@scenario('../features/transfer.feature', 'Players')
def test_players():
    pass

