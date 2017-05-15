## Progress Log

| Day | Date | Created | Learned |
| --- | --- | --- | --- |
| 001 | Mar 30, 2017 | [script to check if tip already submitted to @python_tip](001) | Urlopen, 2vs3, csv parsing, namedtuples, contextlib |
| 002 | Mar 31, 2017 | [script to print out valid IPs of a specified user specified network](002) | ipaddress, simplifying and automating tedious/manual process |
| 003 | Apr 01, 2017 | [script to generate a gif from various png/jpg images](003) | useful for blog, awesome: pip install imageio, cli arg interface is more code :) |
| 004 | Apr 02, 2017 | [script that converts a text list to a text string](004) | useful for tedious sysadmin tasks. Pyperclip is used to read in a list copied to clipboard and convert it to a single line string separated by spaces. |
| 005 | Apr 03, 2017 | [script to create a 100DaysOfCode tweet](005) | takes a date or defaults to today, reads this LOG file in and creates a tweet about our progress (to be automated) |
| 006 | Apr 04, 2017 | [simple reusable code snippet to print a dict](006) | reusable code snippet to print the keys and values of a dict. Includes a demo dict. Short and sweet. |
| 007 | Apr 05, 2017 | [script to automatically tweet 100DayOfCode progress tweet](007) | twitter API, manage config outside source, logging, date parsing and timezones |
| 008 | Apr 06, 2017 | [reusable python flask html template for printing a dict](008) | reusable python flask html template that uses a for loop to print dict contents - flask |
| 009 | Apr 07, 2017 | [interactive script to create a new Pelican blog article](009) | lot of known concepts, but nice to bring a lot of functionality together, and above all a really useful script for our blog |
| 010 | Apr 08, 2017 | [script to spot cheap @transavia flights using their #API](010) | this was a nice exercise, and a very useful script for a monitoring cron job. TODO: wrap it in a Flask web app. Some modules I explored: calendar, datetime, dateutil.relativedelta, requests_cache |
| 011 | Apr 09, 2017 | [generic script to email the contents of a text file](011) | a script that uses your gmail account to email the contents of a text file. Current use case is to email web scraped data. smtplib, email, MIME |
| 012 | Apr 10, 2017 | [using OpenWeatherMap #API to compare weather in Australia vs Spain](012) | OpenWeatherMap API, pytz for timezone handling, datetime.utcfromtimestamp to parse unix timestamp to datetime, Google confirms sunset / sunrise times correct :) |
| 013 | Apr 11, 2017 | [simple #Flask app to compare weather of 2 cities (using OpenWeatherMap #API)](013) | This was a nice follow-up of 012, making it more generic (support any city), using Jinja templating, Flask form handling, and of course a good chunk of timezone handling (for sunset and sunrise) |
| 014 | Apr 12, 2017 | [script to automatically tweet out new @lynda (#Python) titles](014) | feedparser is awesome. Want to run it with filter on Python. Abstracted twitter config away in repo's common dir (re-use). |
| 015 | Apr 13, 2017 | [script to calculate the number of posts on @pybites](015) | small script but some interesting things: urllib.request.urlretrieve (stdlib), test and cache option (using os.start for cache file age), re.findall, dict comprehension. |
| 016 | Apr 14, 2017 | [script to #ssh to specified IPs and check their hostnames](016) | Generic script to ssh to a list of IPs and run a command using paramiko. This can obviously  be altered for many purposes, not just hostname checks. The code is quite flexible. |
| 017 | Apr 15, 2017 | [script to automatically tweet out new @safari Python titles](017) | like the Lynda one, parsing an RSS feed, but only stdlib, so no feedparser, using xml.etree.ElementTree, no requests, using urllib. Also nice exercise converting and calculating with datetime / timedelta |
| 018 | Apr 16, 2017 | [using #pytest to write tests for @safari RSS scraper (day 017)](018) | testing is a good skill to keep honing. It lets you define your design better and look for edge cases that saves debug headaches later on. pytest is nice, to be further explored ... |
| 019 | Apr 17, 2017 | [paste in a list of numbers from the clipboard, sort to ascending then copy back to clipboard @AlSweigart #pyperclip #script](019) | simple yet useful script to read in a list of numbers from the clipboard, sort them into ascending order then copy the sorted list back to clipboard. Numbers need to initally be copied with a new line between them |
| 020 | Apr 18, 2017 | [monitor #Twitter and post to #slack each time our domain gets mentioned](020) | useful script and exercise. Twitter + Slack API combined == awesome. Aim was to clone/ replace mediatrigger.io (got bothered free trial will end one day ...) |
| 021 | Apr 19, 2017 | [script to make an index of modules used for this challenge (stdlib >50%)](021) | collections (defaultdict, Counter), os.path, regex, glob, os.listdir, is_std_lib function (from SO), f-strings. Nice to see we heavily use stdlib, Python == batteries included |
| 022 | Apr 20, 2017 | [create and paste #Amazon affiliation link to clipboard #pyperclip @AlSweigart](022) | nice little utility to copy an take Amazon link from clipboard, convert it into an affiliation link and paste it back to clipboard |
| 023 | Apr 21, 2017 | [use Counter to count the most common words in a file](023) | we did some time ago, collections module is awesome |
| 024 | Apr 22, 2017 | [generate color hex codes from random RGBs and color terminal text](024) | nice play with generators, RGB to hex with format, and colorizing the terminal with the [colored](https://pypi.python.org/pypi/colored) package. This could be useful for future cli apps | 
| 025 | Apr 23, 2017 | [Simple test #database generator script #python #sqlite #contextmanager](025) | Script to generate a quick, test sqlite3 database with 1 table and 3 columns. Can be customised and expanded to suit your needs. Definitely useful for playing around with persistent data. |
| 026 | Apr 24, 2017 | [Simple script to retrieve #movie data from OMDb #API](026) | Get OMDB for movie data, query API by IMDB ID or title. Returns text or html. Uses request_cache to limit repeated calls to API. Could help some folks taking this [this week's challenge](http://pybit.es/codechallenge16.html) |
| 027 | Apr 25, 2017 | [rough script to query the #warcraft #API for a character's mounts](027) | A VERY rough and simple script to query the World of Warcraft API and pull the collected mounts of a specific character. Lots of room to expand this with stripping of JSON data and specifying which data to pull. Just some fun with a new and unconmmon API! |
| 028 | Apr 26, 2017 | [Jupyter notebook to plot and list new #Python titles on @safari by month](028) | Learning: parsing a Twitter CSV backup dump (@newsafaribooks account), matplotlib, collections, hacking iPython css |
| 029 | Apr 27, 2017 | [Traffic Lights script to demo #itertools cycle](029) | A nice and easy script to simulate traffic lights using `itertools.cycle` and other stdlib modules cycle. Itertools rocks! |
| 030 | Apr 28, 2017 | [Script to import movie csv file into an sqlite database](030) | sqlite3, csv, nice groundwork for Flask auto-complete I am working on |
| 031 | Apr 29, 2017 | [Simple and reusable #Python #script to move all files from one folder to another](031) | A simple but useful script to move all files from one diretory to another using shutil and os. Currently using this in a cron job to mv server log files into an archive folder to keep the log dir clean. |
| 032 | Apr 30, 2017 | [#Flask #jQuery movie autocomplete](032) | Used DB of day 30. Learned Jinja template extending / inheritance. Nice plugin for mixing Flask/JS: Flask-JSGlue. TODO: upon select movie direct to page showing movie info. |
| 033 | May 01, 2017 | [I need to drink more water at work so I wrote a #Python #script to remind (spam) me every hour](033) | A simple script using MIME and a cron job (read the readme.txt) to remind me to drink more water at work! Doesn't email on the weekends or before/after hours. Over the top? Maybe. Satisfying? Hell yes. |
| 034 | May 02, 2017 | [Import a #podcast feed into a DB table with #SQLAlchemy](034) | Part of the this week's code challenge solution. Found it useful enough to extract this bit as separate nudget |
| 035 | May 03, 2017 | [Text replacer script using #pyperclip by @AlSweigart](035) | A simple script that will replace any text or characters in text that you have copied to the clipboard. Check out the readme.txt file for more detail. |
| 036 | May 04, 2017 | [Use #Python #pickle to store and retrieve a defaultdict](036) | Nice and easy persistence tool. Using it with context manager to write random log entries. Each time the script is run the data pickle file gets updates. To get random entries I used a generator. |
| 037 | May 05, 2017 | [#Python script to pull down an #XML feed and save it](037) | This is an extremely simple script that uses the requests module to pull down an XML feed and write it as is to your local disk for later use by a scraper etc. Created while working on [PCC17](http://pybit.es/codechallenge17.html) |
| 038 | May 06, 2017 | [Simple #Twitter login for your #Flask app using flask_oauthlib](038) | This was a nice addition to [myreadinglist app](http://pybit.es/codechallenge16_review.html): easy authentication flow. Also want to leverage it to show recommended books from followers of the Twitter logged in user. |
| 039 | May 07, 2017 | [#Python script to give you every valid dictionary match of a specified letter sequence](039) | A script that uses itertools permutations to check whether a user specified sequence of letters (could be a word!) can be used to make a word or words from the English dictionary. |
| 040 | May 08, 2017 | [PyBites podcast challenge 17 in less than 100 LOC using #scheduler and #shelve](040) | Rewriting a script with different modules (originally we used SQLAlchemy/SQlite) and with LOC constraint, was fun | 
| 041 | May 09, 2017 | [Script to check all possible combinations of letters and match against a dictionary. Great for #scrabble](041) | Similar to day 039 but this time it checks all combinations of letters of all lengths, not just the length of the given string. It's a great way to ruin a game of Words with Friends! |
| 042 | May 10, 2017 | [Using #Python icalendar module to parse FB birthdays cal (ics file)](042) | Prework to download all birthdays into a Flask SQLAlchemy app |
| 043 | May 11, 2017 | [Script to read in a list and reverse its contents](043) | I thought it'd be fun to see if I could read in a list of excel cells and reverse their order then paste them out. It's not perfect but it works! |
| 044 | May 12, 2017 | [Random name generator, reading in a bunch of names from a CSV file](044) | I used this for Flask SQLAlchemy birthday app to anonymize the data (real dates, fake names), csv source [here](https://raw.githubusercontent.com/yorkshiretwist/WTester/master/WTester/Helpers/CSV_Database_of_First_Names.csv) (TODO: could use faker module)|
| 045 | May 13, 2017 | [#steam XML feed scraper for new #game releases](045) | A simple script to parse the Steam XML feed for new game releases. Script will store the title and URL data in an SQLite DB. Readme.txt for more info. |
| 046 | May 14, 2017 | [Get friends updates from Goodreads #API #books](046) | Base work for this week's challenge 18 to get book recommendations from Goodreads (requires oauth) |
| 047 | May 15, 2017 | [TITLE](047) | LEARNING |
| 048 | May 16, 2017 | [TITLE](048) | LEARNING |
| 049 | May 17, 2017 | [TITLE](049) | LEARNING |
| 050 | May 18, 2017 | [TITLE](050) | LEARNING |
| 051 | May 19, 2017 | [TITLE](051) | LEARNING |
| 052 | May 20, 2017 | [TITLE](052) | LEARNING |
| 053 | May 21, 2017 | [TITLE](053) | LEARNING |
| 054 | May 22, 2017 | [TITLE](054) | LEARNING |
| 055 | May 23, 2017 | [TITLE](055) | LEARNING |
| 056 | May 24, 2017 | [TITLE](056) | LEARNING |
| 057 | May 25, 2017 | [TITLE](057) | LEARNING |
| 058 | May 26, 2017 | [TITLE](058) | LEARNING |
| 059 | May 27, 2017 | [TITLE](059) | LEARNING |
| 060 | May 28, 2017 | [TITLE](060) | LEARNING |
| 061 | May 29, 2017 | [TITLE](061) | LEARNING |
| 062 | May 30, 2017 | [TITLE](062) | LEARNING |
| 063 | May 31, 2017 | [TITLE](063) | LEARNING |
| 064 | Jun 01, 2017 | [TITLE](064) | LEARNING |
| 065 | Jun 02, 2017 | [TITLE](065) | LEARNING |
| 066 | Jun 03, 2017 | [TITLE](066) | LEARNING |
| 067 | Jun 04, 2017 | [TITLE](067) | LEARNING |
| 068 | Jun 05, 2017 | [TITLE](068) | LEARNING |
| 069 | Jun 06, 2017 | [TITLE](069) | LEARNING |
| 070 | Jun 07, 2017 | [TITLE](070) | LEARNING |
| 071 | Jun 08, 2017 | [TITLE](071) | LEARNING |
| 072 | Jun 09, 2017 | [TITLE](072) | LEARNING |
| 073 | Jun 10, 2017 | [TITLE](073) | LEARNING |
| 074 | Jun 11, 2017 | [TITLE](074) | LEARNING |
| 075 | Jun 12, 2017 | [TITLE](075) | LEARNING |
| 076 | Jun 13, 2017 | [TITLE](076) | LEARNING |
| 077 | Jun 14, 2017 | [TITLE](077) | LEARNING |
| 078 | Jun 15, 2017 | [TITLE](078) | LEARNING |
| 079 | Jun 16, 2017 | [TITLE](079) | LEARNING |
| 080 | Jun 17, 2017 | [TITLE](080) | LEARNING |
| 081 | Jun 18, 2017 | [TITLE](081) | LEARNING |
| 082 | Jun 19, 2017 | [TITLE](082) | LEARNING |
| 083 | Jun 20, 2017 | [TITLE](083) | LEARNING |
| 084 | Jun 21, 2017 | [TITLE](084) | LEARNING |
| 085 | Jun 22, 2017 | [TITLE](085) | LEARNING |
| 086 | Jun 23, 2017 | [TITLE](086) | LEARNING |
| 087 | Jun 24, 2017 | [TITLE](087) | LEARNING |
| 088 | Jun 25, 2017 | [TITLE](088) | LEARNING |
| 089 | Jun 26, 2017 | [TITLE](089) | LEARNING |
| 090 | Jun 27, 2017 | [TITLE](090) | LEARNING |
| 091 | Jun 28, 2017 | [TITLE](091) | LEARNING |
| 092 | Jun 29, 2017 | [TITLE](092) | LEARNING |
| 093 | Jun 30, 2017 | [TITLE](093) | LEARNING |
| 094 | Jul 01, 2017 | [TITLE](094) | LEARNING |
| 095 | Jul 02, 2017 | [TITLE](095) | LEARNING |
| 096 | Jul 03, 2017 | [TITLE](096) | LEARNING |
| 097 | Jul 04, 2017 | [TITLE](097) | LEARNING |
| 098 | Jul 05, 2017 | [TITLE](098) | LEARNING |
| 099 | Jul 06, 2017 | [TITLE](099) | LEARNING |
| 100 | Jul 07, 2017 | [TITLE](100) | LEARNING |
