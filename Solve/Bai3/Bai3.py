def solve(a, b):
    # Sắp xếp a, b tăng dần
    # sorted dùng Tim Sort, là sự kết hợp của merge sort và insertion sort
    # Độ phức tạp thời gian: O(n*log(n))
    # Độ phức tạp không gian: O(n)
    a = sorted(a)
    b = sorted(b)

    print('sorted a =', a)
    print('sorted b =', b)

    i = 0
    j = len(b) - 1

    i_min = i
    j_min = j
    min_abs_sum = abs(a[i_min] + b[j_min])
    
    # Ta duyệt mảng a, b từ 2 hướng ngược nhau
    # Duyệt mảng a từ 0, từ nhỏ đến lớn
    # Duyệt mảng b từ len(b) - 1 về ngược 0, từ lớn đến nhỏ
    # Tổng a[i] + b[j] < 0, có nghĩa là ta cần tăng giá trị bên mảng a lên -> i += 1
    # Tổng a[i] + b[j] > 0, có nghĩa là ta cần giảm giá trị bên mảng b xuống -> j -= 1
    # Trong bước này:
    # Độ phức tạp thời gian: O(m + n)
    # Độ phức tạp không gian: O(1)

    while i < len(a) and j >= 0:
        if abs(a[i] + b[j]) < min_abs_sum:
            i_min = i
            j_min = j
            min_abs_sum = abs(a[i_min] + b[j_min])
            
        if a[i] + b[j] < 0:
            i += 1
        elif a[i] + b[j] > 0:
            j -= 1
        else: 
            # a[i] + b[j] == 0
            return min_abs_sum

    # Tóm lại cả thuật toán:
    # Độ phức tạp thời gian: O(n*log(n))
    # Độ phức tạp không gian: O(n)

    return min_abs_sum

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]
    
    a = lines[1]
    b = lines[2]

    print('a =', a)
    print('b =', b)

    ans = solve(a, b)
    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))
