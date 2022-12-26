def find_gcd(a, b):
    # Tìm ước chung lớn nhất của hai số a và b bằng thuật toán Euclid
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def find_subsequence(arr, k):
    # Tìm đoạn con độ dài k có ước chung lớn nhất
    # Ta xem như với mỗi vị trí bắt đầu i, i = 1..n - k
    # ta duyệt chuỗi con độ dài k để tìm gcd
    # mỗi phép tìm gcd tốn log(d) với d là phần tử lớn nhất của đoạn con.
    # Tóm lại độ phức tạp thời gian của thuật toán này là N*K*log(D)
    # với N là độ dài của mảng, K là độ dài đoạn con, D là giá trị phần tử lớn nhất mảng.
    # Độ phức tạp không gian là O(1)
    result = -1
    for i in range(len(arr) - k + 1):
        # Tìm ước chung lớn nhất của đoạn con độ dài k bắt đầu từ phần tử thứ i 
        gcd = arr[i]
        for j in range(i + 1, i + k):
            gcd = find_gcd(gcd, arr[j])
            if gcd == 1:
                # Nếu gcd của đoạn con tới thời điểm này = 1 thì break luôn khỏi cần đi tiếp
                break
        result = max(result, gcd)
    return result

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]
    
    n = lines[0][0]
    k = lines[0][1]
    arr = lines[1]

    print('n =', n)
    print('k =', k)
    print('arr =', arr)

    ans = find_subsequence(arr, k)
    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))
