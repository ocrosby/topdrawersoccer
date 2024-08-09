from pytest_bdd import scenario

from topdrawersoccer.tests.step_definitions.common_steps import *
from topdrawersoccer.tests.step_definitions.transfer_steps import *


@scenario('./features/transfer.feature', 'Colleges')
def test_colleges():
    pass


@scenario('./features/transfer.feature', 'Outgoing Colleges')
def test_outgoing_colleges():
    pass


@scenario('./features/transfer.feature', 'Incoming Colleges')
def test_incoming_colleges():
    pass


@scenario('./features/transfer.feature', 'Players')
def test_players():
    pass

