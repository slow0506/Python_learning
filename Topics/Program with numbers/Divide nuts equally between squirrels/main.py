N = int(input())
K = int(input())
nuts = (K - (K % N)) / N
print(int(nuts))
