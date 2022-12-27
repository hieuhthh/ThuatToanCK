def solve(arr):
    # Độ phức tạp thời gian: O(n)
    # Độ phức tạp không gian: O(n)

    # left[i] là chiều cao cao nhất từ trái tới i
    left = [0] * len(arr)
  
    # right[i] là chiều cao cao nhất từ phải tới i
    right = [0] * len(arr)
  
    ans = 0
  
    # tính mảng left
    left[0] = arr[0]
    for i in range(1, len(arr)):
        left[i] = max(left[i - 1], arr[i])
  
    # tính mảng right
    right[len(arr) - 1] = arr[len(arr) - 1]
    for i in range(len(arr) - 2, -1, -1):
        right[i] = max(right[i + 1], arr[i])
  
    # với mỗi vị trí i, tìm min(left[i], right[i]) rồi trừ arr[i] ra được lượng nước tại vị trí i
    for i in range(0, len(arr)):
        ans += min(left[i], right[i]) - arr[i]
  
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
