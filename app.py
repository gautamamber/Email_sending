from flask import Flask, render_template, request
from flask_mail import Mail, Message
app = Flask(__name__)


app.config.update(dict(
	DEBUG = True,

	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_TLS = False,
	MAIL_USE_SSL= True,
	MAIL_USERNAME = 'gautamamber5@gmail.com',
	MAIL_PASSWORD = 'ambergautam1998'))

mail = Mail(app)

@app.route('/')
def select():
	return render_template('main.html')

@app.route('/hello/', methods=['POST'])
def hello():
    email=request.form['email']
    name = request.form['name']
    msg = Message("hello world",
                  sender="gautamamber5@gmail.com",
                  recipients=[email])
    msg.body = "testing"
    msg.html = name
    mail.send(msg)
    return "Sent"

    



if __name__ == '__main__':
   app.run(debug = True)