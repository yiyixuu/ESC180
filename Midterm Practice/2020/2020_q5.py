def share_n1(M1, M2):
    matches = 0
    for i in range(len(M1)):
        col_M1 = [row[i] for row in M1]
        for j in range(len(M1[0])):
            col_M2 = [row[j] for row in M2]
            print(col_M1)
            print(col_M2)
            print("\n")
            if col_M1 == col_M2:
                matches += 1
    print(matches)
    return matches >= (len(M1)-1)


M1 = [[1, 2, 3],
      [1, 5, 1],
      [1, 2, 2]]

M2 = [[3, 1, 0],
      [1, 1, 2],
      [2, 1, 0]]

print(share_n1(M1, M2))