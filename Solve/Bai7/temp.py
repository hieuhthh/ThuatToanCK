def solve(arr):
    # 2 con trỏ
    # Độ phức tạp thời gian: O(n)
    # Độ phức tạp không gian: O(1)
      
    left = 0
    right = len(arr) - 1
  
    # Lưu giá trị max cho 2 pointer left, right
    l_max = 0
    r_max = 0
  
    ans = 0

    while (left <= right):
        # Kiểm tra min(left_max, right_max)
   
        if r_max <= l_max:
            ans += max(0, r_max - arr[right])
              
            r_max = max(r_max, arr[right])
              
            right -= 1
        else:
            ans += max(0, l_max-arr[left])
              
            l_max = max(l_max, arr[left])
              
            left += 1

    return ans

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [[int(x) for x in line.strip().split(',')] for line in lines]

    arr = lines[0]
    print('arr =', arr)

    ans = solve(arr)

    print('ans =', ans)

    with open('output.txt', 'w') as f:
        f.write(str(ans))
