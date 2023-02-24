# Sets - They are mutable and new elements can be added once sets are defined
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # duplicates will be removed

a = set('abracadabra')
print(a) # unique letters in a

a.add('z')
print(a)

