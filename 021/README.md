## 021

Script to go through all our 100DaysOfCode repo's Python script and list for each module in which script(s) it's used and its origin (stdlib, pypi, own module).

Output so far:

		__future__   | stdlib | 021
		codecs       | stdlib | 001
		collections  | stdlib | 001, 021
		common       | own    | 014, 017
		config       | own    | 007
		configparser | stdlib | 020
		contextlib   | stdlib | 001, 016, 021
		csv          | stdlib | 001
		datetime     | stdlib | 005, 007, 009, 012, 013, 017, 018
		email        | stdlib | 011
		feedparser   | pypi   | 014
		flask        | pypi   | 013
		glob         | stdlib | 003, 021
		imageio      | pypi   | 003
		importlib    | stdlib | 021
		ipaddress    | stdlib | 002
		logging      | stdlib | 007, 020
		os           | stdlib | 007, 009, 012, 013, 014, 015, 017, 018, 021
		paramiko     | pypi   | 016
		pprint       | stdlib | 013
		pyperclip    | pypi   | 004
		pytz         | pypi   | 007, 012, 013
		re           | stdlib | 005, 007, 009, 015, 021
		requests     | pypi   | 005, 007, 009, 012, 013
		safari       | own    | 018
		slacker      | pypi   | 020
		smtplib      | stdlib | 011
		socket       | stdlib | 017, 018
		ssl          | stdlib | 001, 017, 018
		stdlib       | own    | 021
		sys          | stdlib | 001, 003, 005, 007, 009, 014, 015, 017, 018, 021
		time         | stdlib | 014, 015
		titles       | own    | 018
		tweepy       | pypi   | 007
		twython      | pypi   | 020
		urllib       | stdlib | 015, 017, 018
		weather      | own    | 013
		xml          | stdlib | 017, 018

		stdlib    :  22 (57.9%)
		pypi      :  10 (26.3%)
		own       :   6 (15.8%)
		------------------------------
		Total: 38
