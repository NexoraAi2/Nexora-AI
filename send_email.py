import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # Set up the server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.starttls()

    # Login to Gmail account
    server.login("chefdemi003@gmail.com", "<Vivi@9121>")

    # Set up the message
    msg = MIMEMultipart()
    msg['From'] = "chefdemi003@gmail.com"
    msg['To'] = "vinayakgautham@gmail.com"
    msg['Subject'] = "Daily Crypto Report"

    # Add body to the email
    body = "Here is your faily crypto analysis report."
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server.send_message(msg)
    server.quit()

send_email()
