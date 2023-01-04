from Golomb import golomb_coding, golomb_decoding, best_golomb_coding, best_golomb_m
from math import ceil, log2
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

#matrix = [0, 0, 0, 0, 1, 1, 1, 1]
#matrix = [0, 0, 0, 0, 1, 1, 1, 1]
matrix = np.random.randint(0,100,10)

diff_m = []
diff_k = []
diff_m_matrix_len = []
print(matrix)
print("Best (k,m) : " + str(best_golomb_m(matrix)))
k = ((best_golomb_m(matrix))[0])
for i in range(-10, 10, 1):
    matrix_len = 0
    if k + i > 0:
        for j in range(len(matrix)):
            matrix_len += len((golomb_coding(matrix[j], k+ i)))
        diff_k.append(round(k + i, 2))
        diff_m.append(int(2**(k+i)))
        diff_m_matrix_len.append(matrix_len)

print(golomb_decoding("100",3))
print("Different k : " + str(diff_k))
print("Different m : " + str(diff_m))
print("Different matrix length : " + str(diff_m_matrix_len))
print("Best golomb coding : " + str(best_golomb_coding(matrix)))
fig = plt.figure()
plt.title("Best golom coding parameter m")
plt.xlabel("m")
plt.ylabel("codeword length")

for i in range(len(diff_m)):
    plt.text(diff_m[i] + 0.25, diff_m_matrix_len[i] - 0.5, (round(diff_m[i], 2), diff_m_matrix_len[i]))
plt.plot(diff_m, diff_m_matrix_len, marker='o', mec='r', mfc='w')
plt.show()
