def merge(nums_1, nums_2):
    """
    Merges the numbers in the two lists in-place
    pass nums_1 = [1,3,6,8,9,0,0,0,0] nums_2 = [2,4,5,7]
    merge(nums_1, nums_2) print(nums_1) > [1,2,3,4,5,6,7,8,9]
    """
    new_l = []
    for i in nums_1:
        if i!=0:
            new_l.append(i)
    new_l.extend(nums_2)
    l=len(new_l)
    for j in range(l):
        for m in range(l-1):
            if new_l[m]>new_l[m+1]:
                new_l[m],new_l[m+1]=new_l[m+1],new_l[m]
    return new_l


    #return sorted(new_l)
nums_1 = [1,3,6,8,9,0,0,0,0]
nums_2 = [2,4,5,7]
print(merge(nums_1, nums_2))
