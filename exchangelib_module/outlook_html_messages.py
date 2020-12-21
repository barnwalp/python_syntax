from exchangelib import Account, Message, HTMLBody, Credentials
from exchangelib import Configuration, DELEGATE
import os


# getting the sensitive information from enviornment variables
# stored in the .bash_profile
outlook_user = os.environ.get('OUTLOOK_USER')
outlook_password = os.environ.get('OUTLOOK_PASS')
outlook_server = os.environ.get('OUTLOOK_SERVER')
outlook_email = os.environ.get('OUTLOOK_EMAIL')

# Using the necessary credential and configuration to connect to
# the exchange server
credentials = Credentials(username=outlook_user, password=outlook_password)
config = Configuration(server=outlook_server,
                       credentials=credentials)
account = Account(primary_smtp_address=outlook_email,
                  config=config, autodiscover=False,
                  access_type=DELEGATE)

msg = Message(
    account=account,
    subject="HTML formatted mail",
    body=HTMLBody(
        """
        <html>
            <body>
                <h1>Hey! straight from the HTML</h1
            </body
        </html>
        """),
    to_recipients=['barnwalp@indianoil.in']
)
msg.send_and_save()
