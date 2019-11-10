# lets practise some exception handling

my_list= [1,2,3,4]
"""
try:
    for i in range(len(my_list) +1 ):
        print(my_list[i])
except:
    print("error")
"""

try:
    raise NameError("Anurag")
except NameError:
    print("Exception")
    raise