def solve(a, b):
    # Sắp xếp a, b tăng dần
    a = sorted(a)
    b = sorted(b)

    print('sorted a =', a)
    print('sorted b =', b)

    i = 0
    j = len(b) - 1

    i_min = i
    j_min = j
    min_abs_sum = abs(a[i_min] + b[j_min])
    
    while i < len(a) and j >= 0:
        if abs(a[i] + b[j]) < min_abs_sum:
            i_min = i
            j_min = j
            min_abs_sum = abs(a[i_min] + b[j_min])
            
        if a[i] + b[j] < 0:
            i += 1
        else:
            j -= 1

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
