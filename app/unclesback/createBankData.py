import requests
import json

#customerId = 'your customerId here'
apiKey = 'af9dea6d17214e549ef3155859546fdd'

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
payload = {
  "type": "Savings",
  "nickname": "test",
  "rewards": 10000,
  "balance": 10000,	
}
# Create a Savings Account
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
	print('account created')


#customer details
	#customerId : 560f0205f8d8770df0ef9a91
	#accountNo  : 560f0207f8d8770df0efa631
	#nickname   : evert
# 	Deposits:
# 	[
#   {
#     "_id": "5619f71f287f270f002fe1ff",
#     "medium": "balance",
#     "transaction_date": "10/9/2015",
#     "amount": 100,
#     "description": "string",
#     "status": "executed",
#     "payee_id": "560f0207f8d8770df0efa631",
#     "type": "deposit"
#   },
#   {
#     "_id": "5619f731287f270f002fe200",
#     "medium": "balance",
#     "transaction_date": "10/8/2015",
#     "amount": 30,
#     "description": "string",
#     "status": "pending",
#     "payee_id": "560f0207f8d8770df0efa631",
#     "type": "deposit"
#   },
#   {
#     "_id": "5619f74e287f270f002fe201",
#     "medium": "balance",
#     "transaction_date": "9/30/2015",
#     "amount": 19,
#     "description": "last deep of sept",
#     "status": "pending",
#     "payee_id": "560f0207f8d8770df0efa631",
#     "type": "deposit"
#   }
# ]


