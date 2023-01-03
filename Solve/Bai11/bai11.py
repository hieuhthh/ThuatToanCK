def solve(arr, k, n, m):
    # Sort giảm dần theo nhóm loại 1, nếu bằng nhau thì giảm dần theo nhóm loại 2
    arr.sort(key=lambda x: (-x[0],-x[1]))

    # Nếu chỉ phải phân vào nhóm loại 1
    # -> Sort dãy lại theo nhóm 1 giảm dần rồi lấy n cụm đầu tiên phân vào nhóm 1

    # Ta có 2 nhóm (loại 1, 2)
    # Sort giảm dần theo nhóm loại 1, nếu bằng nhau thì giảm dần theo nhóm loại 2

    # Tư tưởng chính là khi đã sort theo nhóm 1 giảm dần, 
    # nếu ko chọn vào nhóm 2 thì luôn lấy nó vào nhóm 1 nếu còn chỗ trống

    # Khởi tạo mảng f
    # f[i, j] là tổng trọng số lớn nhất khi xét đến cụm i và chọn j cụm vào nhóm 2

    # Giả sử đang xét đến i cụm đầu tiên trong dãy mà đã phân j cụm vào nhóm 2
    # trong i - j cụm còn lại nếu i - j <= n thì ta sẽ chọn hết vào nhóm 1
    # ngược lại thì mình chọn n cụm đầu tiên trong i - j cụm còn lại vào nhóm 1

    # Công thức truy hồi
    # TH1: Chọn cụm i vào nhóm 1: 
    #   f(i, j) = f(i - 1, j) + a(i) nếu i - j <= n hoặc f(i, j) = f(i - 1, j) nếu i - j > n
    # TH2: chọn cụm i vào nhóm 2:
    #   f(i, j) = f(i - 1, j - 1) + b(i)

    f = [[0 for i in range(k + 1)] for j in range(k + 1)]
        
    for i in range(1, k + 1):
        f[i][0] = f[i - 1][0] + (arr[i - 1][0] if i <= n else 0)
        for j in range(1, m + 1):
            f[i][j] = max(f[i - 1][j] + (arr[i - 1][0] if i - j <= n else 0), f[i - 1][j - 1] + arr[i - 1][1])

    return f[k][m]

if __name__ == "__main__":
    inp = open('input.txt', 'r')
    out = open('output.txt', 'w')
    k, n, m = map(int, inp.readline().split())
    
    arr = []

    for i in range(k):
        first, second = map(int, inp.readline().split())
        arr.append((first, second))

    print('arr =', arr)

    ans = solve(arr, k, n, m)
    print('ans =', ans)
    
    inp.close()
    out.write(f"{ans}")
    out.close()    