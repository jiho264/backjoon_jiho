N = int(input())

dja = input()
input_array = list(map(int, dja.split()))

num = input_array
arr = sorted(list(set(num)))

for i in range(N):
    print(arr.index(num[i]), end=" ")
