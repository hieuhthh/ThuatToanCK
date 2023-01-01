def f_func(n):
    sieve = [False for _ in range(2*n + 2)]
    sieve[0] = sieve[1] = True
    p = []
    ans = 1
    for i in range(2, 2*n + 1):
        if (sieve[i] == False):
            for j in range(2 * i, 2*n + 1, i):
                sieve[j] = True

            p.append(i)
            low = 1
            high = len(p) - 1
            pos = -1
            while (low <= high):
                mid = (low + high) // 2
                if (p[mid] + i <= 2*n):
                    pos = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            
            ans += max(pos, 0)
    
    return ans

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    n = lines[0][0]
    print('n =', n)
    ans = f_func(n)
    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))