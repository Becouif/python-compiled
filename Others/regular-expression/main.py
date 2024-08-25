# we can use regular expression to search
import re




string = 'search this inside of this text please!'

# a = re.search('this', string)
# print(a.group())

# another way to use it
pattern = re.compile('this')
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(d)

# useful website
# regex101.com

# very good for validation