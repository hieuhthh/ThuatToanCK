def kmp_search(a, b):
    # Độ phức tạp thời gian: O(n + m)
    # Độ phức tạp không gian: O(m)

    n = len(a)
    m = len(b)

    # Preprocess the pattern string to generate the partial match table
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and b[i] != b[j]:
            j = lps[j - 1]
        if b[i] == b[j]:
            j += 1
        lps[i] = j

    # Search for all occurrences of the pattern string in the text string
    i = 0
    j = 0
    positions = []
    while i < n:
        if a[i] == b[j]:
            i += 1
            j += 1
        if j == m:
            positions.append(i - j)
            j = lps[j - 1]
        elif i < n and a[i] != b[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return positions

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    a = lines[0].strip()
    print('a =', a)

    b = lines[1].strip()
    print('b =', b)

    ans = kmp_search(a, b)
    print('ans =', ans)

    with open('output.txt', 'w') as f:
        for val in ans:
            f.write(str(val) + ' ')
