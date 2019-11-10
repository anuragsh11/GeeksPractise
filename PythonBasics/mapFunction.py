# map() function
# It also takes the iterable object as input and pass to a function
# just like the filter() function but filter return only the True value as it makes comparision always
#cwhere the map return the function result
#

def checkEvenOdd(numList):
    if numList % 2 != 0:
        return  numList



numList=[1,2,3,4,5,6,7,8,9]
oddList=set(map(checkEvenOdd,numList))
print(oddList)