# import os
# from dotenv import load_dotenv
# import stripe
# load_dotenv()
# class CreditCard:
#     async def crateCreditCard():
#         stripe.api_key = os.environ['STRIPE_PUBLIC']

#         response=stripe.Token.create(
#         card={
#                 "number": "4242424242424242",
#                 "exp_month": 1,
#                 "exp_year": 2023,
#                 "cvc": "314",
#             },       
#         )
#         print(f'response {response}')
#         return response

#     async def paymentCard():
#         token=await CreditCard.crateCreditCard()
#         stripe.api_key=os.environ['STRIPE_SECRET']
#         payment = stripe.Charge.create(
#                     amount= int(100)*100,                  # convert amount to cents
#                     currency='usd',
#                     description='Example charge',
#                     source=token['id'],
#                     )
#         print(payment)