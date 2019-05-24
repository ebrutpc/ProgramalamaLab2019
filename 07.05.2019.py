import  random

def get_n_random_integer(n):
    random.seed(100)
    numbers=[]
    for i in range(n):
        s=random.randint(-100,100)
        numbers.append(s)
    return numbers

def shellsort(arr):

    comparison=0
    n=len(arr)
    gap=int(n/2)
    comparison+=1
    swap=0

    while (gap>0):
        for i in range(gap,n):
            comparison+=1
            temp=arr[i]
            j=i
            while(j>=gap and arr[j-gap]>temp):
                swap+=1
                comparison+=1
                arr[i]=arr[j-gap]
                j-=gap
            arr[j]=temp
        gap=gap//2
    return arr,comparison,swap


a=get_n_random_integer(10)
m=shellsort(a)

print(m)