__author__ = 'G'

import re

def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    text = str(text)

    return [atoi(c) for c in re.split('(\d+)', text)]
