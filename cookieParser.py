import argparse
import datetime
from collections import Counter

class CommandLineParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Process the cookie log file.')
        self.parser.add_argument('-f', '--file', type=str, required=True, help='Filename of the cookie log')
        self.parser.add_argument('-d', '--date', type=str, required=True, help='Date to find the most active cookie')

    def parse_arguments(self):
        return self.parser.parse_args()

class CookieLogFile:
    def __init__(self, filename):
        self.filename = filename

    def read_and_filter_cookies(self, date):
        cookies = []
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        with open(self.filename, 'r') as file:
            next(file)    
            for line in file:
                cookie, timestamp = line.strip().split(',')
                cookie_date = datetime.datetime.fromisoformat(timestamp).date()
                if cookie_date == date:
                    cookies.append(cookie)
        return cookies

class CookieAnalyzer:
    @staticmethod
    def find_most_active_cookie(cookies):
        counter = Counter(cookies)
        max_count = max(counter.values())
        return [cookie for cookie, count in counter.items() if count == max_count]

def main():
    parser = CommandLineParser()
    args = parser.parse_arguments()

    try:
        cookie_log_file = CookieLogFile(args.file)
        filtered_cookies = cookie_log_file.read_and_filter_cookies(args.date)
        most_active_cookies = CookieAnalyzer.find_most_active_cookie(filtered_cookies)
        for cookie in most_active_cookies:
            print(cookie)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
