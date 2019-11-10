# differnce method of Set gives the differnce values from two sets


valid = set(['Green','Blue','Red','Orange','Yellow'])

my_set=set(['Blue','Green','Black'])

print(my_set.difference(valid))  # it gives which is not in valid O/P Black
print(valid.difference(my_set)) # it give which is not in my_set O/p {'RedOrange', 'Yellow'}
print(valid.union(my_set))