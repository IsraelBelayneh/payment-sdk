import requests
from .config import API_BASE_URL, TIMEOUT
from .exceptions import PaymentGatewayException

class PaymentGatewayClient:
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = API_BASE_URL

    def _request(self, endpoint, method="GET", data=None):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        url = f"{self.base_url}/{endpoint}"

        try:
            if method == "GET":
                response = requests.get(url, headers=headers, timeout=TIMEOUT)
            else:
                response = requests.post(url, json=data, headers=headers, timeout=TIMEOUT)

            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise PaymentGatewayException(f"API Request Failed: {str(e)}")

