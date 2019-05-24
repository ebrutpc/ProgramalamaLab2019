#noktaların merkeze olan uzaklıkarını bulan ve grafiklerini çizen program

import random

array_1=[5,7,1,9,2]

for i in range(len(array_1)):
    #min=i
    for j in range(i+1,len(array_1)):
        if array_1[i]<array_1[j]:
            pass
        else:
            temp=array_1[i]
            array_1[i]=array_1[j]
            array_1[j]=temp
print(array_1)

#en kücügü tespit edip yer değiştirme yaptık

point_1=[[2,5],[1232,2235],[123,253],[12,2325],[123,25],[22,5],[2,45],[72,5],[2,5]]

from matplotlib import pyplot as plt  #pythonda bilimsel hesaplamada önemli bi araçtır
                                       #Grafik cizimi icin kullanilir

for i in range (len(point_1)):
    plt.plot(point_1[i][0],point_1[i][0],'*')
plt.show()

point_1 = [[2,5],[12,25],[12,25],[12,25],[12,25],[2,5],[2,5],[2,5],[2,5]]
print(len(point_1))
point_1=[2,5]
point_2=[12,25]
center[(2+12)/2,(25+5)/2]
from matplot import pyplot as plt

plt.plot(point_1[0],point_1[1],'*')
plt.plot(point_2[0],point_2[1],'♥')
plt.plot(center[0],center[1],'♥')


plt.show()

import random



def get_center(points): #points icindeki noktalrın (xcenter,ycenter) merkez noktası bulunur
    x_s=[i for i,j in points]
    y_s=[j for i,j in points]

    center_x=sum(x_s)/len(x_s)
    center_y=sum(y_s)/len(y_s)

    return center_x,center_y


from matplotlib import pyplot as plt


def get_points(n):# n tane nokta belirlendi (-10,10) araliğinda
    point_1=[]
    for i in range(n):
        x=random.randint(-10,10)
        y=random.randint(-10,10)
        point_1.append([x,y])

    return point_1

def plot_points(points):
    for i in range(len(points)):
        plt.plot(points[i],[0],points[i][1])
    center=get_center(points)
    plt.plot(center[0],center[i],'or')
    #plt.plot(center[0],center[1],'r')
    plt.show()


def get_distance_for_n_point(points):
# points listesi içindeki noktaların merkez noktasına olan uzaklığı  ve aradaki uzunluk bulundu
    center=get_center(points)
    distance=[]
    for p in points:
        a=(p[0]-center[0])
        b=(p[1]-center[1])
        distance.append((a**2+b**2)**0.5)
    return  distance

p1=get_center(10)
plot_points(p1)

p_1=get_center(10000)
plot_points(p_1)



def get_center(points):
    x_s=[i for i,j in points]
    print(x_s)
    y_s=[j for i,j in points]

    center_x = sum(x_s) / len(x_s)
    center_y = sum(y_s) / len(y_s)

    return center_x , center_y

def get_distance_for_n_point(points):
    center=get_center()
    distance=[]
    for p in points:
        a=(p[0]-center[0])
        b=(p[1]-center[1])
        distance.append((a**2+b**2)**0.5)
    return distance


p_2=get_points(10)
get_distance_for_n_point(p_2)


def get_n_points(n):
    points=[]
    for i in range(n):
        x=random.randint(-10,10)
        y=random.randint(-10,10)
        points.append([x,y])
    return  points

def get_distance(p_1,p_2):
    a=p_2[0]-p_1[0]
    b=p_2[1]-p_2[1]
    return ((a**2+b**2)**0.5)

points_1=get_points(10)

get_center(points_1)
#
def mySelectionSort(points):
    n=len(points)
    center=get_center(points)
    comprasion=0
    swap=0
    for i in range(n):
        for j in range(i+1,n):
            a=get_distance(points[i],center)
            b=get_distance(points[j],center)
            comprasion+=1 #karşılaştırma kaç ke yapılmıştır
            if(a>b):
                swap+=1
                temp=points[i]
                points[i]=points[j]
                points[j]=temp
        return points,comprasion,swap


points_1=get_n_points(5)

point_2=mySelectionSort(points_1)
