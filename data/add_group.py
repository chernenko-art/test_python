# -*- coding: utf-8 -*-
from model.group import Group
import random
import string


def random_string(prefix, maxlen):
    # generate string on letters, numbers symbols and spaces
    symbol = string.ascii_letters + string.digits + string.punctuation + " "*10
    # generate string on random symbols and length
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


testdata = [
        Group(name=name, header=header, footer=footer)
        for name in ["", random_string("name", 10)]
        for header in ["", random_string("header", 20)]
        for footer in ["", random_string("footer", 20)]
    ]

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]