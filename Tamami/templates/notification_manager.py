import pywhatkit
from twilio.rest import Client
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.environ.get("TWILIO_FROM")
TWILIO_TO = os.environ.get("TWILIO_TO")
WHATSAPP_TO = os.environ.get("WHATSAPP_TO")

current_hour = datetime.datetime.today().hour
print(current_hour + 1)

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_whatsapp(self, text):
        if current_hour == 23:
            pywhatkit.sendwhatmsg(WHATSAPP_TO, text, 00, 00)
        else:
            pywhatkit.sendwhatmsg(WHATSAPP_TO, text, current_hour+1, 00)

    def send_sms(self, text):
        self.client.messages.create(
            from_=TWILIO_FROM,
            body=text,
            to=TWILIO_TO
        )
