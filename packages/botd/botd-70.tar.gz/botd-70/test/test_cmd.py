# This file is placed in the Public Domain.

import unittest

from bot.bus import Bus
from bot.run import getmain
from bot.tbl import Table
from bot.obj import Object

events = []

param = Object()
param.add = ["test@shell", "bart", ""]
param.cfg = ["cfg server=localhost", "cfg", ""]
param.dne = ["test4", ""]
param.rm = ["reddit", ""]
param.dpl = ["reddit title,summary,link", ""]
param.log = ["test1", ""]
param.flt = ["0", ""]
param.fnd = ["cfg", "log", "rss", "cfg server==localhost", "rss rss==reddit"]
param.rss = [
    "https://www.reddit.com/r/python/.rss",
]


class Test_Commands(unittest.TestCase):
    def test_commands(self):
        k = getmain("k")
        c = Bus.first()
        l = list(Table.modnames)
        for cmd in l:
            for ex in getattr(param, cmd, [""]):
                e = c.event(cmd + " " + ex)
                k.dispatch(e)
                events.append(e)
