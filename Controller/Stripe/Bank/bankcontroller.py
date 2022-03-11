# import stripe

# class bankController:

#     async def createBankToken():
#             stripe.api_key = ""

#             response=stripe.Token.create(
#             bank_account={
#                     "number": "4242424242424242",
#                     "exp_month": 1,
#                     "exp_year": 2023,
#                     "cvc": "314",
#                 },       
#             )
#             print(f'response {response}')
#             return response