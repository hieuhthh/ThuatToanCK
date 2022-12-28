from math import acos, sqrt, pi

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def intersection(x1, y1, x2, y2, r):
    d = distance(x1, y1, x2, y2) / 2
    a = acos(d / r) # Đúng ra a = acos(d / r) / (2pi) mới ra tỉ lệ
    part_circle = r**2 * a * 0.5 # Đúng ra part_circle = pi * r**2 * a
    h = sqrt((r**2 - d**2))
    triangle = 0.5 * h * d
    ans = 4 * (part_circle - triangle)
    return ans

def union(x1, y1, x2, y2, r):
    ans = pi * r**2 * 2 - intersection(x1, y1, x2, y2, r)
    return format(ans, '.3f') # làm tròn 3 chữ số thập phân

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    x1, y1, x2, y2, r = lines[0]
    print('x1, y1, x2, y2, r =', x1, y1, x2, y2, r)

    ans = union(x1, y1, x2, y2, r)
    print(ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))