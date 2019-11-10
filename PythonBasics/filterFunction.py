# Demo of filter function in Python
#
# the filter() function
# Remmber when an iterable object is passed in filter() function then one element is passed one by one
# not the complete List is passed.
#
def find_odd(numberList):

    if numberList % 2 == 0:
        return True
    else:
        return False

numb=[1,2,3,4,5,6,7,8,9]
print(numb)
oddList=list(filter(find_odd,numb))
print(oddList)

