import pytest
from pytest_bdd import when, then, parsers

from topdrawersoccer.tests.step_definitions.common_steps import context
from topdrawersoccer.models.team import Team
from topdrawersoccer.utils.text import remove_double_quotes
from topdrawersoccer.config import DIVISIONS
from topdrawersoccer.extractors.team_extractor import TeamExtractor, DIVISION_TO_URL_MAP


@when(parsers.parse('I retrieve all "{gender}" teams'))
def retrieve_all_teams_by_gender(gender: str, context):
    try:
        context['list'] = TeamExtractor.all_teams()
    except Exception as e:
        context['errors'].append(str(e))


@when(parsers.parse('I retrieve "{gender}" {division} teams by conference {conference_name}'))
def retrieve_teams_by_gender_division_and_name(gender: str, division: str, conference_name: str, context):
    try:
        TeamExtractor.teams_by_gender_and_division(gender, division)
    except Exception as e:
        context['errors'].append(str(e))


@when(parsers.parse('I retrieve "{gender}" {division} teams'))
def retrieve_teams_by_gender_and_division(gender: str, division: str, context):
    try:
        TeamExtractor.teams_by_gender_and_division(gender, division)
    except Exception as e:
        context['errors'].append(str(e))


@then(parsers.parse('the list should contain teams'))
def validate_list_contains_teams(context):
    teams = context.get('list', None)

    assert teams is not None, 'The list is not defined!'

    for item in teams:
        assert isinstance(item, Team), f'Found a non-Team item!'


@then(parsers.parse('the list should contain {expected_count:d} teams'))
def validate_team_count(expected_count: int, context):
    validate_list_contains_teams(context)
    items = context.get('list', None)

    assert len(items) == expected_count, f'Expected {expected_count} teams, found {len(items)}'


@then(parsers.parse('the list should contain a team named "{expected_team_name}"'))
def validate_team_by_name(expected_team_name: str, context):
    """
    Go through the list of all teams and verify that at least one contains the expected name

    :param expected_team_name: the team name to search for
    :param context:
    :return:
    """
    expected_team_name = remove_double_quotes(expected_team_name)

    found = False
    for item in context.get('list', None):
        if item and isinstance(item, Team) and item.name == expected_team_name:
            found = True
            break

    assert found


@then(parsers.parse('the list should not contain a team named "{unexpected_team_name}"'))
def validate_team_not_in_list(unexpected_team_name: str, context):
    """
    Go through the list of all teams and verify that none contain the unexpected name

    :param unexpected_team_name: the team name to search for
    :param context:
    :return:
    """
    unexpected_team_name = remove_double_quotes(unexpected_team_name)

    found = False
    for item in context.get('list', None):
        if item and isinstance(item, Team) and item.name == unexpected_team_name:
            found = True
            break

    assert not found
