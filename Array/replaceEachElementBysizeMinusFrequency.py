#
# Replace each element by the difference of the total size of the array and frequency of that element
#
# Create a map and store the occurance of all element and subtract from the size of arr and place in array.



def main(arr):
    size= len(arr)
    mp=dict()
    for i in range(size):

        mp[arr[i]] = mp.get(arr[i], 0) + 1
    print(mp)

    for i in range(size):
        arr[i]= size - mp.get(arr[i])
    print(arr)

main(arr=[1, 2, 5, 2, 2, 5, 4])