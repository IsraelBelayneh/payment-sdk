class PaymentGatewayAPI:
    def __init__(self, client):
        self.client = client

    def create_transaction(self, amount, currency, customer_id):
        data = {
            "amount": amount,
            "currency": currency,
            "customer_id": customer_id
        }
        return self.client._request("transactions", "POST", data)

    def get_transaction(self, transaction_id):
        return self.client._request(f"transactions/{transaction_id}")

    def refund_transaction(self, transaction_id):
        return self.client._request(f"transactions/{transaction_id}/refund", "POST")
