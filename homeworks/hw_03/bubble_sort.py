def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True

        if swapped == False:
            break

arr = [1,4,30,90,45,3,56]
bubbleSort(arr)

print("Sorted array :")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")