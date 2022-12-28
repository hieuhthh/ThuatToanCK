from collections import deque

def bfs(adj, i):
    # Khởi tạo các biến cần thiết
    n = len(adj)
    h = [0] * n
    visit = [False] * n
    visit[i] = True
    h[i] = 0

    q = deque([i])

    # bfs
    while q:
        u = q.popleft()
        for v in adj[u]:
            # Nếu chưa đi qua v
            if not visit[v]:
                visit[v] = True
                h[v] = h[u] + 1
                q.append(v)

    # tính tổng khoảng cách từ đỉnh i đến các đỉnh còn lại
    sum = 0
    for i in range(n):
        sum += h[i]

    return sum

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    n = lines[0][0]
    edges = lines[1:n]

    print('n =', n)
    print('edges =', edges)

    adj = [[] for i in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    sum = 0
    for i in range(n + 1):
        sum += bfs(adj, i)

    # ta đã tính từ i -> j và j -> i nên phải chia 2
    ans = sum // 2
    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))