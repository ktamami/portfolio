from flask import Flask, render_template, request
import datetime
import notification_manager

notification_manager = notification_manager.NotificationManager()

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def contact():
    current_year = datetime.datetime.now().year
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        text = f"📩 You got a message via 🍕\n\n" \
               f"Name: {name} san\n" \
               f"Email: {email}\n" \
               f"{message}"
        notification_manager.send_sms(text)
        return render_template("index.html", year=current_year)
    return render_template("index.html", year=current_year)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
