import smtplib, ssl, getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(html_file):
    port = 587
    password = getpass.getpass()
    # input("Type your password and press enter: ")

    smtp_server = "smtp.gmail.com"
    sender_email = "pythonemailtest098@gmail.com"
    receiver_email = "pythonemailtest098@gmail.com"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Today's News!"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    Subject: Today's News!

    Hi,
    This message is sent from Python."""

    with open(html_file, "r") as f:
        html = f.read()

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print("Email failed to send")
    finally:
        server.quit()

# context = ssl.create_default_context()

# server = smtplib.SMTP_SSL(smtp_server, port, context)
# server.connect(smtp_server, port)
# server.ehlo()
# server.set_debuglevel(1)
# server.login(sender_email, password)
# server.sendmail(sender_email, receiver_email, message)
# server.quit()

# with smtplib.SMTP_SSL(smtp_server, port, context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)