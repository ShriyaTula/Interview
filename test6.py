def reverse(s):
    st=s[::-1]
    return st

s = 'Hello World'
print(reverse(s))
def reverse1(strings):
    new_s = ''
    for i in strings:
        new_s = i+new_s
    return new_s
s = 'Hello World'
print(reverse1(s))