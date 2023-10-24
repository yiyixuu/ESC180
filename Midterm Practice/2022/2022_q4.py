def matrix_sum(A, B):
    if not len(A) == len(B) or not len(A[0]) == len(B[0]): return "ERROR"

    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    
    return A