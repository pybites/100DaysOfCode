# from SDK docs
# https://www.twilio.com/docs/libraries/python
import os
import sys

import click
from twilio.rest import Client

ACCOUNT_SID = os.environ.get('TWILIO_SID') or sys.exit('need account sid')
AUTH_TOKEN = os.environ.get('TWILIO_TOK') or sys.exit('need auth token')
CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)
FROM_PHONE = os.environ.get('TWILIO_PHONE') or sys.exit('need Twilio (verified) phone')


@click.command()
@click.option('--phone', help='to phone number (trial = needs to be validated)')
@click.option('--message', help='SMS text message')
@click.option('--media', help='media url (optional)', required=False)
def send_sms(phone, message, media):
    message = CLIENT.messages.create(
        from_=FROM_PHONE,
        to=phone,
        body=message,
        media_url=media,
    )
    print(message.sid)


if __name__ == '__main__':
    send_sms()
