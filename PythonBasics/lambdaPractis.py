# Demo of filter function in Python
#
# the filter() function with Lambda function
# Remember when an iterable object is passed in filter() function then one element is passed one by one
# not the complete List is passed.
#

numberList=[1,2,3,4,5,6,7,8,9,10,11]

oddList= list(filter(lambda x: (x%2),numberList))
# It return odd number as 1 %2 is 1 which is True and 2 %2 is 0 which is False

evenList= list(filter(lambda x: (x%2 == 0),numberList))
# It return Even number as 1 %2 is 1 which is not equal to 0
oddList_2= list(filter(lambda x: (x%2 !=0),numberList))

print(oddList)
print(evenList)
print(oddList_2)