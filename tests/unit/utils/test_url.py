import pytest

from topdrawersoccer.utils.url import extract_id_from_url, extract_gender_from_url, extract_division_from_url


@pytest.mark.unit
@pytest.mark.parametrize("url, expected_id, expect_error, error_message", [
    ("https://www.acme.com/cfid-22", 22, False, None),
    ("https://www.acme.com/cfid-33", 33, False, None),
    ("https://www.acme.com/cfid-44", 44, False, None),
    ("https://www.acme.com/cfid-55", 55, False, None),
    ("https://www.acme.com/?genderId=&conferenceId=123&conferenceName=asun", 123, False, None),
    ("https://www.acme.com/cfid-", None, True, "ID not found in URL: https://www.acme.com/cfid-"),
    ("https://www.acme.com/big-ten/", None, True, "ID not found in URL: https://www.acme.com/big-ten/"),
    ("/college-soccer/college-soccer-details/men/washington/clgid-159", 159, False, None),
])
def test_extract_id_from_url(url, expected_id, expect_error, error_message):
    if expect_error:
        with pytest.raises(ValueError) as excinfo:
            extract_id_from_url(url)
        assert str(excinfo.value) == error_message
    else:
        assert extract_id_from_url(url) == expected_id


@pytest.mark.unit
@pytest.mark.parametrize("url, expected_gender, expect_error, error_message", [
    ("https://www.acme.com/women/albany/clgid-6", "Women's", False, None),
    ("https://www.acme.com/men/albany/clgid-6", "Men's", False, None),
    ("https://www.acme.com/something/albany/clgid-6", None, True, "Gender not found in URL: 'https://www.acme.com/something/albany/clgid-6'"),
    ])
def test_extract_gender_from_url(url, expected_gender, expect_error, error_message):
    if expect_error:
        with pytest.raises(ValueError) as excinfo:
            extract_gender_from_url(url)
        assert str(excinfo.value) == error_message
    else:
        assert extract_gender_from_url(url) == expected_gender



@pytest.mark.unit
@pytest.mark.parametrize("url, expected_division, expect_error, error_message", [
    ("https://www.acme.com/?divisionName=di&divisionId=1", "DI", False, None),
    ("https://www.acme.com/?divisionName=dii&divisionId=2", "DII", False, None),
    ("https://www.acme.com/?divisionName=diii&divisionId=3", "DIII", False, None),
    ("https://www.acme.com/?divisionName=naia&divisionId=4", "NAIA", False, None),
    ("https://www.acme.com/?divisionName=njcaa&divisionId=5", "NJCAA", False, None),
    ("https://www.acme.com", None, True, "Division not found in URL: 'https://www.acme.com'"),
])
def test_extract_division_from_url(url, expected_division, expect_error, error_message):
    if expect_error:
        with pytest.raises(ValueError) as excinfo:
            extract_division_from_url(url)
        assert str(excinfo.value) == error_message
    else:
        assert extract_division_from_url(url) == expected_division
