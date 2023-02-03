import requests

def get_response() -> int:
    return requests.get('https://www.google.com/').status_code
