def merge(left, right):
    # n = len(left)
    # m = len(right)
    # Độ phức tạp thời gian: O(n + m) | hàm sẽ duyệt qua tất cả các phần tử trong hai dãy con
    # Độ phức tạp không gian: O(n + m) | hàm sẽ tạo ra một dãy mới có độ dài là n + m

    # Gộp hai dãy con lại với nhau
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Nếu còn phần tử trong một trong hai dãy, thêm các phần tử còn lại vào kết quả
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    arrs = lines[1:]
    print('arrs =', arrs)

    ans = arrs[0]

    for a in arrs[1:]:
        ans = merge(ans, a)

    print('ans =', ans)

    with open('output.txt', 'w') as f:
        for val in ans:
            f.write(str(val) + ' ')
