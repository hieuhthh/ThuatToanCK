def sang_nguyen_to(n):
    # Độ phức tạp thời gian: O(n*log(log(n)))
    # Độ phức tạp không gian: O(n)

    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False

    p = 2

    while (p * p <= n):
        if is_prime[p] == True:
            # Nếu p là số nguyên tố thì bội của p không phải số nguyên tố
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
  
    return is_prime

def g_func(n):
    # Độ phức tạp thời gian: O(n)
    # Độ phức tạp không gian: O(1)

    global is_prime

    cnt = 0

    for i in range(2, n + 1):
        if is_prime[i] and is_prime[2 * n - i]:
            # p + q == 2 * n
            # p, q là số nguyên tố
            cnt += 1

    return cnt
   
def f_func(n):
    # Độ phức tạp thời gian: O(n^2)
    # Độ phức tạp không gian: O(1)
    
    # Khởi tạo biến tổng là 0
    ans = 0

    # Duyệt từ 2 đến n và cộng tất cả g(n)
    for i in range(2, n + 1):
        ans += g_func(i)
  
    return ans

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    n = lines[0][0]
    print('n =', n)

    is_prime = sang_nguyen_to(2 * n)
    ans = f_func(n)
    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))
