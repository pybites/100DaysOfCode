This is a pretty simple script. I've reused code from my previous automated emailing scripts and just tweaked it for this purpose.

The real magic is in the cron job I have set up to run this code during my work day. This is the line in my crontab:

0 8-16 * * 1-5 cd /opt/development/drink_water && /usr/bin/python3 water_reminder.py

This will result in the email being sent between the hours of 08:00 and 16:00, Mon - Fri. (Not on the weekend! That's beer time!).

Another question you may be asking is "why not just use a repeated alarm on your phone?". I was actually asked this by a good mate... to which I answered "Now where's the bloody fun in that?".

Keep Calm and Code in Python!

-- Julian
