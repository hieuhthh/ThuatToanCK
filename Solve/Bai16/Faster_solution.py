MXN = 10**5
size_subtree = [0 for i in range(MXN + 4)]
depth = [0 for i in range(MXN + 4)]

def dfs(start, parent, deep):
    global adj
    depth[start] = deep
    size_subtree[start] = 1
    for next_node in adj[start]:
        if (next_node == parent):
            continue
        dfs(next_node, start, deep + 1)
        size_subtree[start] += size_subtree[next_node]
    
    

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    n = lines[0][0]
    edges = lines[1:n]

    print('n =', n)
    print('edges =', edges)

    adj = [[] for i in range(n + 1)]
    print(edges)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dfs(1, -1, 0)
    sum = 0
    for u, v in edges:
        children = u if depth[u] > depth[v] else v
        sum += 1 * size_subtree[children] * (n - size_subtree[children])
     

    # ta đã tính từ i -> j và j -> i nên phải chia 2
    # ans = sum // 2
    ans = sum
    print('ans =', ans)

    # with open('output.txt', 'w') as f:
    #     f.write(str(ans))