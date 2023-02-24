def getdistinctelements(arr):
    list =[]
    for num in arr:
        if arr.count(num) == 1:
            list.append(num)
            return list
        print(getdistinctelements([1,2,3,4]))
