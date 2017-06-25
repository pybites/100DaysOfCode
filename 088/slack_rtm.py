"""
Slack Real Time Messaging API
https://api.slack.com/rtm

And snippet from
https://gist.github.com/devStepsize/b37376c8263a02359401e6f0c155a3ea

Typing in 'test message for bot' in a Slack channel this captures it like:

[{'channel': 'C4SFQJJ9Z',
  'source_team': 'T4SJVFM8C',
  'team': 'T4SJVFM8C',
  'text': 'test message for bot',
  'ts': '1498393738.661513',
  'type': 'message',
  'user': ''}]

Going to use this for a simple karma app :)
"""
import os
from pprint import pprint as pp
import time

from slackclient import SlackClient

SLACK_CLIENT = SlackClient(os.environ.get('SLACK_KARMA'))

if SLACK_CLIENT.rtm_connect():
    while True:
        msg = SLACK_CLIENT.rtm_read()
        pp(msg)
        time.sleep(1)
else:
    print('Connection Failed, invalid token?')
