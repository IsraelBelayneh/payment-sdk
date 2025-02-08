from .api_client import ApiClient
from .config import Config
from .utils import get_password, get_timestamp

class StkPush:
    def __init__(self):
        self.client = ApiClient()

    def initiate_stk_push(self, phone_number, amount):
        payload = {
            "BusinessShortCode": Config.SHORTCODE,
            "Password": get_password(),
            "Timestamp": get_timestamp(),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": Config.SHORTCODE,
            "PhoneNumber": phone_number,
            "CallBackURL": Config.CALLBACK_URL,
            "AccountReference": "TestPayment",
            "TransactionDesc": "Payment Test"
        }
        return self.client.post_request("/mpesa/stkpush/v1/processrequest", payload)
