def bubbleSort(arr):
    n=len(arr)
    for  i in range(n-1):
        swapped=False
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if(swapped==False):
            break
    return arr  


arr=[1,4,67,89,7666,66]
answer=bubbleSort(arr)
print(answer)