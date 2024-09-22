import stripe
import os

stripe.api_key = os.getenv('STRIPE_SECRET_KEY', 'sk_test_51Q1WUFFahxIveB3J9xITPIPSWzzSNrhzAnjui53ubMOwR5fM1tblhqhPS5gknE4pLhPXOrdwS0ZgReVB2ajubpEN00NcxHK0Qy')

def stripe_checkout_session(email):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        customer_email=email,
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Pro License',
                },
                'unit_amount': 5000,  # $50
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:3000/success',
        cancel_url='http://localhost:3000/cancel',
    )
    return session
