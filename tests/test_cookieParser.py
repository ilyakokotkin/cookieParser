import pytest
from unittest.mock import mock_open, patch
from cookieParser import CommandLineParser, CookieAnalyzer, CookieLogFile

# Sample data for testing
cookie_log_content = """cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
"""

def test_command_line_parser():
    test_args = ["-f", "test_log.csv", "-d", "2018-12-09"]
    parser = CommandLineParser()
    parsed = parser.parse_arguments(test_args)
    assert parsed.file == "test_log.csv"
    assert parsed.date == "2018-12-09"

@patch("builtins.open", new_callable=mock_open, read_data=cookie_log_content)
def test_cookie_log_file_reading(mock_file):
    cookie_log_file = CookieLogFile("test_log.csv")
    cookies = cookie_log_file.read_and_filter_cookies("2018-12-09")
    assert cookies == ["AtY0laUfhglK3lC7", "SAZuXPGUrfbcn5UA", "5UAVanZf6UtGyKVS", "AtY0laUfhglK3lC7"]

def test_cookie_analyzer():
    cookies = ["AtY0laUfhglK3lC7", "AtY0laUfhglK3lC7", "5UAVanZf6UtGyKVS"]
    most_active = CookieAnalyzer.find_most_active_cookie(cookies)
    assert most_active == ["AtY0laUfhglK3lC7"]
