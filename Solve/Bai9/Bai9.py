def solve(s, p):
    # Trả về chuỗi s có thể được sinh ra từ chuỗi p
    # n = len(s)
    # Độ phức tạp thời gian: O(n) | chúng ta duyệt từng kí tự của chuỗi s
    # Độ phức tạp không gian: O(n) nếu tính luôn bộ nhớ stack | độ sâu của đệ quy bằng với độ dài chuỗi s 

    # Nếu p rỗng, trả về True nếu s rỗng, ngược lại trả về False
    if not p:
        return not s

    # Ta chỉ xét phần đầu của mỗi chuỗi
    
    # Kiểm tra xem có phải trường hợp * 
    if len(p) > 1 and p[1] == '*':
        # Bỏ qua phần * bên p hoặc nếu phần tử đầu giống nhau thì xét tiếp s 
        return solve(s, p[2:]) or (s and s[0] == p[0] and solve(s[1:], p))
    # Kiểm tra xem có phải trường hợp .
    elif p[0] == '.':
        # Thay thế '.' bằng ký tự tương ứng bên s và xét tiếp s và p
        return s and solve(s[1:], p[1:])
    # Kiểm tra xem các ký tự đầu tiên của s và p có giống nhau không
    else:
        return s and s[0] == p[0] and solve(s[1:], p[1:])

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

    s = lines[0]
    print('s =', s)

    p = lines[1]
    print('p =', p)

    ans = solve(s, p)
    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans).lower())
