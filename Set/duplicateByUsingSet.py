my_list=[1,3,2,9.10,1,12,34,33,11,3,11]

duplicate=set([x for x in my_list if my_list.count(x) > 1])

print(duplicate)