# .jpg .png .gif resmin sıkısma algortimasını veren uzantı
#.bmp --> hicbir sıkıstırma yapmadan tek renk  erisim
#var olan her renk icin :
#rgb->0-255  #gray->0-255  #bw->01

#pic element -> pixel m,n matrisli pixeller boyutu
#her bir pixelde tek değer yani renk vardır

import matplotlib.pyplot as plt
#import matplotlib. as mpimg
import numpy as np

def my_rot(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    my_new_image=np.zeros((n,m,3),dtype=int)
    for row in range(m):
        for column in range(n):
            me_new_image[column,row,:]=im_1[row,column,:]
    return my_new_image

def my_convert_rgb_to_gray(im_1):
   m=im_1.shape[0]
    n = im_1.shape[1]
    my_new_image = np.zeros((n,m ),dtype=int)
    for row in range(m):
        for column in range(n):
            my_new_image[row,column]=my_norm(im_1[row,column,:])


    return my_new_image

def my_norm(my_v):
    return  int(((m_v[0]**2)+(my_v[1]**2)+(my_v[2]**2))**0.5)

def my_norm1(my_v):
    s=int(((m_v[0]**2)+(my_v[1]**2)+(my_v[2]**2))**0.5)
    if (s>280):
        return 1
    else:
        return 0


def my_convert_gray_to_bw(im_1):
    m = im_1.shape[0]
    n = im_1.shape[1]
    my_new_image = np.zeros((n , m) , dtype=int)

    for row in range(m):
        for column in range(n):
            my_new_image[row,column]=my_norm1(im_1[row,column,:])
    return  my_new_image



file_name="resim.jpg"
im_1=plt.imread(file_name)
im_2=my_rot(im_1)
im_3=my_convert_rgb_to_gray(im_2)
im_4=my_convert_gray_to_bw(im_2)


plt.subplot(1,4,1)
plt.imshow(im_1)
plt.subplot(1,4,2)
plt.imshow(im_2)
plt.subplot(1,4,3)
plt.imshow(im_3,cmap='gray')
plt.subplot(1,4,4)
plt.imshow(im_4,cmap='gray')