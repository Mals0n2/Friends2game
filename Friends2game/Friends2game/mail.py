from flask import url_for
from Friends2game import app
from flask_mail import Mail, Message

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465  # Port for SMTP (SSL)
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "infosportybuddies@gmail.com"
app.config["MAIL_PASSWORD"] = "htysutkbluguliwy"

mail = Mail(app)


def send_registration_email(email):
    msg = Message(
        "Pomyslna rejestracja", sender="infosportybuddies@gmail.com", recipients=[email]
    )
    msg.body = "Dziekujemy za rejestracje w Friends2game! Teraz mozesz zalogowac sie na swoje konto."
    mail.send(msg)


def send_reset_password_email(email, serializer):
    token_data = {"email": email}
    token = serializer.dumps(email)
    reset_link = url_for("new_pass", token=token, _external=True)

    msg = Message("Reset Password", sender="infosportybuddies@gmail.com", recipients=[email])
    msg.body = f"Kliknij w link, aby zresetowac haslo do konta: {reset_link}"
    mail.send(msg)
