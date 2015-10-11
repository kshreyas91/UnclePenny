
import json
import urllib2
import json
import pprint
from dateutil import parser
from datetime import datetime

apiKey = 'af9dea6d17214e549ef3155859546fdd'

def makeRestCall(url):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	jsonData = json.loads(response.read())
	return jsonData

def getAccountBalance(accountId):
	url = 'http://api.reimaginebanking.com/customers/accounts/{}?key={}'.format(customerId,apiKey)
	#url = 'http://api.reimaginebanking.com/enterprise/accounts/560f0209f8d8770df0efb090?key=af9dea6d17214e549ef3155859546fdd'
	response = makeRestCall(url)
	
	print response

def getWithdrawals(accountId,transaction_date):
	url = 'http://api.reimaginebanking.com/accounts/{}/withdrawals?key={}'.format(accountId,apiKey)
	response = makeRestCall(url)
	s = 0
	dt = parser.parse(transaction_date)

	for i in response:
		dt1 = parser.parse(i['transaction_date'])
		if(dt1<dt):
			s +=  float(i['amount'])
	return s



def getDeposits(accountId,transaction_date):
	url = 'http://api.reimaginebanking.com/accounts/{}/deposits?key={}'.format(accountId,apiKey)
	response = makeRestCall(url)
	s = 0
	dt = parser.parse(transaction_date)
	#dt = datetime.strptime(transaction_date,'mm/dd/yyyy')
	for i in response:
		dt1 = parser.parse(i['transaction_date'])
		#dt1 = datetime.strptime(i['transaction_date'],'mm/dd/yyyy')
		if(dt1<dt):
			s +=  float(i['amount'])
	return s

def getSavings(accountId,date):
	print (getDeposits(accountId,date) - getWithdrawals(accountId,date))

def createAccount()	

getSavings('560f0207f8d8770df0efa631','10/8/2015')
