#!python3
#TODO: could potentially make this OS generic by adding code to detect OS type
#then have it use the compatible folder syntax type for that OS. - ie, \ for Win
# or / for Unix.

import os
import shutil

#These dirs are specified relative to where the script is run from.
#In this case, the script was run on Win10 thus the \ in the path.
#Alternatively, (and preferably) you'd specify the full path of each dir.

fromdir = "testdir1"
todir = "testdir2\\"

files = os.listdir(fromdir)

for i in files:
	shutil.move(fromdir + "\\" + i, todir) #Adjust the \ or / based on OS type.
	print("Moved %s" % i)
