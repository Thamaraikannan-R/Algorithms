ary=[20,40,10,4,2,29,48,24,54,65,76,89,80,78,67,9,7,97,678,97,68,6676,86878,67668,69,788,9,768]
ary.sort()
low=0
key=2
high=int(len(ary)-1)
while(low<=high):
    mid=int((low+high)/2)
    if ary[mid]==key:
        print("key found...")
        break
    elif ary[mid]>key:
        high = mid - 1
    else:
        low = mid + 1

