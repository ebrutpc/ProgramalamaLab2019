def my_searchselection(my_array):
    swap_sayisi=0
    for i in range(len(my_array)-1,0,-1):
        positionOfMax=0
        for location in range(1,i+1):#0. indisi atadığımız için 1den başlattık,indisleri tutarak sıralama yapar
            if(my_array[location]>my_array[positionOfMax]):
                positionOfMax=location
        temp=my_array[location]
        my_array[location]=my_array[positionOfMax]
        my_array[positionOfMax]=temp
        swap_sayisi+=1
    print("swap sayisi",swap_sayisi)
my_arr=[92,56,100,5]
my_searchselection(my_arr)

print(my_arr)

def my_binary_Search(my_sorted_array,item):
    first=0
    last=len(my_sorted_array)-1
    found=False
    s=0
    while(first<=last and not found):
        midpoints=(first+last)//2
        print("first-last",first,last)
        s+=1
        if(my_sorted_array[midpoints]==item):
            found=True
        else:
            if(item<my_sorted_array[midpoints]):
                last=midpoints-1
            else:
                first=midpoints+1
                #s+1 diziyi kaç defa ssağ tarafa böler
    return (found,midpoints)
print(my_binary_Search(my_arr,92))

#orta eleman=midponts
#s:kaçıncı adımda olduğunu yazar
#first=0
#last=n-1
