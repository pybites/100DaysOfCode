Set Up Automated Emailer for steam scraper

Use the pull_xml.py file to pull down the newreleases.xml rss file.

Add the following line to crontab (customising the path to your script) to get it to run daily at 20:30.
You'd then preferably run your steamscraper script a few minutes (I gave it 30 mins) after this cron job runs.


CRONTAB ENTRY:

30 20 * * * cd /opt/development/steamscraper && /usr/bin/python3 pull_xml.py
