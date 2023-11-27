import numpy as np


# Printing matrices using NumPy:

# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
# print(M)

def print_matrix(M_lol):
    M = np.array(M_lol)
    print(M)

# print_matrix([[1,-2,3],[3,10,1],[1,5,3]])


def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0: 
            return i
        
    return len(row)

def get_row_to_swap(M, start_i):
    swap_row = start_i
    smallest_lead_ind = get_lead_ind(M[start_i])
    for i in range(start_i, len(M)):
        if get_lead_ind(M[i]) < smallest_lead_ind:
            smallest_lead_ind = get_lead_ind(M[i])
            swap_row = i
    return swap_row


def add_rows_coefs(r1, c1, r2, c2):
    l = [0 for i in range(len(r1))]
    for i in range(len(r1)):
        l[i] = c1*r1[i] + c2*r2[i]
    return l

def eliminate(M, row_to_sub, best_lead_int):
    for i in range(row_to_sub+1, len(M)):
        if M[row_to_sub][best_lead_int] != 0:
            coef = -M[i][best_lead_int]/M[row_to_sub][best_lead_int]
            # print(f'Adding {coef} times row {row_to_sub} to row {i}')
            M[i] = add_rows_coefs(M[row_to_sub], coef, M[i], 1)
    return M

def back_eliminate(M, row_to_sub, best_lead_int):
    for i in range(row_to_sub-1, -1, -1):
        if M[row_to_sub][best_lead_int] != 0:
            coef = -M[i][best_lead_int]/M[row_to_sub][best_lead_int]
            # print(f'Adding {coef} times row {row_to_sub} to row {i}')
            M[i] = add_rows_coefs(M[row_to_sub], coef, M[i], 1)
    return M

# print(eliminate([[5, 6, 7, 8], [0,0, 1, 1], [0, 0, 5, 2], [0, 0, 7, 0]], 1, 2))

def forward_step(M):
    print('The matrix is currently:')
    print_matrix(M)
    for i in range(len(M)):
        print(f'Now looking at row {i}')
        row_to_swap = get_row_to_swap(M, i)
        lead_ind = get_lead_ind(M[row_to_swap])
        print(f'Swapping rows {i} and {row_to_swap} so that entry {lead_ind} in the current row is non-zero')
        M[i], M[row_to_swap] = M[row_to_swap], M[i]
        print('The matrix is currently:')
        print_matrix(M)
        print(f'Adding row {i} to rows below it to eliminate coefficients in column {lead_ind}')
        M = eliminate(M, i, lead_ind)
        print('The matrix is currently:')
        print_matrix(M)
    print('Done with the forward step')
    print('The matrix is currently:')
    print_matrix(M)
    return M




def backward_step(M):
    for i in range(len(M)-1, -1, -1):
        print(f'Now looking at row {i}')
        lead_ind = get_lead_ind(M[i])
        print(f'Adding row {i} to rows above it to eliminate coefficients in column {lead_ind}')
        M = back_eliminate(M, i, lead_ind)
        print('The matrix is currently:')
        print_matrix(M)
    print('Now dividing each row by the leading coefficient')
    for i in range(len(M)):
        lead_ind = get_lead_ind(M[i])
        M[i] = [M[i][j]/M[i][lead_ind] for j in range(len(M[i]))]
    print('The matrix is currently:')
    print_matrix(M)
    return M

# backward_step(forward_step([[1, -2, 3, 22], [3, 10, 1, 314], [1, 5, 3, 92]]))
#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
# M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
# x = np.array([75,10,-11])
# b = np.matmul(M,x)        

# print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

# To obtain a list of lists from the array M, we use .tolist()
# M_listoflists = M.tolist() 

# # print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

def construct_M_b(M, b):
    M_listoflists = M.tolist()
    for i in range(len(M_listoflists)):
        M_listoflists[i].append(b[i])
    return M_listoflists

def solve(M, b):
    M_listoflists = construct_M_b(M, b)
    M_listoflists = backward_step(forward_step(M_listoflists))
    return [row[-1] for row in M_listoflists]