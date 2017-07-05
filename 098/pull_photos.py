import os
import sys

from instagram.client import InstagramAPI

client_id = os.environ.get('IG_100D_CLIENT_ID')
client_secret = os.environ.get('IG_100D_CLIENT_SECRET')

IG_USER_ID = '4799'  # bbelderbos
SCOPE = ''
REDIRECT_URL = 'http://127.0.0.1:5000'

if not client_id or not client_secret:
    print('Please set the following env vars: ')
    print('IG_100D_CLIENT_ID')
    print('IG_100D_CLIENT_SECRET')
    sys.exit(1)


def _get_access_token():
    api = InstagramAPI(client_id=client_id,
                       client_secret=client_secret,
                       redirect_uri=REDIRECT_URL)
    redirect_uri = api.get_authorize_login_url(scope=SCOPE)

    print("Visit this page in browser and authorize access:\n", redirect_uri)
    code = input("Paste in code in query string after redirect: ").strip()

    access_token, user_info = api.exchange_code_for_access_token(code)

    return access_token


if __name__ == '__main__':
    # this script lets you use access_token from env or get it on the fly
    # you can also use:
    # https://github.com/facebookarchive/python-instagram/blob/master/get_access_token.py
    access_token = os.environ.get('IG_100D_ACCESS_TOKEN')
    if not access_token:
        _get_access_token()

    api = InstagramAPI(access_token=access_token)

    recent_media, next_ = api.user_recent_media(user_id=IG_USER_ID, count=50)

    for media in recent_media:
        print('thumb url: ', media.get_thumbnail_url())  # instagram/model.py
        print('\tstd res url: ', media.get_standard_resolution_url())
        print()
