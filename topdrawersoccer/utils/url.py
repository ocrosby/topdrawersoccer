import re


def extract_id_from_url(url: str) -> int:
    """
    Extracts the conference ID from the given URL.

    :param url: The URL containing the conference ID.
    :return: The extracted conference ID.
    """
    match = re.search(r'[-](\d+)', url)
    if match:
        return int(match.group(1))
    else:
        raise ValueError(f"ID not found in URL: {url}")