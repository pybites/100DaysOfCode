#!python3

import os
import shutil

#These dirs are specified relative to where the script is run from.
#In this case, the script was run on Win10 thus the \ in the path.
#Alternatively, (and preferably) you'd specify the full path of each dir.

fromdir = "testdir1"
todir = "testdir2"

files = os.listdir(fromdir)

for i in files:
	shutil.move(os.path.join(fromdir, i), todir)
	print("Moved {} from {} to {}".format(i, fromdir, todir))
