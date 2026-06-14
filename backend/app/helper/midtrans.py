from app.model import User, Transaction, PaymentMethod

class MidtransUtility:
    @staticmethod
    def build_params(user: User, transaction: Transaction, payment_method:PaymentMethod) -> dict:
        first_name,last_name = MidtransUtility._split_name(user.name)
        return {
            "transaction_details": {
                "order_id": transaction.transaction_code,
                "gross_amount": transaction.amount
            }, 
            "credit_card": {
                "secure": True
            },
            "customer_details": {
                "first_name": first_name,
                "last_name": last_name,
                "email": user.email
            },
            "enabled_payments": [payment_method.code]
        }

    @staticmethod
    def _split_name(fullname:str) -> tuple[str,str] :
        name = fullname.split(' ')
        last_name = name.pop() if len(name) > 1 else ''
        first_name = name[0]
        return first_name, last_name