from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]

sentence = 'Blah blah blah blah thinking about python'
print(Counter(sentence))
print('\n')


# defualtdict expect a callable and a dict
# callable can be functions, classes,methods e.t.c
dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})
# with defaultdict we assign a defualt value using lambda 

print(dictionary["c"])


# OrderedDict maintain order of insertion

d = {}
d['a'] = 1
d['b'] = 2


d2 = {}
d2['b'] = 2
d2['a'] = 1


print(d == d2)
# this gives false because order is not maintained

