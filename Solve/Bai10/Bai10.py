def solve(matrix, find=1):
    """
    Hàm tìm độ dài cạnh hình chữ nhật lớn nhất toàn số {find}
    Độ phức tạp thời gian: O(m*n)
    Độ phức tạp không gian: O(m*n)
    """
    row = len(matrix)
    col = len(matrix[0])

    # khởi tạo hàm f, f[i][j] chứa độ dài cạnh của hình vuông có góc phải dưới ở ô [i,j]
    # f[i][j] = (matrix[i][j]==find) với hàng đầu và cột đầu, các ô còn lại = 0
    f = []
    for i in range(row):
        temp = []
        for j in range(col):
            if i == 0 or j == 0:
                temp.append(int(matrix[i][j] == find))
            else:
                temp.append(0)
        f.append(temp)

    # cập nhật mảng f
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == find:
                f[i][j] = min(f[i][j - 1], f[i - 1][j], f[i - 1][j - 1]) + 1
            else:
                f[i][j] = 0
 
    # tìm cạnh hình vuông lớn nhất
    ans = f[0][0]

    for i in range(row):
        for j in range(col):
            if (ans < f[i][j]):
                ans = f[i][j]

    return ans

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    arr = lines[1:]
    print('arr =', arr)

    ans_1 = solve(arr, find=1)
    print('ans_1 =', ans_1)

    ans_0 = solve(arr, find=0)
    print('ans_0 =', ans_0)

    ans = max(ans_1, ans_0)
    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))
