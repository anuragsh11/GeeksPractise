stir ="Geeks"
res=[]
for i in range(len(stir)):
    for j in range(i+1,len(stir)+1):
        res.append(stir[i:j])

print(res)

# by using list comprehession

res1=[ stir[i:j] for i in range(len(stir)) for j in range(i+1,len(stir)+1)]
print(str(res1))