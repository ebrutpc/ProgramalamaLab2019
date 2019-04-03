#Frekans tablosunu bulup tekrar edenleri yazan bi fonk

#Dictionary
def my_frequency_dict(list):
    frequency_dict={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict

#List

def my_frequency_list(list):
    frequency_list=[]
    for i in range(len(list)):
        s=False
        for j in range(len(frequency_list)):
            if(list[i]==frequency_list[j][0]):
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list[i],1])
    return frequency_list




my_list_1=[5,4,7,9,62,85,75,14,5,7,4,62,58]
print(my_list_1)
print(my_frequency_dict(my_list_1))
print(my_frequency_list(my_list_1))

