def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


print(get_matrix(3, 6, 'Текст'))
a = [1, 2, 3]
