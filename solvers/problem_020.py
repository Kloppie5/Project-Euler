import os
import sys

sys.path.insert(1, os.path.dirname(os.path.abspath(__file__))+'/../')

from library import factorial

print(sum([int(c) for c in f"{factorial.factorial(100)}"]))