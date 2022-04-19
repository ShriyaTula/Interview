list_e = [[90, 4, 12, 2], [], [34, 45, 2], [9,4], "char", [7, 3, 19]]
def COUNTY(list):
    count=0
    for each in list:
        count=len(each)+count
    return count
print(COUNTY(list_e))