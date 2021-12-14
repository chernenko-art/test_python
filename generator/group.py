# -*- coding: utf-8 -*-
from model.group import Group
import random
import string
import jsonpickle
import os.path
import getopt
import sys


# default params
n = 5  # quantity iterations
f = "data/groups.json"

# get option from cmd
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# parsing opts value
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# path to file
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


# generate random string
def random_string(prefix, maxlen):
    # generate string on letters, numbers symbols and spaces
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    # generate string on random symbols and length
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


# generate Group from random data
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for name in range(n)
]


# write generate data (User object) to json file
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)  # format params
    out.write(jsonpickle.encode(testdata))
