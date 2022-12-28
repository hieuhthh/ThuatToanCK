from collections import deque

def bfs(n):
    """
    Tập hợp các bội của một số nguyên a là {0, a, 2a, 3a, ...}
    Ở đây ta tạm không xét trường hợp 0
    n nguyên dương -> n > 0
    """

    if n == 1:
        return 1

    # Khởi tạo các biến cần thiết
    q = deque([1])

    # bfs
    while q:
        u = q.popleft()
        for v in range(2):
            val = u * 10 + v
            
            if val % n == 0:
                return val

            if len(str(val)) < 9:
                q.append(val)

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