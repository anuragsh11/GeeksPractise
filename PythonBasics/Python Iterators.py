# Iterators are objects that can be iterated upon.
# In this tutorial, you will learn how iterator works
# and how you can build your own iterator using __iter__ and __next__ methods.
#

my_list=[1,2,3,4,5,6,]

# make an iterable object

my_iter=iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(next(my_iter))
print(next(my_iter)) # this will raise an Exception StopIteration as there is no new element

# How for loop works
# the above code can be achiver by
# for x in my_list:
#   print(x)

while True:
    try:
        element=next(my_iter)
    except StopIteration:
        break