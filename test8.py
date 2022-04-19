li=[2,3,4,4,1,2,3,5,6,7]
d={}
d1={}
for i in li:
    if(d.get(i,None)==None):
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
for i in li:
    if(d1.get(i,None)==None):
        d1[i]=li.count(i)
print(d1)
