import re

def kebabize(string):
    splitted = re.findall('[A-Z][^A-Z]*', string)
    return '-'.join(splitted).lower()