import pytest

from pytest_bdd import then, scenarios


@pytest.fixture
def context():
    return {
        'errors': [],
    }


@then('there should be no errors')
def no_errors(context):
    errors = context.get('errors', [])

    assert len(errors) == 0, f"Expected no errors, got {len(errors)}"


@then('the list should not be empty')
def list_not_empty(context):
    resulting_list = context.get('list', [])

    assert len(resulting_list) > 0, "Expected list to not be empty"

