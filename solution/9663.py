def check(array, x, y):
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
    if (sum == 0):
        return True
    return False


# create map
# N = int(input())
N = 8
dim = N * N
res = [[[[0 for col in range(N)] for row in range(N)]
        for zzz in range(dim)] for kkk in range(2)]
solution_num = 0


def inner_index(_res, _x, _y):
    if (0 <= _x and _x < N and 0 <= _y and _y < N):
        if (check(_res, _x, _y) == True):
            return True
    return False


global _cnt


def spin_polling_dis3(_res, _x, _y):
    global _cnt
    # 우우 하
    if (inner_index(_res, _x+1, _y+3) == True):
        _res[_x+1][_y+3] = 1
        _cnt += 1
        spin_polling_dis3(_res, _x+1, _y+3)

        # spin_polling_dis2(_res, _x+1, _y+2)
    # 하하 좌
    if (inner_index(_res, _x+3, _y-1) == True):
        _res[_x+3][_y-1] = 1
        _cnt += 1
        spin_polling_dis3(_res, _x+3, _y-1)

        # spin_polling_dis2(_res, _x+2, _y-1)
    # 좌좌 상
    if (inner_index(_res, _x-1, _y-3) == True):
        _res[_x-1][_y-3] = 1
        _cnt += 1
        spin_polling_dis3(_res, _x-1, _y-3)

        # spin_polling_dis2(_res, _x-1, _y-2)
    # 상상 우
    if (inner_index(_res, _x-3, _y+1) == True):
        _res[_x-3][_y+1] = 1
        _cnt += 1
        spin_polling_dis3(_res, _x-3, _y+1)

        # spin_polling_dis2(_res, _x-2, _y+1)


def spin_polling_dis2(_res, _x, _y):
    global _cnt
    # 우우 하
    if (inner_index(_res, _x+1, _y+2) == True):
        _res[_x+1][_y+2] = 1
        _cnt += 1
        spin_polling_dis2(_res, _x+1, _y+2)
    # 하하 좌
    if (inner_index(_res, _x+2, _y-1) == True):
        _res[_x+2][_y-1] = 1
        _cnt += 1
        spin_polling_dis2(_res, _x+2, _y-1)
    # 좌좌 상
    if (inner_index(_res, _x-1, _y-2) == True):
        _res[_x-1][_y-2] = 1
        _cnt += 1
        spin_polling_dis2(_res, _x-1, _y-2)
    # 상상 우
    if (inner_index(_res, _x-2, _y+1) == True):
        _res[_x-2][_y+1] = 1
        _cnt += 1
        spin_polling_dis2(_res, _x-2, _y+1)


for kkk in range(1):
    i = 0
    j = 0
    for zzz in range(dim):
        if (j == N):
            i += 1
            j = 0
        res[0][zzz][i][j] = 1
        _cnt = 1
        spin_polling_dis3(res[kkk][zzz], i, j)
        spin_polling_dis2(res[kkk][zzz], i, j)
        if (_cnt == N):
            solution_num += 1
        j += 1

# print result
for zzz in range(dim):
    print('L turn', zzz, 'R turn')
    for i in range(N):
        print(res[0][zzz][i], res[1][zzz][i])
        # print(res[1][zzz][i])
    print('--------------------')
print('--------------------')
print(int(solution_num/2))

# [0, 0, 0, 0, 0, *, 0, 0]
# [0, 0, *, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, *, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, *, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [*, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, *, 0, 0, 0, 0]
