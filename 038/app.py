import os
from pprint import pprint as pp
import ssl
import sys

from flask import Flask, render_template, request, g
from flask import session, flash, redirect, url_for
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.secret_key = os.environ.get('PYB_100D_APP_SECRET') or sys.exit('need secret app key')

oauth = OAuth(app)

# urllib.error.URLError: <urlopen error 
#   [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)>
ssl._create_default_https_context = ssl._create_unverified_context


twitter = oauth.remote_app(
    'twitter',
    consumer_key=os.environ.get('PYB_100D_TW_KEY') or sys.exit('need tw key'),
    consumer_secret=os.environ.get('PYB_100D_TW_SECRET') or sys.exit('need tw secret'),
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize'
)


@twitter.tokengetter
def get_twitter_token():
    if 'twitter_oauth' in session:
        resp = session['twitter_oauth']
        return resp['oauth_token'], resp['oauth_token_secret']


@app.before_request
def before_request():
    g.user = None
    if 'twitter_oauth' in session:
        g.user = session['twitter_oauth']


@app.route('/login')
def login():
    # this snippet works better:
    # https://github.com/mitsuhiko/flask-oauth/blob/master/example/tweet.py
    return twitter.authorize(callback=url_for('oauthorized',
                             next=request.args.get('next') or request.referrer or None))


@app.route('/logout')
def logout():
    session.pop('twitter_oauth', None)
    return redirect(request.referrer or url_for('index'))  # fix: redirect to previous url


@app.route('/oauthorized')
def oauthorized():
    resp = twitter.authorized_response()
    if resp is None:
        flash('You denied the request to sign in.')
    else:
        session['twitter_oauth'] = resp
    #return redirect(url_for('index'))
    return redirect(request.args.get('next')
                    or request.referrer or
                    url_for('index'))  # fix: redirect to previous url


@app.route('/', methods=['GET', 'POST'])
def index():
    if g.user:
        pp(g.user['screen_name'])
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
