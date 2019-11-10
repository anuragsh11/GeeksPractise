def right_highest(arr):

    size=len(arr)
    max_element=arr[size-1]
    arr[size-1] = -1
    for i in range(size-2,-1,-1):
        temp = arr[i]
        arr[i] = max_element
        if max_element < temp:
            max_element = temp
    return  arr

def left_highest(arr):
    size=len(arr)
    max_left= arr[0] #4
    arr[0] = -1  #[-1,]
    for i in range(1,size):
        temp=arr[i] #temp =5
        arr[i] =max_left #[-1,4,]
        if max_left < temp:
            max_left =temp
    return arr
arr = [16, 17, 4, 3, 5, 2]
arr1= [4, 5, 2, 1, 7, 6]
print(right_highest(arr))
print(left_highest(arr1))