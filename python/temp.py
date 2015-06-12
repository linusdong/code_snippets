text = 'blah blah glad glad'
dict = {key:text.count(key) for key in set(text.split())}
# print dict
key = max(dict, key=dict.get)
# print dict[key]

def allmax(iterable, key=lambda x:x):
    "Return a list of all items equal to the max of the iterable."
    maxi = max(iterable, key=key)
    return [element for element in iterable if key(element) == key(maxi)]

res = allmax(dict, key=dict.get)
print res
