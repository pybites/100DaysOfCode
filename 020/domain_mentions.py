import os

from twython import TwythonStreamer

CONSUMER_KEY = os.environ["CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

DOMAIN = 'pybit.es'
MSG = '''A new mention of {domain}:
{user} (name: {name} / followers {followers}) tweeted: {tweet_text}
Link to tweet: https://twitter.com/{user}/status/{tweet_id}'''


class MyStreamer(TwythonStreamer):
    ''' https://twython.readthedocs.io/en/latest/usage/streaming_api.html '''

    def on_success(self, data):
        user = data['user']['screen_name'].encode('utf-8')
        name = data['user']['name'].encode('utf-8')
        followers = data['user']['followers_count']
        tweet_text = data['text'].encode('utf-8')
        tweet_id = data['id_str'].encode('utf-8')
        notification = MSG.format(domain=DOMAIN,
                                   user=user,
                                   name=name,
                                   followers=followers,
                                   tweet_text=tweet_text,
                                   tweet_id=tweet_id)
        # TODO send to slack :)

    def on_error(self, status_code, data):
        print('An error occurred: {}, exiting'.format(status_code))
        self.disconnect()


if __name__ == "__main__":

    stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                        ACCESS_TOKEN, ACCESS_SECRET)

    # https://dev.twitter.com/streaming/overview/request-parameters#track
    domain = DOMAIN.replace('.', ' ')
    stream.statuses.filter(track=domain)
