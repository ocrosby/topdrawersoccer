import pytest

from topdrawersoccer.utils.url import extract_id_from_url


@pytest.mark.unit
@pytest.mark.parametrize("url, expected_id, expect_error, error_message", [
    ("https://www.acme.com/cfid-22", 22, False, None),
    ("https://www.acme.com/cfid-33", 33, False, None),
    ("https://www.acme.com/cfid-44", 44, False, None),
    ("https://www.acme.com/cfid-55", 55, False, None),
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