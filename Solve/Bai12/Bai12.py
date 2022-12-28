from math import sqrt

def solve(s):
    """
    s: Diện tích hình vuông (nguyên dương)
    s = r^2 (r là số thực)
    r^2 = a^2 + b^2
    Nếu tìm được a, b nguyên
    -> có thể xây dựng hình vuông diện tích s với các đỉnh tọa độ nguyên.
    (0, 0)
    (a, b)
    (a + b, b - a)
    (b, -a)
    Độ phức tạp thời gian: O(sqrt(s))
    Độ phức tạp không gian: O(1)
    """
    for a in range(1, int(sqrt(s)) + 1):
        b_sqr = s - a**2
        b = int(sqrt(b_sqr))
        if sqrt(b_sqr) == b:
            return a, b

    return None, None

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    s = lines[0][0]
    print('s =', s)

    with open('output.txt', 'w') as f:
        a, b = solve(s)

        if a is None:
            print('Impossible')
            f.write('Impossible')
        else:
            print(0, 0)
            print(a, b)
            print(a + b, b - a)
            print(b, -a)

            f.write("0, 0\n")
            f.write(str(a) + ' ' + str(b) + '\n')
            f.write(str(a + b) + ' ' + str(b - a) + '\n')
            f.write(str(b) + ' ' + str(-a) + '\n')

    
        
