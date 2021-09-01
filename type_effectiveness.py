#!/usr/bin/env python

import urllib.request, json 
import random
import pandas as pd

url = "https://pogoapi.net/api/v1/type_effectiveness.json"
data = {}
ptypes = []
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

table = []

for key in data.keys():
    ptypes.append(key)
    data_tuple = tuple(data[key].values())
    table.append(data_tuple)

df = pd.DataFrame(table, columns = ptypes, index = ptypes)

def get_types():
    return ptypes

class Attack:
    def __init__(self, ptype):
        if ptype not in ptypes:
            raise ValueError

        self.ptype = ptype
        self.dy = df.transpose()
        self.eff = self.dy[self.ptype]

    def __eq__(self, other):
        if (isinstance(other, Attack)):
            return self.ptype == other.ptype
        return false

    def strong_against(self):
        dy=df.transpose()
        return list(self.dy[self.eff == 1.6].index)

    def weak_against(self):
        dy=df.transpose()
        return list(self.dy[self.eff == 0.625].index)

    def normal_against(self):
        dy=df.transpose()
        return list(self.dy[self.eff == 1].index)

    def ineffective_against(self):
        dy=df.transpose()
        return list(self.dy[self.eff == 0.390625].index)


class Defender:
    def __init__(self, ptype):
        self.ptype = 0
        self.eff = 0

        if isinstance(ptype, list):
            if len(ptype) != 2:
                raise ValueError
            if ptype[0] == ptype[1]:
                raise ValueError
            for x in ptype:
                if x not in ptypes:
                    raise ValueError
            self.ptype = ptype
            self.ptype.sort()
            self.eff = df[self.ptype].prod(1)
        else:
            if ptype not in ptypes:
                raise ValueError
            self.ptype = ptype
            self.eff = df[self.ptype]

    def __eq__(self, other):
        if (isinstance(other, Defender)):
            return self.ptype == other.ptype
        return false

    def very_immune_to(self):
        return list(df[self.eff == 0.244140625].index)

    def immune_to(self):
        return list(df[self.eff == 0.390625].index)

    def resistant_to(self):
        return list(df[self.eff == 0.625].index)

    def vulnerable_to(self):
        return list(df[self.eff == 1.6].index)

    def neutral_to(self):
        return list(df[self.eff == 1].index)

    def doubly_vulnerable_to(self):
        return list(df[self.eff == (1.6*1.6)].index)
