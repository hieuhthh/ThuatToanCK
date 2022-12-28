# Tính tổng diện tích của đa giác lồi n đỉnh
def polygon_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

# Tìm đường chéo chia đa giác thành 2 phần có diện tích chênh lệch nhau ít nhất
def min_area_difference(points):
    n = len(points)
    min_diff = float('inf')

    # Vét cạn với mọi 2 đỉnh tạo thành 1 đường chéo
    for i in range(n):
        for j in range(i + 1, n):
            list_1 = points[i:j + 1]
            area_1 = polygon_area(list_1)
            list_2 = points[j:] + points[:i + 1]
            area_2 = polygon_area(list_2)
       
            diff = abs(area_1 - area_2)
            
            if diff < min_diff:
                min_diff = diff
                i_save = i
                j_save = j

    print('min_diff:', min_diff)

    return i_save + 1, j_save + 1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    points = lines[1:]
    print('points =', points)

    id_1, id_2 = min_area_difference(points)
    print('id_1 =', id_1)
    print('id_2 =', id_2)

    with open('output.txt', 'w') as f:
        f.write(f"{id_1} {id_2}")
