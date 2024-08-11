import http.client

from urllib.parse import urlparse


class BaseExtractor:
    url: str

    def __init__(self, url: str):
        self.url = url

    def fetch_page(self) -> str:
        """
        This function fetches the transfer tracker page.

        :return: The HTML content of the transfer tracker page.
        """
        print(f"Fetching page: '{self.url}' ...")

        url_parts = urlparse(self.url)

        # Check if the URL is valid
        if not url_parts.scheme or not url_parts.netloc:
            raise ValueError(f"Invalid URL: {self.url}")

        conn = http.client.HTTPSConnection(url_parts.netloc)
        conn.request("GET", url_parts.path)
        response = conn.getresponse()

        if response.status != 200:
            raise Exception(f"Failed to fetch page, status code: {response.status}")

        html = response.read().decode('utf-8')
        conn.close()

        return html
