from Golomb import golomb_coding, golomb_decoding, best_golomb_coding

# print(golomb_coding(0, 3))
# print(golomb_coding(1, 3))# 110
# print(golomb_coding(2, 3)) # 111
#print(golomb_coding(5, 2))
matrix = [0, 0, 0, 0, 0]
matrix2 = [1, 1, 1, 1, 1]
matrix3 = [115, 115, 115, 115, 115]
matrix_len = 0

print("Code : " + str(best_golomb_coding(matrix)))
print("Code : " + str(best_golomb_coding(matrix2)))
print("Code : " + str(best_golomb_coding(matrix3)))

for i in range(len(matrix)):
    matrix_len +=len(best_golomb_coding(matrix)[i])

print("Total code length : " + str(matrix_len))
print("Average code length : " +str(matrix_len / len(matrix3)))
