#Calling other functions from another file

import sys

from say import hello
from say import goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])
    