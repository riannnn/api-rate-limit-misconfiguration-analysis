import requests

URL = "https://example.com/api"
PARAMS = {"per_page": 300, "page": 1}

def test_rate_limit():
    for i in range(1, 51):
        response = requests.get(URL, params=PARAMS)
        print(f"Request {i}: Status Code {response.status_code}")

if __name__ == "__main__":
    test_rate_limit()
