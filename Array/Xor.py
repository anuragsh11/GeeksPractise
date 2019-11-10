# Replace every array element by
# Bitwise Xor of previous and next element
#
#

def main(arr,n):
    previous = arr[0]
    arr[0] = arr[0] ^ arr[1]

    for i in range(1,n-1):
        curr = arr[i]
        arr[i] = previous ^ arr[i+1]
        previous= curr
    arr[n-1] = arr[n-1] ^ previous

    print(arr)


arr=[2, 3, 4, 5, 6]
size=len(arr)
main(arr,size)