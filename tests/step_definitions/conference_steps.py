from pytest_bdd import when, then, parsers

from topdrawersoccer.extractors.school_extractor import SchoolExtractor
from topdrawersoccer.extractors.conference_extractor import ConferenceExtractor
from topdrawersoccer.models.school import School


@when(parsers.parse('I retrieve the list of {division} {gender} conferences'))
def retrieve_list_of_conferences(division: str, gender: str, context):
    conferences = None

    try:
        conferences = ConferenceExtractor(division).get_conferences_by_gender(gender)
    except Exception as e:
        context['errors'].append(str(e))
    finally:
        context['list'] = conferences


@when(parsers.parse('I retrieve the {gender} conference with ID {cid:d}'))
def retrieve_conference_by_id(gender: str, cid: int, context):
    conference = None

    try:
        conference = ConferenceExtractor.lookup_conference_by_id(gender, cid)
    except Exception as e:
        context['errors'].append(str(e))
    finally:
        context['conference'] = conference


def remove_double_quotes(s: str) -> str:
    return s.replace('"', "")


@when(parsers.parse('I retrieve the {gender} conference with name {name}'))
def retrieve_conference_by_name(gender: str, name: str, context):
    conference = None

    gender = remove_double_quotes(gender)
    name = remove_double_quotes(name)

    try:
        conference = ConferenceExtractor.lookup_conference_by_name(gender, name)
    except Exception as e:
        context['errors'].append(str(e))
    finally:
        context['conference'] = conference


@when(parsers.parse('I retrieve schools for the "{gender}" conference with name "{name}"'))
def retrieve_schools_for_conference_name(gender: str, name: str, context):
    schools = None

    gender = remove_double_quotes(gender)
    name = remove_double_quotes(name)

    try:
        conference = ConferenceExtractor.lookup_conference_by_name(gender, name)
        school_extractor = SchoolExtractor(conference.url)
        schools = school_extractor.get_schools(conference.id, conference.division)
    except Exception as e:
        context['errors'].append(str(e))
    finally:
        context['list'] = schools


@when(parsers.parse('I retrieve schools for the "{gender}" conference with ID {cid:d}'))
def retrieve_schools_for_conference_id(gender: str, cid: int, context):
    schools = None

    gender = remove_double_quotes(gender)

    try:
        conference = ConferenceExtractor.lookup_conference_by_id(gender, cid)
        school_extractor = SchoolExtractor(conference.url)
        schools = school_extractor.get_schools(conference.id, conference.division)
    except ValueError as e:
        context['errors'].append(str(e))
    except Exception as e:
        context['errors'].append(str(e))
    finally:
        context['list'] = schools


@then('the conference should be found')
def verify_conference_found(context):
    conference = context['conference']
    assert conference is not None, "Expected conference to be found"


@then('the conference should not be found')
def verify_conference_not_found(context):
    conference = context['conference']
    assert conference is None, "Expected conference to not be found"


@then(parsers.parse('the conference should have the ID {expected_id:d}'))
def verify_conference_id(expected_id: int, context):
    conference = context['conference']
    assert conference.id == expected_id, f"Expected conference ID to be {expected_id}, but got {conference.id}"


@then(parsers.parse('the conference should have the name "{expected_name}"'))
def verify_conference_name(expected_name: str, context):
    conference = context['conference']
    assert conference.name == expected_name, f"Expected conference name to be {expected_name}, but got {conference.name}"


@then(parsers.parse('the conference should have division {expected_division}'))
def verify_conference_division(expected_division: str, context):
    conference = context['conference']
    assert conference.division == expected_division, f"Expected conference division to be {expected_division}, but got {conference.division}"


@then(parsers.parse('the conference should be a {expected_gender} conference'))
def verify_conference_gender(expected_gender: str, context):
    conference = context['conference']
    assert conference.gender == expected_gender, f"Expected conference gender to be {expected_gender}, but got {conference.gender}"


@then(parsers.parse('the conference should have the URL "{expected_url}"'))
def verify_conference_url(expected_url: str, context):
    conference = context['conference']
    assert conference.url == expected_url, f"Expected conference URL to be {expected_url}, but got {conference.url}"


@then(parsers.parse('The list should contain {expected_count:d} conferences'))
def verify_conference_count(expected_count: int, context):
    actual_count = len(context['list'])
    assert actual_count == expected_count, f"Expected {expected_count} conferences, but got {actual_count}"


@then(parsers.parse('The list should contain a conference named "{expected_name}"'))
def verify_conference_in_list(expected_name: str, context):
    conferences = context['list']
    assert any(conference.name == expected_name for conference in conferences), f"Expected conference named {expected_name} in list"


@then(parsers.parse('The list should not contain a conference named "{expected_name}"'))
def verify_conference_not_in_list(expected_name: str, context):
    conferences = context['list']
    assert not any(conference.name == expected_name for conference in conferences), f"Expected conference named {expected_name} not in list"


@then(parsers.parse('there should be {expected_count:d} schools in the list'))
def verify_school_count(expected_count: int, context):
    assert 'list' in context, "Expected a list of schools"
    target_list = context['list']
    assert target_list is not None, "Expected a list of schools"
    actual_count = len(target_list)
    assert actual_count == expected_count, f"Expected {expected_count} schools, but got {actual_count}"

    # Loop over all the items in the list and make sure they are of type School
    for item in target_list:
        assert isinstance(item, School)


@then(parsers.parse('the list should contain a school named "{expected_name}"'))
def verify_school_in_list(expected_name: str, context):
    expected_name = remove_double_quotes(expected_name)

    target_list = context['list']
    assert target_list is not None, "Expected a list of schools"
    assert any(school.name == expected_name for school in target_list), f"Expected school named {expected_name} in list"
