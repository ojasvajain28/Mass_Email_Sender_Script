```markdown
# Email Sender

This Python script allows you to send emails to a large number of recipients by reading their email addresses from a CSV file.

## Features

- Sends emails to multiple recipients using a CSV file as the source of email addresses.
- Customizable email subject and message.
- Uses the SMTP protocol for sending emails.
- Handles exceptions and provides error messages in case of failures.

## Requirements

- Python 3.x
- `smtplib` library

## Installation

1. Clone the repository:

```bash
$ git clone https://github.com/your-username/email-sender.git
```

2. Navigate to the project directory:

```bash
$ cd email-sender
```

3. Install the required dependencies:

```bash
$ pip install -r requirements.txt
```

## Usage

1. Place your recipient email addresses in a CSV file, with one email address per row in the first column.

2. Open the `send_email.py` script in a text editor.

3. Update the following variables with your SMTP server details and email credentials:

```python
SMTP_SERVER = 'your_smtp_server'
SMTP_PORT = 587
SMTP_USERNAME = 'your_username'
SMTP_PASSWORD = 'your_password'
SENDER_EMAIL = 'sender@example.com'
CSV_FILE = 'recipients.csv'
```

4. Modify the email subject and message as per your requirements:

```python
subject = 'Hello from Python!'
message = 'This is a test email sent using Python.'
```

5. Save the changes to the script.

6. Run the script:

```bash
$ python send_email.py
```

7. The script will connect to the SMTP server, read the recipient email addresses from the CSV file, and send the email to all recipients.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

