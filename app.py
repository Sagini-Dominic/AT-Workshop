from flask import Flask, render_template

app = Flask(__name__)

@app.route('/base')
def base():
	return render_template("base.html")

@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/sms')
def sms():
	return render_template("sms.html")

@app.route('/voice')
def voice():
	return render_template("voice.html")

@app.route('/payment')
def payment():
	return render_template("payment.html")

@app.route('/airtime')
def airtime():
	return render_template("airtime.html")			

if __name__ == '__main__':
	app.run()