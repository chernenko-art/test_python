import random
import string
from model.user import User
import jsonpickle
import os.path
import getopt
import sys


# default params
n = 5  # quantity iterations
f = "data/users.json"

# path to file
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


# get option from cmd
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of user", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# parsing opts value
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# generate random string
def random_string(prefix, maxlen):
    # generate string on letters, numbers symbols and spaces
    symbol = string.ascii_letters + string.digits + " "*10
    # generate string on random symbols and length
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


# generate User from random data
test_data = [
                User(firstname="", middlename="", lastname="", address="", home="", mobile="", work="", email="",
                  email2="", email3="", phone2="")
            ] + [
    User(firstname=random_string("firstname", 10), middlename=random_string("lastname", 10),
         lastname=random_string("lastname", 10), address=random_string("address", 10), home=random_string("home", 10),
         mobile=random_string("mobile", 10), work=random_string("work", 10), email=random_string("email", 10),
         email2=random_string("email2", 10), email3=random_string("email3", 10), phone2=random_string("phone2", 10))
    for name in range(n)
]


# write generate data (User object) to json file
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)  # format params
    out.write(jsonpickle.encode(test_data))
