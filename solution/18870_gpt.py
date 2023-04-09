n = int(input())  # 좌표의 개수 입력
coordinates = list(map(int, input().split()))  # 좌표값 입력

# 정렬된 배열에서 각 좌표값이 몇 번째 위치에 있는지 찾음
sorted_coordinates = sorted(set(coordinates))
coordinate_dict = {coordinate: i for i,
                   coordinate in enumerate(sorted_coordinates)}

# 새로운 좌표값으로 변환한 값을 출력
for coordinate in coordinates:
    print(coordinate_dict[coordinate], end=" ")
