def find_max_min(arr):
    max = arr[0]
    min = arr[0]
    for i in arr[1:]:
        if type(i) == list:
            max, min = find_max_min(i)
            arr.extend([max, min])
        else:
            if i > max:
                max = i
            if i < min:
                min = i
    return max, min

if __name__ == '__main__':
    l = [12,32,34,1,[1,5,6,83],76]
    print(find_max_min(l))
