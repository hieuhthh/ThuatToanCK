
# Tính tổng diện tích của đa giác lồi n đỉnh
def polygon_area(points):
    # Độ phức tạp thời gian: O(n)
    # Độ phức tạp không gian: O(1)
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

# Tìm 2 đỉnh mà đường chéo của nó chia đa giác thành 2 phần có diện tích chênh lệch ít nhất
def min_area_difference(points):
    n = len(points)
    total_area = polygon_area(points) # diện tích đa giác tổng
    diff_min = total_area
    i_min = 0
    j_min = 0

    # Độ phức tạp thời gian: O(n^2)
    # Độ phức tạp không gian: O(1)
    for i in range(n):
        area = 0
        for j in range(i + 2, n):
            # Mỗi lần chỉ cần cộng thêm diện tích tam giác vào phần mới
            area += polygon_area([points[i], points[j - 1], points[j]])  # O(1) do đa giác cần tính này chỉ là tam giác

            diff = abs(area - (total_area - area))

            if diff < diff_min:
                diff_min = diff
                i_min = i
                j_min = j

    return i_min + 1, j_min + 1

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
