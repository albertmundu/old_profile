# https://www.twilio.com/blog/2018/03/send-email-programmatically-with-gmail-python-and-flask.html
from flask import Flask
from flask_mail import Mail, Message
import os
import pandas

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}


f=open('message.html',encoding='utf8')
text=f.read()

app.config.update(mail_settings)
mail = Mail(app)

# colnames = ['eaddress']
# data = pandas.read_csv('mail-list.csv',names=colnames)
# contacts = data.eaddress.tolist() 
# print(contacts)


if __name__ == '__main__':
    for r in ["rsi2017506@iiita.ac.in", "ihm2014004@iiita.ac.in", "rsi2018509@iiita.ac.in", "rsi2017505@iiita.ac.in", "pse2016002@iiita.ac.in", "rsi2016005@iiita.ac.in", "rse2017502@iiita.ac.in", "phc2014001@iiita.ac.in", "phc2016003@iiita.ac.in", "phc2016001@iiita.ac.in" ]:
        rec = []
        with app.app_context():
            rec.append(r)
            msg = Message(subject="Invitation to participate in National Workshop & Summer School (ADASIVA - 2018)",
                    sender=app.config.get("MAIL_USERNAME"),
                     # replace with your email for testing
                     recipients=rec,
                     html=text)
                    # body="<h1>This is a test email I sent with Gmail and Python!</h1>")
            msg.attach('brochure.pdf',content_type='application/pdf',data=open('brochure.pdf','rb').read())
            mail.send(msg)
