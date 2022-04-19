# Online Python - IDE, Editor, Compiler, Interpreter

s = 'apple'
print(s[::-1])
print(s[:2])
print(s[3:][::-1])
print(s[3:])
print(s[:2:-1])
"""
If input is "Robert000Smith000123". The function should return the following using that input:
{ "first_name": "Robert", "last_name": "Smith", "id": "123" }
"""


def split_based(s):
    d = {}
    l = s.split('000')
    print(l)
    d['first_name'] = l[0]
    d['last_name'] = l[1]
    d['id'] = l[2]
    return d


print(split_based('Robert000Smith000123'))

