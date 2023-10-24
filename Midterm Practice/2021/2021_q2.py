def add_sparse_matrices(A, B, dim):
    result = [[0 for _ in range(dim[1])] for _ in range(dim[0])]
    for i in range(dim[0]):
        for j in range(dim[1]):
            if((i,j)) in A and B:
                result[i][j] += A[(i,j)]
                result[i][j] += B[(i,j)]

    return result