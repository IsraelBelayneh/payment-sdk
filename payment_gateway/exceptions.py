class PaymentGatewayException(Exception):
    """Base Exception for the Payment Gateway SDK"""
    pass

class AuthenticationError(PaymentGatewayException):
    """Raised when authentication fails"""
    pass

class TransactionError(PaymentGatewayException):
    """Raised when a transaction fails"""
    pass
