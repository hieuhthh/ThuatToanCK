MXN = 10**5 + 10

# Segment tree
st = [0 for i in range(MXN << 2)]

def gcd(a, b):
    # Tìm ước chung lớn nhất của hai số a và b bằng thuật toán Euclid
    if (a == 0):
        return b
    if (b == 0):
        return a
    while a % b != 0:
        t = b
        b = a % b
        a = t
    return b

def build(id, value, x, lx, rx):
    """
    Xây dựng segment tree từ dữ liệu ban đầu. 
    id là chỉ số của phần tử muốn thêm vào cây
    value là giá trị của phần tử
    x là chỉ số của nút hiện tại trong mảng st
    lx và rx là chỉ số bắt đầu và kết thúc của khoảng mà nút hiện tại quản lý.
    """
    if lx == rx:
        st[x] = value
        return

    mid = (lx + rx) >> 1

    if (id <= mid):
        build(id, value, x * 2 + 1, lx, mid)
    else:
        build(id, value, x * 2 + 2, mid + 1, rx)

    st[x] = gcd(st[2 * x + 1], st[2 * x + 2])

def get(l, r, x, lx, rx):
    """
    Lấy giá trị ước chung lớn nhất của các phần tử trong khoảng [l, r] trong cây phân đoạn. 
    l và r là chỉ số bắt đầu và kết thúc của khoảng cần tìm
    x, lx, và rx tương tự như trong hàm build().
    """
    if (r < lx or rx < l):
        return 0

    if (l <= lx and rx <= r):
        return st[x]
    
    mid = (lx + rx) >> 1
    left = get(l, r, 2 * x + 1, lx, mid)
    right = get(l, r, 2 * x + 2, mid + 1, rx)
    
    return gcd(left, right)

def find_subsequence(arr, k, n):
    """
    Tìm giá trị ước chung lớn nhất của các phần tử liên tiếp có độ dài là k 
    trong mảng arr có độ dài là n
    Hàm build và get đều có độ phức tạp là O(log n) (do đây là cây phân đoạn)
    nên độ phức tạp thời gian của tổng thuật toán là O(nlogn).
    Độ phức tạp không gian là O(n).
    """
    for i in range(n):
        build(i, arr[i], 0, 0, n - 1)

    answer = 0

    for i in range(n - k + 1):
        answer = max(answer, get(i, i + k - 1, 0, 0, n - 1))

    return answer
        
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split()] for line in lines]
    
    n = lines[0][0]
    k = lines[0][1]
    arr = lines[1]

    print('n =', n)
    print('k =', k)
    print('arr =', arr)

    ans = find_subsequence(arr, k, n)
    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))