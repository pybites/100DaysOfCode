## 068

### from PyBites import newsletter

Awesome: [@mohhinder](https://twitter.com/mohhinder) translated our `from PyBites import newsletter` into code.

In his own words: 

> Written on iPhone with the Pythonista 3 app as a joke for the PyBites guys, I don't see why it wouldn't work anywhere else though. They always start off their newsletter annoucements with: `from @PyBites import newsletter`, so I turned it into actual code that pulls their feed and opens their latest newsletter in a browser :) 

Original [source](https://gist.github.com/clamytoe/f302c8b042341deb48bab4f3b7645198) and [tweet](https://twitter.com/mohhinder/status/870208685523456000)

### How to install / run

	[bbelderb@macbook 068 (master)]$ python3 -m venv venv && source venv/bin/activate
	(venv) [bbelderb@macbook 068 (master)]$ pip install -r requirements.txt

	(venv) [bbelderb@macbook 068 (master)]$ python
	>>> from PyBites import newsletter
	>>> newsletter()
	05/29/2017 - PyBites of the Week
	http://eepurl.com/cQy06f
	05/22/2017 - PyBites of the Week
	http://eepurl.com/cPJ40D
	,,,
	...
	02/06/2017 - PyBites of the Week
	http://eepurl.com/cAGL2j
	01/30/2017 - PyBites of the Week
	http://eepurl.com/czEmw5
	01/23/2017 - PyBites of the Week
	http://eepurl.com/cyFLgr
	01/16/2017 - PyBites of the Week
	http://eepurl.com/cxGVRz

Then opens our latest PyBites newsletter in the browser.

Thanks Martin!
