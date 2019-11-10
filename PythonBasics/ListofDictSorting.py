# How to sort a list of dictionary or tupple
# 1: by lambda
# 2: by itemGetter


my_list=[{"Name": "Anurag","Age":32},{"Name": "Varsha","Age":27},{"Name": "Anvay","Age":2}]

print(my_list)

# sort above list by lambda

print(sorted(my_list,key= lambda i: i["Age"]))

# sort by Item Getter

from operator import itemgetter

print(sorted(my_list,key=itemgetter("Age")))