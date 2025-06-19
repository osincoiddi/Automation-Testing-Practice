
import random
import string
from random import choice
from string import ascii_lowercase

def random_string(length=10, chars=ascii_lowercase+string.digits):
    return ''.join(choice(chars) for x in range(length))
