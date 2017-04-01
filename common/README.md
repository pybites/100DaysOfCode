## Shared scripts

To use one or more scripts in this directory use this code in your DAY_NUMBER/script.py:

	import os
	import sys

	cwd = os.getcwd()
	project_root = os.path.dirname(cwd)
	sys.path.append(project_root)

	from common import shared_script

For example if you want your script to mail out its output on your host, you can use our mail script with above code, then importing it as: 

	from common import mail
