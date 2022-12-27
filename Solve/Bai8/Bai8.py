def solve(n):
    """
    Độ phức tạp thời gian: O(n!) | có n chỗ ở row đầu, n - 1 chỗ row thứ 2, ..., 1 chỗ row thứ n -> n!
    Độ phức tạp không gian: O(n^2) | để lưu res (board)
    """
    def backtrack(row, pList, res):
        """
        row: đang xét hàng thứ mấy (int)
        pList[i]: trả về col đặt hậu của row i
        res: lưu mảng output
        """
        if row == n:
            res.append(['.' * x + 'Q' + '.' * (n-1-x) for x in pList])
            return

        if row > n:
            return

        for col in range(n):
            if check(col, row, pList):
                backtrack(row + 1, pList + [col], res)

    def check(col, row, pList):
        """
        đảm bảo row khác nhau rồi
        -> chỉ cần check xem có cùng cột hay đường chéo
        """
        for r in range(row):
            if pList[r] == col or row - r == abs(col - pList[r]):
                return False

        return True

    res = []
    backtrack(0, [], res)
    res =  ['\n'.join(output) for output in res]

    return res

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(',')] for line in lines]

    n = lines[0][0]
    print('n =', n)

    ans = solve(n)

    with open('output.txt', 'w') as f:
        for val in ans:
            f.write(val + '\n\n')
            print(val + '\n')
