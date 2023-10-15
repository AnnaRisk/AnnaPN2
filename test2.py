import requests
import pprint

from pprint import pprint


def test_111():
    url = "https://send-request.me/api/users/"
    data = {
      "first_name": "Diana",
      "last_name": "Donovan",
      "company_id": 2,
      "user_id": 68
    }
    response = requests.post(url,json = data)
    
    print(response.json())
    print(response.status_code)
