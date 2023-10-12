import stripe
from rest_framework import status
from stripe.error import StripeError

from courses.models import Payment


def stripe_card_payment(data_dict, product_price):
    try:
        card_details = {
            "type": "card",
            "card": {
                "number": data_dict['card_number'],
                "exp_month": data_dict['expiry_month'],
                "exp_year": data_dict['expiry_year'],
                "cvc": data_dict['cvc'],
            },
        }

        payment_intent = stripe.PaymentIntent.create(
            amount=product_price,
            currency='rub',
            payment_method="pm_card_visa",
            payment_method_types=[card_details["type"]],
            automatic_payment_methods={
                "enabled": False,
            },
        )

        try:
            payment_confirm = stripe.PaymentIntent.confirm(
                payment_intent['id']
            )
            payment_intent_modified = stripe.PaymentIntent.retrieve(
                payment_intent['id']
            )
        except StripeError as e:
            payment_intent_modified = stripe.PaymentIntent.retrieve(
                payment_intent['id']
            )
            payment_confirm = {
                "stripe_payment_error": f"Failed with message: \n {e}",
                "code": payment_intent_modified['last_payment_error'][
                    'code'],
                "message": payment_intent_modified['last_payment_error'][
                    'message'],
                'status': "Failed"
            }
        if (payment_intent_modified
                and payment_intent_modified['status'] == 'succeeded'):
            response = {
                'message': "Card Payment Success",
                'status': status.HTTP_200_OK,
                "card_details": card_details,
                "payment_intent": payment_intent_modified,
                "payment_confirm": payment_confirm
            }
        else:
            response = {
                'message': "Card Payment Failed",
                'status': status.HTTP_400_BAD_REQUEST,
                "card_details": card_details,
                "payment_intent": payment_intent_modified,
                "payment_confirm": payment_confirm
            }
    except Exception as e:
        response = {
            'error': f"{e}",
            'status': status.HTTP_400_BAD_REQUEST,
            "payment_intent": {"id": "Null"},
            "payment_confirm": {'status': "Failed"}
        }
    return response


def save_payment_if_valid(response, payment):
    if response['payment_confirm'] and response[
        'status'
    ] == status.HTTP_200_OK:
        payment_confirm = response['payment_confirm']

        payment_method = stripe.PaymentMethod.retrieve(
            payment_confirm['payment_method']
        )

        payment['amount'] = payment_confirm['amount_received']
        payment['payment_method'] = payment_method['type']

        Payment.objects.create(**payment)

