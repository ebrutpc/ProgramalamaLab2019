import random

def get_n_random_integer(n):#n elemanlı random integer olustur
    random.seed(100)
    numbers=[]
    for i in range(n):
        s=random.randint(-100,100)
        numbers.append(s)
    return  numbers


def get_mean_for_n_integer(numbers): #ortalamayı bulan fonksiyon
    toplam=0
    kactane=0
    for sayi in numbers:
        toplam+=sayi
        kactane+=1

    return toplam/kactane

def get_std_for_n_integer(numbers):#standart sapma bulan fonksiyon
    toplam=0
    kactane=0
    ortalama=get_mean_for_n_integer(numbers)
    for sayi in numbers:
        toplam=toplam+(sayi-ortalama)**2
        kactane+=1

    var_1=toplam/(kactane-1)
    std_1=var_1**.5
    return std_1

def normalization(numbers):#
    new_number=[]
    ortalama=get_mean_for_n_integer(numbers)
    standart_sapma=get_std_for_n_integer(numbers)

    for x in numbers:
        new_x=(x-ortalama)/standart_sapma
        new_number.append(new_x)

    return new_number

def get_mean_one_std_neighbor_ration(numbers):
    kactane=0
    toplamKacsayi=0
    ortalama=get_mean_for_n_integer(numbers)
    standart_sapma=get_std_for_n_integer(numbers)


    low=ortalama-standart_sapma
    high=ortalama+standart_sapma

    for  x in numbers:
        toplamKacsayi=toplamKacsayi+1
        if(x>low and x<high):
            kactane+=1
        return kactane/toplamKacsayi




def insertion(numbers):#sıralama fonksiyonu
    sayilar2=numbers
    lenght_1=len(sayilar2)
    for i in range(1,lenght_1):
        for j in range(i,0,-1):
            if(sayilar2[j]<sayilar2[j-1]):
                temp=sayilar2[j-1]
                sayilar2[j-1]=sayilar2[j]
                sayilar2[j]=temp

    return sayilar2


sayilar=get_n_random_integer(5)
ortalama=get_mean_for_n_integer(sayilar)
standart_sapma=get_std_for_n_integer(sayilar)
yeni_sayilar=normalization(sayilar)



print("sayilar = ",sayilar)
print("ortalama = ",ortalama)
print("standart sapma = ",standart_sapma)
print("yeni normalize edilmiş liste = ",yeni_sayilar)

sayilar_1 = get_n_random_integer(100)
print("************",get_mean_one_std_neighbor_ration(sayilar_1))
print(yeni_sayilar)