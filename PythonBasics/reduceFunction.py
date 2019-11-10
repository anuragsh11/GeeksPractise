# Reduce() is a function which takes an iterable and returns
# it furst operate on first 2 elements of an iterable and then take result with the 3rd one and so on.
#
#
# A function to calculate some of array elements

from functools import reduce
from itertools import accumulate


numList=[1,2,3,4]
def sumList(numb1,numb2):
    return numb1 + numb2

# To Find highest among the array

def high(numb1,numb2):
    if numb1 > numb2:
        return numb1
    else:
        return numb2

sum=reduce(sumList,numList)

max=reduce(high,numList)
print(sum, "max is ",max)


# by using lambda Function

my_list=[40,4,5,2]

division= reduce(lambda a,b : a/b,my_list)
divByaccumulate= list(accumulate(my_list,lambda a,b : a/b))
print(division)
print(divByaccumulate)