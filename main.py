import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
SMTP_SERVER = 'your_smtp_server'
SMTP_PORT = 587
SMTP_USERNAME = 'your_username'
SMTP_PASSWORD = 'your_password'
SENDER_EMAIL = 'sender@example.com'

# CSV file path
CSV_FILE = 'recipients.csv'

# Email content
subject = 'Hello from Python!'
message = 'This is a test email sent using Python.'

# Read recipient emails from CSV file
recipients = []
with open(CSV_FILE, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        recipients.append(row[0])

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = SENDER_EMAIL
msg['To'] = ', '.join(recipients)
msg['Subject'] = subject

# Attach the message to the email
msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(SENDER_EMAIL, recipients, msg.as_string())
    server.close()
    print('Email sent successfully!')
except Exception as e:
    print('Error sending email:', str(e))
