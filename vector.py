def creatmy_vector(n):
    return my_vector

v=[1,2,3]
w=[2,4,6]
a=[1,2,3,2,4,6]
b=[11,22,33,22,44,66]

def my_vector_Addition(v,w):
    size=len(v)
    my_ressult=[]
    for i in range(size):
        my_ressult.append(0)
    for i in range (size):
        my_ressult[i]=v[i]+w[i]
    return my_ressult

print("vector addition ",my_vector_Addition(v,w))

def my_vector_substraction(v,w):
    my_result=[0,0,0]
    for i in range(3):
        my_result[0]=v[0]-w[0]
        my_result[1]=v[1]-w[1]
        my_result[2]=v[2]-w[2]
    return my_result
print("vector substraction",my_vector_substraction(v,w))
def my_vector_scalar_product(alpha,v):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]*alpha
    return my_result
print("vector scalar product",my_vector_scalar_product(2,v))

c=my_vector_scalar_product(5,a)
d=my_vector_scalar_product(10,b)
e=my_vector_Addition(c,d)
f=my_vector_substraction(a,b)

print("scalar vector -> c",c)
print("vectors addition ->d",d)
print("vectors substraction ->e",e)

def my_vector_Inner_product(v,w):
     size=len(v)
     my_result=[]
     for i in range(size):
        my_result.append(0)
     for i in range(size):
        my_result[i]=v[i]*w[i]
     t=0
     for i in range(size):
        t=t+my_result[i]
     return  my_result


a=[1,2]
b=[3,5]
print(my_vector_Inner_product(a,b))