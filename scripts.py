import random
from collections import OrderedDict


def shuffle_dict(d):
    keys = list(d.keys())
    random.shuffle(keys)
    return OrderedDict([(k, d[k]) for k in keys])
