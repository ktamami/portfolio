from flask import Flask, render_template, request
import datetime
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from dotenv import load_dotenv
load_dotenv()

mail_from = os.environ.get("MAIL_FROM")
password = os.environ.get("PASS")
mail_to = os.environ.get("MAIL_TO")
charset = "iso-2022-jp"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
    current_year = datetime.datetime.now().year
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        my_msg = MIMEText(f"おめでとう！メッセージが来たよ！\n\n"
                          f"お名前：　　　　{name}さん\n"
                          f"メールアドレス：{email}\n"
                          f"メッセージ：　　{message}",
                          "plain", charset)
        my_msg['Subject'] = Header(f"【🍕新着🍕】{name}さん", charset)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=mail_from, password=password)
            connection.sendmail(from_addr=mail_from, to_addrs=mail_to, msg=my_msg.as_string())
        return render_template("index.html", year=current_year)
    return render_template("index.html", year=current_year)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
