from collections import Counter

c = Counter()
print(type(c)) # <class 'collections.Counter'>
print(c) # Counter()

cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c = Counter(cars)
print(c)
