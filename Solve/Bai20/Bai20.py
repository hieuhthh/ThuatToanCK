import math

def getPermutation(n, k):
    ans = ''
    nums = list(map(str, range(1, n + 1)))
    fact = math.factorial(len(nums) - 1)
    k -= 1
    while k:
        i, k = divmod(k, fact)
        ans += nums.pop(i) + ' '
        fact //= len(nums)         
    ans += ' '.join(nums)
    return ans

def getPosition(n, p):
    # Thêm vào để mảng bắt đầu từ 1
    p = [0] + p
    check = [False for _ in range(n + 1)]
    k = 0
    for i in range(1, n + 1):
        d = 0
        for j in range(1, p[i] + 1):
            if not check[j]:
                d += 1
        k += (d - 1) * math.factorial(n - i)
        check[p[i]] = True
    return k + 1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(' ')] for line in lines]

    p = lines[0]
    print('p =', p)

    y = lines[1][0]
    print('y =', y)

    n = len(p)
    print('n =', n)

    position_out = getPosition(n, p)
    print('position_out =', position_out)

    permutation_out = getPermutation(n, y)
    print('permutation_out =', permutation_out)

    with open('output.txt', 'w') as f:
        f.write(str(position_out) + '\n')
        f.write(str(permutation_out))