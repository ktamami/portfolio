from flask import Flask, render_template, request
import datetime
from twilio.rest import Client
import os
from dotenv import load_dotenv
import time
load_dotenv()

tamami = os.environ.get("TAMAMI")
twilio_sid = os.environ.get("TWILIO_SID")
twilio_token = os.environ.get("TWILIO_TOKEN")
messaging_service_sid = os.environ.get("MESSAGING_SERVICE_SID")
phone = os.environ.get("PHONE")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
    current_year = datetime.datetime.now().year
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        my_msg = (f"🍕\n"
                  f"{name}さん\n"
                  f"{email}\n"
                  f"{message}")
        twilio_client = Client(twilio_sid, twilio_token)
        twilio_client.messages.create(
            messaging_service_sid=messaging_service_sid,
            body=my_msg,
            to=phone
        )
        time.sleep(10)
        return render_template("index.html", year=current_year, tamami=tamami)
    return render_template("index.html", year=current_year, tamami=tamami)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
