def merge_sort_count_inversion(a):
    # Độ phức tạp thời gian: O(n*log(n))
    # Độ phức tạp không gian: O(n)
    
    # Trường hợp mảng có 0 hoặc 1 phần tử
    if len(a) <= 1:
        return 0

    # Chia mảng làm 2 nửa
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    # Gọi hàm merge sort đệ quy vào 2 nửa
    left_count = merge_sort_count_inversion(left)
    right_count = merge_sort_count_inversion(right)

    # Merge lại và đếm số cặp nghịch nhau
    count = left_count + right_count
    i = 0
    j = 0

    for k in range(len(a)):
        if i == len(left):
            # Duyệt hết mảng left thì gán mảng right còn lại vào
            a[k] = right[j]
            j += 1
        elif j == len(right):
            # Duyệt hết mảng right thì gán mảng left còn lại vào
            a[k] = left[i]
            i += 1
        # gán sao cho mảng a tăng dần
        elif left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            # left[i] > right[j]
            # mà left ở trước right
            # thỏa điều kiện a[i] > a[j] và i < j
            a[k] = right[j]
            j += 1
            # left[i] > right[j] -> left[i + 1, ..., len(left) - 1] > right[j]
            count += len(left) - i

    return count


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    a = lines[1]
    print('a =', a)

    ans = merge_sort_count_inversion(a)
    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))
