my_matrix1=[[4,1],[2,5]]
my_matrix2=[[11,14,45,48],[10,12,21],[32,65,98]]
my_matrix3=[[0,15,74,78],[61,54,23,41],[71,52,62,32],[55,69,96,14]]

print(my_matrix1)
print(my_matrix2)
print(my_matrix3)

def my_matrix_det(m_1):
    s1=(m_1[0][0])*(m_1[1][1])
    s2=(m_1[0][1])*(m_1[1][0])
    s3=s1-s2
    return s3
print(my_matrix_det(my_matrix1))


def my_matrix_det2(m_1):
