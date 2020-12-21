from exchangelib import Credentials, Account, Message, Mailbox
from exchangelib import DELEGATE, Configuration
# from exchangelib.items import SEND_ONLY_TO_ALL, SEND_ONLY_TO_CHANGED
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

# for item in account.inbox.all().order_by('-datetime_received')[:10]:
#    print(item.subject, item.sender, item.datetime_received)

# Sending simple text mail to to, cc & bcc list
msg = Message(
    account=account,
    subject='another test mail',
    body='this is an another random body for testing mail services',
    to_recipients=[
        # Mailbox(email_address='shubhams@indianoil.in')
        Mailbox(email_address='barnwalp@indianoil.in')
    ],
    cc_recipients=['barnwalp.ioc@gmail.com', 'barnwalp@indianoil.in'],
    bcc_recipients=['suno.pankaj@gmail.com']
)

# it will sent and save the mail in the sent folder
msg.send_and_save()

# replying to a mail that are stored in the mailbox, i.e. they have a
# valid item ID
msg_in_mail = account.inbox.get(subject='Fwd: Ethanol Handling')
msg_in_mail.reply(
    subject='RE: another test mail',
    body='reply tested-2',
    to_recipients=['barnwalp@indianoil.in',
                   'barnwalp.ioc@gmail.com'
                   ]
)

# replying to all recipients
msg_in_mail.reply_all(subject='another test mail', body='reply all tested')

msg_in_mail.forward(
    subject='FW: Ethanol Handling',
    body='Hey, look at this',
    to_recipients=['barnwalp.ioc@gmail.com']
)
