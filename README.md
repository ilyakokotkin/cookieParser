# Cookie Log Analysis Program

## Introduction
This Python program processes a cookie log file and identifies the most active cookie for a specified day. It follows object-oriented principles and includes command-line argument parsing, file operations, and cookie analysis logic.

## Requirements
- Python 3.x
- pytest

```
pip install -r requirements.txt
```

## Usage
Run the program from the command line by passing the cookie log file and the date for which you want to find the most active cookie:

``` 
python cookie_log_analysis.py -f <path_to_cookie_log_file> -d <date>
```

## Testing
To run the tests, make sure pytest is installed (it's listed in requirements.txt) and execute the following command in the terminal:

```
pytest run
```