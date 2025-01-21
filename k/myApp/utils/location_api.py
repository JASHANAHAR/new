import requests

BASE_URL = "https://www.universal-tutorial.com/api/"
API_KEY = "x_P272a-cEsC7bIDmbdjOOhh5G3zqRMzqP0gKf9g3CTXMKpqKQW57EukJ59xJyaaqe0"

def get_auth_token():
    headers = {"Accept": "application/json", "api-token": API_KEY, "user-email": "your_email@example.com"}
    response = requests.get(f"{BASE_URL}getaccesstoken", headers=headers)
    response.raise_for_status()
    return response.json()["auth_token"]

def get_countries(auth_token):
    headers = {"Authorization": f"Bearer {auth_token}", "Accept": "application/json"}
    response = requests.get(f"{BASE_URL}countries/", headers=headers)
    response.raise_for_status()
    return response.json()

def get_states(auth_token, country_name):
    headers = {"Authorization": f"Bearer {auth_token}", "Accept": "application/json"}
    response = requests.get(f"{BASE_URL}states/{country_name}", headers=headers)
    response.raise_for_status()
    return response.json()
