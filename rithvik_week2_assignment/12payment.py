class Payment:
    def process_payment(self):
        pass
class CreditCardPayment(Payment):
    def process_payment(self):
        print("paying with Credit Card")
class PayPalPayment(Payment):
    def process_payment(self ):
        print("paying with PayPal")

class BitCoinPayment(Payment):
    def process_payment(self ):
        print("paying with BitCoin")
CreditCard_Payment=CreditCardPayment()
CreditCard_Payment.process_payment()
PayPal_Payment=PayPalPayment()
PayPal_Payment.process_payment()
BitCoin_Payment=BitCoinPayment()
BitCoin_Payment.process_payment()
