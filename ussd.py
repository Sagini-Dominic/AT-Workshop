from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
	session_id = request.values.get("sessionId", None)
	session_code = request.values.get("serviceCode", None)
	phone_number = request.values.get("phone_Number", None)
	text = request.values.get("text", "default")
	if text=='':
		response = "CON what would you like to check \n"
		response += "1. My Account \n"
		response += "2. My Phone number"
	elif text =='1':
		response = "CON Choose account information you want to view \n"
		response += "1. My Account \n"
		response += "2. Account balance"
	elif text =='1*1':
		accountNumber = "ACC1001"
		response = "END your account number is " + balance
	elif text == '1*2':
		balance = "KES 10,000"
		response = "END your phone number is " + phone_number
	else:
		response = "CON invalid choice. Try Again"
	return response

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=os.environ.get('PORT'))

		

