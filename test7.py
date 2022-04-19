def smallest(A):
    AA=set(A)
    AAA=sorted(AA)
    small=len(A)
    list1=[]
    for each in range(1,small+2):
        if each not in AAA:
            list1.append(each)
    return list1[0]
A=[1, 3, 6, 4, 1, 2]
print(smallest(A))
