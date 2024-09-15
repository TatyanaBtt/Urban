def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
rezalt1 = get_matrix(2,2,10)
rezalt2 = get_matrix(3,5,42)
rezalt3 = get_matrix(4,2,13)
print(rezalt1)
print(rezalt2)
print(rezalt3)