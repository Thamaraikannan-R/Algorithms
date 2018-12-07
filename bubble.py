arr=[9,6,8,4,7]
print("before bubble sort:",arr)
l=len(arr)
print(l)
for i in range(l):
    for j in range(0,l-i-1):
        if (arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("output",arr)