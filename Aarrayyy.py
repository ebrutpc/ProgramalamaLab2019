array=[5,7,9,6,-3]

def toplambul(liste):
    enbuyuk=0
    sayi=0
    for i in range(0,len(liste)):
        for j in range(0,len(liste)):
            sayi+=liste[i]
            if(sayi>enbuyuk):
                enbuyuk==sayi
        sayi=0
    print(enbuyuk)

toplambul(array)

def asalmi(num):
    dizi=[]
    for i in range(2,num):
        if(num%i==0):
            dizi.append(i)
    if(len(dizi)==0):
        print("Asal degildir",num)
    return dizi

print(asalmi(13))