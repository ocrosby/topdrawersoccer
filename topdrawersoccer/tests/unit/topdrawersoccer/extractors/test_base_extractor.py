import pytest
from unittest.mock import patch, MagicMock
from topdrawersoccer.extractors.base_extractor import BaseExtractor


class TestBaseExtractor:

    @pytest.mark.unit
    @patch('http.client.HTTPSConnection')
    def test_fetch_page_success(self, mock_https_connection):
        # Mock the response to return a successful status and HTML content
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b'<html><body>Test Page</body></html>'
        mock_https_connection.return_value.getresponse.return_value = mock_response

        extractor = BaseExtractor('https://www.example.com')
        html = extractor.fetch_page()

        assert html == '<html><body>Test Page</body></html>'

    @pytest.mark.unit
    @patch('http.client.HTTPSConnection')
    def test_fetch_page_non_200_status(self, mock_https_connection):
        # Mock the response to return a non-200 status
        mock_response = MagicMock()
        mock_response.status = 404
        mock_https_connection.return_value.getresponse.return_value = mock_response

        extractor = BaseExtractor('https://www.example.com')

        with pytest.raises(Exception) as excinfo:
            extractor.fetch_page()

        assert str(excinfo.value) == 'Failed to fetch page, status code: 404'

    @pytest.mark.unit
    def test_fetch_page_invalid_url(self):
        # Test with an invalid URL
        extractor = BaseExtractor('invalid-url')

        with pytest.raises(ValueError) as execinfo:
            extractor.fetch_page()

        assert str(execinfo.value) == 'Invalid URL: invalid-url'
