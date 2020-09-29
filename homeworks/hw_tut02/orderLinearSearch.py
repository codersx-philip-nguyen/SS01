def orderLinearSearch(arr ,key):
    for i in range(len(arr)):
        if(key == arr[i]):
            print(i)
orderLinearSearch([1,2,3,4,5,6],6)