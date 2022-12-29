from collections import deque
from copy import deepcopy

def bfs(a):
    """
    Ta luôn có cách giải bài này
    VD: mảng 5 phần tử là 1 hoán vị của 1, 2, 3, 4, 5
    Ta đảo lần đầu từ đầu đến vị trí có số 5 -> số 5 lên đầu
    Đảo từ đầu đến cuối -> số 5 xuống cuối
    Tương tự đảo từ đầu đến vị trí số 4 -> số 4 lên đầu
    Đảo từ đầu đến vị trí thứ 4, số 4 về vị trí thứ 4
    Tương tự như vậy ...
    Tốn tối đa 2n thao tác để đảo mảng thành tăng dần
    -> BFS để tìm cách đảo nhanh nhất, đảm bảo có lời giải khi vét
    """
    # Khởi tạo các biến cần thiết
    n = len(a)
    visit = {}
    visit[tuple(a)] = 0
    # visit[u]: chứa số bước để đạt đến trạng thái u từ trạng thái đầu

    q = deque([a])

    # bfs
    while q:
        u = q.popleft()
        tuple_u = tuple(u)

        # mảng đã sắp tăng dần
        if u == sorted(u):
            return visit[tuple_u]

        for i in range(1, n + 1):
            v = deepcopy(u)
            # Đảo ngược từ đầu đến vị trí i
            v[:i] = v[:i][::-1]
            tuple_v = tuple(v)
            # Nếu chưa duyệt v
            if tuple(v) not in visit:
                visit[tuple_v] = visit[tuple_u] + 1
                q.append(v)

    return -1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    n = lines[0][0]
    a = lines[1][:n]

    print('n =', n)
    print('a =', a)

    ans = bfs(a)
    if ans == -1:
        ans = 'Not found'

    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))