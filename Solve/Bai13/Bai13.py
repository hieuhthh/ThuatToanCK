import math
from copy import deepcopy

def convex_hull(points):
    """
    Độ phức tạp thời gian: O(nlogn)
    Độ phức tạp không gian: O(n)
    """
    # Sắp xếp các điểm theo tọa độ x tăng dần
    points.sort(key=lambda p: p[0])
    # Tìm ra điểm có tọa độ y nhỏ nhất
    bottommost_point = min(points, key=lambda p: p[1])
    # Xóa điểm này khỏi tập điểm và thêm nó vào mảng points_on_hull
    points.remove(bottommost_point)
    points_on_hull = [bottommost_point]
    # Sắp xếp lại tập điểm theo góc tính từ điểm bottommost_point
    points.sort(key=lambda p: angle(bottommost_point, p))
    # Thêm các điểm vào points_on_hull
    for point in points:
        while len(points_on_hull) > 1 and not is_left(points_on_hull[-2], points_on_hull[-1], point):
            points_on_hull.pop()
        points_on_hull.append(point)
    # Trả về hình chữ nhật bao quanh tập điểm
    return points_on_hull

def angle(p1, p2):
    # Tính góc tính từ điểm p1 đến điểm p2 (theo độ)
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def is_left(p1, p2, p3):
    # Kiểm tra xem điểm p3 có phải bên trái đường thẳng qua p1 và p2 hay không
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) > 0

def find_centers(points_on_hull):
    # Tìm ra 2 góc của hình chữ nhật
    corner1 = min(points_on_hull, key=lambda p: (p[0], p[1]))
    corner2 = max(points_on_hull, key=lambda p: (p[0], p[1]))
    # Trả về 2 góc của hình chữ nhật làm 2 điểm trung tâm
    return corner1, corner2

def find_centers_of_split(points):
    ori_points = deepcopy(points)
    points_on_hull = convex_hull(points)

    print('points_on_hull =', points_on_hull)

    corner1, corner2 = find_centers(points_on_hull)

    print('corner1 =', corner1)
    print('corner2 =', corner2)

    return ori_points.index(corner1) + 1, ori_points.index(corner2) + 1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    points = lines[1:]
    print('points =', points)

    id_corner1, id_corner2 = find_centers_of_split(points)
    print('id_corner1 =', id_corner1)
    print('id_corner2 =', id_corner2)

    with open('output.txt', 'w') as f:
        f.write(f"{id_corner1} {id_corner2}")
