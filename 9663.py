# if (x+i < N and y+i < N):
#             array[x+i][y+i] = 1
#         if (x+i < N and 0 <= y-i):
#             array[x+i][y-i] = 1
#         if (0 <= x-i and y+i < N):
#             array[x-i][y+i] = 1
#         if (0 <= x-i and 0 <= y-i):
#             array[x-i][y-i] = 1


def pooling(array, x, y):
    sum = 0
    for i in range(N):
        # row pooling
        sum += array[i][y]
        # col pooing
        sum += array[x][i]
        # cross pooling
        if (x+i < N and y+i < N):
            sum += array[x+i][y+i]
        if (x+i < N and 0 <= y-i):
            sum += array[x+i][y-i]
        if (0 <= x-i and y+i < N):
            sum += array[x-i][y+i]
        if (0 <= x-i and 0 <= y-i):
            sum += array[x-i][y-i]
    if (sum != 0):
        return -999
    array[x][y] = 1
    return 111


# create map
# N = int(input())
N = 4
dim = N * N
res = [[[[0 for col in range(N)] for row in range(N)]
        for zzz in range(dim)] for kkk in range(4)]
solution_num = 0

for kkk in range(4):
    i = 0
    j = 0
    for zzz in range(dim):
        if (j // N > 0):
            i += 1
            j = 0
        res[kkk][zzz][i][j] = 1
        j += 1

for k in range(dim):
    cnt = 1
    for i in range(N):
        for j in range(N):
            # 놓을 수 있는 자리면, 놓고 cnt
            if (pooling(res[k], i, j) == 111):
                cnt += 1
    if (cnt == N):
        solution_num += 1

# print result
for zzz in range(dim):
    print(zzz)
    for i in range(N):

        print(res[zzz][i])
    print('--------------------')
print('--------------------')
print(solution_num)
