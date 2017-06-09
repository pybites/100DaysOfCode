## 072

### Packt Ebook Download Manager

For the [Packt free learning challenge](https://pybit.es/codechallenge22.html) I'd like: 

1. Notification mail or tweet (TODO)

2. Download manager

3. Auto-add new books (captcha, kinda game over)

I tackled number 2 first, here is [my first go](https://github.com/pybites/100DaysOfCode/blob/master/072/packt.py). 

Wow login with requests is easy! Thanks Julian for [reminding me](https://pybit.es/requests-session.html).

### Example

	$ python packt.py
	PACKT DOWNLOAD MANAGER

	Logging in
	Retrieving books

	Seach for a book (q for exit): dta
	No matches, try again

	Seach for a book (q for exit): data
	1) Learning Data Mining with Python [eBook]
	2) R Data Visualization Cookbook [eBook]
	3) Practical Data Science Cookbook [eBook]
	4) Data Analysis with R [eBook]
	5) ASP.NET Data Presentation Controls Essentials [eBook]
	6) Implementing Splunk: Big Data Reporting and Development for Operational Intelligence [eBook]
	Choose book (n for new search): 1
	1) https://www.packtpub.com/ebook_download/21201/pdf
	2) https://www.packtpub.com/ebook_download/21201/epub
	3) https://www.packtpub.com/ebook_download/21201/mobi
	Choose url (c to cancel): 1
	Downloading https://www.packtpub.com/ebook_download/21201/pdf
	Saving to /Users/bbelderb/Documents/books/Packt/learning-data-mining-with-python.pdf
	Choose book (n for new search): n

	Seach for a book (q for exit): python
	1) Expert Python Programming - Second Edition [eBook]
	2) Modern Python Cookbook [eBook]
	3) Python GUI Programming Cookbook [eBook]
	4) What You Need to Know about Python [eBook]
	5) Raspberry Pi Cookbook for Python Programmers [eBook]
	6) Learning Python Application Development [eBook]
	7) Learning Robotics Using Python [eBook]
	...
	many more (thanks Packt!)
	...
	Choose book (n for new search): 1
	1) https://www.packtpub.com/ebook_download/25257/pdf
	2) https://www.packtpub.com/ebook_download/25257/epub
	3) https://www.packtpub.com/ebook_download/25257/mobi
	Choose url (c to cancel): 3
	Downloading https://www.packtpub.com/ebook_download/25257/mobi
	Saving to /Users/bbelderb/Documents/books/Packt/expert-python-programming-second-edition.mobi
	Choose book (n for new search): 22
	1) https://www.packtpub.com/ebook_download/20125/pdf
	2) https://www.packtpub.com/ebook_download/20125/epub
	3) https://www.packtpub.com/ebook_download/20125/mobi
	Choose url (c to cancel): 1
	Downloading https://www.packtpub.com/ebook_download/20125/pdf
	Saving to /Users/bbelderb/Documents/books/Packt/functional-python-programming.pdf
	Choose book (n for new search): n

	Seach for a book (q for exit): postgres
	1) PostgreSQL 9 Admin Cookbook [eBook]
	2) Learning PostgreSQL [eBook]
	Choose book (n for new search): 2
	1) https://www.packtpub.com/ebook_download/22041/pdf
	2) https://www.packtpub.com/ebook_download/22041/epub
	3) https://www.packtpub.com/ebook_download/22041/mobi
	Choose url (c to cancel): 1
	Downloading https://www.packtpub.com/ebook_download/22041/pdf
	Saving to /Users/bbelderb/Documents/books/Packt/learning-postgresql.pdf
	Choose book (n for new search): 1
	1) https://www.packtpub.com/ebook_download/6088/pdf
	2) https://www.packtpub.com/ebook_download/6088/epub
	3) https://www.packtpub.com/ebook_download/6088/mobi
	Choose url (c to cancel): c
	Choose book (n for new search): n

	Seach for a book (q for exit): science
	1) Practical Data Science Cookbook [eBook]
	Choose book (n for new search): n

	Seach for a book (q for exit): machine
	1) Practical Machine Learning [eBook]
	2) Machine Learning with R - Second Edition [eBook]
	3) Machine Learning with Spark [eBook]
	4) Python Machine Learning [eBook]
	5) Building Machine Learning Systems with Python [eBook]
	Choose book (n for new search): 6
	Wrong input, please try again
	Choose book (n for new search): f
	Wrong input, please try again
	Choose book (n for new search): 5
	1) https://www.packtpub.com/ebook_download/11703/pdf
	2) https://www.packtpub.com/ebook_download/11703/epub
	3) https://www.packtpub.com/ebook_download/11703/mobi
	Choose url (c to cancel): 1
	Downloading https://www.packtpub.com/ebook_download/11703/pdf
	Saving to /Users/bbelderb/Documents/books/Packt/building-machine-learning-systems-with-python.pdf
	Choose book (n for new search): n
	Seach for a book (q for exit): q
	Bye

Finder:

![downloasds](out-folder.png)
