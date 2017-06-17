## 038

Snippet to add Twitter login to your Flask app. Basically I got [this](https://github.com/lepture/flask-oauthlib/blob/master/example/twitter.py) working ([myreadinglist app](https://pybit.es/codechallenge16_review.html)) and adapted it slightly when testing.

### Steps

* Create [Twitter app](https://apps.twitter.com/app/new), see printscreen below, note the Callback URL.

* Note down consumer_key and consumer_secret

* Set env vars (and/or persist them in your .bashrc):

        $ export PYB_100D_TW_KEY=abc
        $ export PYB_100D_TW_SECRET=def
        $ export PYB_100D_APP_SECRET=ghi

* Start app:
    
        $ python app.py

### Demo

Create app:

![twitter login 1](sample/step1.png)

Login:

![twitter login 2](sample/step2.png)

Twitter asks you to authorize the app:

![twitter login 3](sample/step3.png)

Logout:

![twitter login 4](sample/step4.png)

### TODO

Do actual stuff with Twitter API (load feed, post, etc)
