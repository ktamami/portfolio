from flask import Flask, render_template, request
import datetime
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

twilio_sid = os.environ.get("TWILIO_SID")
twilio_token = os.environ.get("TWILIO_TOKEN")
messaging_service_sid = os.environ.get("MESSAGING_SERVICE_SID")
phone = os.environ.get("PHONE")
charset = "iso-2022-jp"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
    current_year = datetime.datetime.now().year
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        my_msg = (f"\nおめでとう！メッセージが来たよ！\n"
                  f"お名前：　　　　{name}さん\n"
                  f"メールアドレス：{email}\n"
                  f"メッセージ：　　{message}")
        twilio_client = Client(twilio_sid, twilio_token)
        message = twilio_client.messages.create(
                messaging_service_sid=messaging_service_sid,
                body=my_msg,
                to=phone
            )
        print(message.status)
        return render_template("index.html", year=current_year)
    return render_template("index.html", year=current_year)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
