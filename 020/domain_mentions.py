import configparser
import logging

from slacker import Slacker
from twython import TwythonStreamer

config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config['Twitter']['cs_key']
CONSUMER_SECRET = config['Twitter']['cs_secret']
ACCESS_TOKEN = config['Twitter']['acc_token']
ACCESS_SECRET = config['Twitter']['acc_secret']
SLACK_TOKEN = config['Slack']["token"]

CHANNEL = '#pybites-mentions'
DOMAIN = ('pybit', 'es')
MSG = '''A new mention of {domain}:

{user} (name: {name} / followers {followers}) tweeted:
{tweet_text}

Link to tweet: https://twitter.com/{user}/status/{tweet_id}
'''

slack = Slacker(SLACK_TOKEN)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='bot.log')


def create_post(data):
    tweet_text = data['text']
    tweet_id = data['id_str']
    user = data['user']['screen_name']
    name = data['user']['name']
    followers = data['user']['followers_count']
    return MSG.format(domain='.'.join(DOMAIN),
                      user=user,
                      name=name,
                      followers=followers,
                      tweet_text=tweet_text,
                      tweet_id=tweet_id)


class MyStreamer(TwythonStreamer):
    ''' https://twython.readthedocs.io/en/latest/usage/streaming_api.html '''

    def on_success(self, data):
        post = create_post(data)
        logging.debug(post)
        try:
            slack.chat.post_message(CHANNEL, post, as_user=True)
        except Exception as exc:
            logging.error('\nOH NO!')
            logging.error('an exception occurred in slack.chat.post_message({}, {}, as_user=True)'.format(CHANNEL, post))
            logging.error('exception raised by slack API was:\n{}\n'.format(exc))

    def on_error(self, status_code, data):
        print('An error occurred: {}, exiting'.format(status_code))
        self.disconnect()


if __name__ == "__main__":

    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                        ACCESS_TOKEN, ACCESS_SECRET)

    # https://dev.twitter.com/streaming/overview/request-parameters#track
    stream.statuses.filter(track=' '.join(DOMAIN))
