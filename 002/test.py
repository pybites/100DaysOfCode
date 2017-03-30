import os
import sys

cwd = os.getcwd()
project_root = os.path.dirname(cwd)
sys.path.append(project_root)

from common import test
