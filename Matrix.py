matrix_1 = [[4 , 6] , [8 , 5]]
matrix_2 = [[2 , 3 ] , [ 2 , 9]]
alpha = 10


def my_matrix_addition(m_1 , m_2) :
    result = []
    for row in range(len(m_1)) :
        result.append([])  # liste ekle
        for column in range(len(m_1[0])) :
            # print(m_1[row][column],end= )
            result[row].append(m_1[row][column] + m_2[row][column])
    return result


print(my_matrix_addition(matrix_1 , matrix_2))
print("matrix_1 in satır sayısı" , len(matrix_1))
print("matrix_!  in sutün sayısı" , len(matrix_1[0]))
print("matrix_2 in satır sayısı" , len(matrix_2))
print("matrix_2 in satır sayısı" , len(matrix_2[0]))

print("----------------------")


def my_matrix_subs(m_1 , m_2):
    result = []
    for row in range(len(m_1)):
        result.append([])
        for column in range(len(m_1[0])):
            result[row][column].append(m_1[row][column] - m_2[row][column])
    return result
# unindent does not match any outer indentation level

def my_matrix_scalar_product(alpha,m_1):
 result=[]
 for row in range(len(m_1)):
     result.append([])

     for column in range(len(m_1[0])):
         result[row][column].append(m_1[row][column]*alpha)
 return  result

print(my_matrix_scalar_product(2,matrix_1))

def f_1(matrix1,i):
    return matrix1[i]
#return matrix1[i][:]
t=f_1(matrix_1,1)
print("f1",t)

def f_2(matrix1,j):
    my_j_th_col=[]
    for row in matrix1:
        for indis in range(len(row)):
            if(indis==j):
                my_j_th_col.append(row[indis])
    return my_j_th_col


def my_vector_inner_pro(v,w):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]*w[i]
    t=0
    for i in range(size):
        t=t+my_result[i]
    return t



def my_matrix_multiply(m_1,m_2):
    result=[]
    for row in range(len(m_1)):
        result.append()
        for column in range(len(m_2[0])):
            a=f_1(m_1,row)
            b=f_2(m_2,column)
            c=my_vector_inner_pro(a,b)
            result[row].append(c)
    return  result

