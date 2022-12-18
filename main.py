from Golomb import golomb_coding, golomb_decoding, optimal_golomb_coding, bernoulli_golomb_coding

print(golomb_coding(0, 3))
print(golomb_coding(1, 3))# 110
print(golomb_coding(2, 3)) # 111

print("Best Golomb : " + str(optimal_golomb_coding(115, 0.9)))
print(bernoulli_golomb_coding([115,115,115,115,1]))
print(golomb_coding(115, 1)) # 111



