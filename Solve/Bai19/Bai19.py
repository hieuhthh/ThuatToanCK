# def maximum_depth(h, T):
#     n = len(h)
#     dp = [[0] * (T + 1) for _ in range(n)]
#     for i in range(n):
#         dp[i][0] = h[i]
#     for i in range(1, n):
#         for j in range(1, T + 1):
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - 1)
#     return dp[n - 1][T]

def maximum_depth(h, T):
    left, right = 0, max(h)
    ans = -1
    reduce = False
    while left <= right:
        print('left:', left)
        print('right:', right)
        mid = (left + right) // 2
        print('mid:', mid)
        cost = sum(max(hi - mid, 0) for hi in h)
        print('cost:', cost)
        if cost <= T:
            ans = mid
            right = mid - 1
            if cost < T:
                reduce = True
                print('reduce:', reduce)
                print('ans:', ans)
        else:
            left = mid + 1
    print('reduce:', reduce)
    print('ans:', ans)
    print('ans - reduce', ans - reduce)
    return ans - reduce

# def maximum_depth(h, T):
#     left, right = 0, max(h)
#     while left < right:
#         mid = (left + right) // 2
#         cost = sum(max(hi - mid, 0) for hi in h)
#         if cost > T:
#             right = mid
#         else:
#             # Check if the difference between consecutive heights is at most 1
#             valid = True
#             for i in range(1, len(h)):
#                 if h[i] - h[i - 1] > 1:
#                     valid = False
#                     break
#             if valid:
#                 left = mid + 1
#             else:
#                 right = mid
#     return left - 1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    n, T = lines[0]
    print('n =', n)
    print('T =', T)

    h = lines[1][:n]
    print('h =', h)

    ans = maximum_depth(h, T)
    print('ans =', ans)

    # permutation_out = getPermutation(n, y)
    # print('permutation_out =', permutation_out)

    # with open('output.txt', 'w') as f:
    #     f.write(str(position_out) + '\n')
    #     f.write(str(permutation_out))