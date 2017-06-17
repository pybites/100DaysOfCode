## 059

### Twilio API

Playing with the Twilio API = very cool. Got the [example code](https://www.twilio.com/docs/libraries/python) working with a free trial, see [here](send_sms.py).

Two things I ran into:

* Had to register a +1 number, Spanish number could not send SMS:

	> Unable to create record: The From phone number +34... is not a valid, SMS-capable inbound phone number or short code for your account.

* Might consider upgrade as free trial needs all destination numbers to be validated before use:

	> Unable to create record: The number +34... is unverified. Trial accounts cannot send messages to unverified numbers; verify +34... at twilio.com/user/account/phone-numbers/verified, or purchase a Twilio number to send messages to unverified numbers.

### Usage

Using click for the cli arg parsing:

	$ python send_sms.py --help
	Usage: send_sms.py [OPTIONS]

	Options:
	--phone TEXT    to phone number (trial = needs to be validated)
	--message TEXT  SMS text message
	--media TEXT    media url (optional)
	--help          Show this message and exit.

	$ python send_sms.py --phone +34... --message 'Hi from PyBites'
	SM0c30db9166704e3cbb3471e567de2cf1

	$ python send_sms.py --phone +34... --message 'Hi from PyBites again' --media 'https://pybit.es/theme/img/profile.png'
	MM904cda63e1674c7ca69128cf8feb0448

### Result

SMS from Twilio:

![cat pic](catpic.png)
