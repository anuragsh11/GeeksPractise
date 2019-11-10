# Find the longest string that can be made up of other strings from the array
# Given an array of strings arr[], the task is to find the largest string in the
# array which is made up of the other strings from the array after concatenating
# one after another. If no such string exists then print -1

def buildword(s,isOrginalWord,mp):
    #print(s,isOrginalWord,mp)
    if s in mp and mp[s] == 0:
        return False

    if s in mp and mp[s] == 1 and isOrginalWord == 0:
        return True

    for i in range(1,len(s)):
        left=s[:i]
        right=s[i:]

        if left in mp and mp[left] == 1 and buildword(right,0,mp):
            return True

def longestString(arr,n):
    print(arr)
    mp=dict()
    for i in arr:
        mp[i] =1

    for i in arr:
        if buildword(i,1,mp):
            return i
        else:
            print('False')

arr=["geeksfor","geeks", "for", "geeksforgeeks","for"]
arr=sorted(arr,reverse=True)
size=len(arr)
print(longestString(arr,size))
