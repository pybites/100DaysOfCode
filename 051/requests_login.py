#!python3
#requests_login.py is a code snippet/script you can customise to do a request get of a site behind a login.
#For this example file I'm pulling down my home page post listing on freecycle.org.

import requests

#This URL will be the URL that your login form points to with the "action" tag.
POST_LOGIN_URL = 'https://my.freecycle.org/login'

#This URL is the page you actually want to pull down with requests.
REQUEST_URL = 'https://my.freecycle.org/home/posts'


#username-input-name is the "name" tag associated with the username input field of the login form.
#password-input-name is the "name" tag associated with the password input field of the login form.
payload = {
    'username-input-name': 'username',
	'password-input-name': 'password'  #Preferably set your password in an env variable and sub it in.
}

with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=payload)
	r = session.get(REQUEST_URL)
	print(r.text)   #or whatever else you want to do with the request data!
