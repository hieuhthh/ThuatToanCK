from collections import deque

def bfs(n):
    """
    Tập hợp các bội của một số nguyên a là {0, a, 2a, 3a, ...}
    Ở đây ta tạm không xét trường hợp 0
    n nguyên dương -> n > 0
    d = bằng số chữ số tối đa của m | m là bội của n, chứa toàn 0, 1
    Độ phức tạp thời gian: O(2^d)
    Độ phức tạp không gian: O(2^d)
    """

    if n == 1:
        return 1

    # Khởi tạo các biến cần thiết
    q = deque([1])

    # Có thể chạy trong O(N)
    # sử dụng tính chất (a + b ) % N = a % n + b % n
    # Tương tự (a * b ) % n
    # thì với m = '10' và n = 7 thì m % n = 3
    # mà khi xét tiếp theo ta có m = '101' với m % n = 3 (nhưng 101 > 10 thì ta sẽ không cần cải tiến từ 101 trở về sau nữa vì không tối ưu bằng)
    # nên thay đổi lại trong code này là thêm mảng đánh dấu
    flag = [False for i in range(n)]
    # bfs
    while q:
        u = q.popleft()
        for v in range(2):
            val = u * 10 + v
            
            if val % n == 0:
                return val
                                    # Thêm điều kiện này
            if len(str(val)) < 9: #  and flag[val % n] == False:
                q.append(val)
                # và này, flag[val % n] = True

    return -1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    n = lines[0][0]
    print('n =', n)

    ans = bfs(n)
    
    if ans == -1:
        ans = 'Not found'

    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))