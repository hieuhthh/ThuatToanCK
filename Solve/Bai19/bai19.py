def check(height, ar, cost):
    n = len(ar)
    pref = [0 for i in range(n)]
    
    pref[0] = ar[0]
    
    for i in range(1, n):
        pref[i] = ar[i] + pref[i - 1]
    
    def getPref(l, r):
        """
        Hàm lấy tổng tiền tố từ [l; r]

        Args:
            l (int): biên trái
            r (int): biên phải

        Returns:
            int: Tổng chiều cao các phần tử từ l đến r
        """
        if l:
            return pref[r] - pref[l - 1]
        else:
            return pref[r]
        
    min_cost = 10**20
    
    for i in range(len(ar)):
        # Tìm kiếm nhị phân từ vị trí i trở về trước
        left, right = i, i
        low = 0
        high = i - 1
        while (low <= high):
            mid = (low + high)//2
            if (height + (i - mid) <= ar[mid]):
                left = mid
                high = mid - 1
            else:
                low = mid + 1
                
        # Tìm kiếm nhị phân tiếp bên phải của i
        low = i + 1
        high = n - 1
        while (low <= high):
            mid = (low + high)//2
            if (height + (mid - i) <= ar[mid]):
                right = mid
                low = mid + 1
            else:
                high = mid - 1

        # print(left, right, height)
        
        amount_left = i - left + 1
        amount_right = right - i + 1

        """
            Dùng công thức toán tính tổng các phần tử nguyên liên tiếp từ a đến b là a + (a + 1) + ... + (b - 1) + b = (a + b)*(b - a + 1)//2
        """
        
        cost_placement = (amount_left * (2*height + (i - left))//2) + (amount_right * (2*height + (right - i)) // 2)
        #                                                                        trừ lại chi phí này do chúng ta có tính trùng.
        cost_placement = getPref(left, i) + getPref(i, right) - cost_placement - (ar[i] - height)
        
        min_cost = min(cost_placement, min_cost) 

    # Trả về True/False là có cách để đào đến chiều sâu đó hay không.
    return min_cost <= cost
        
def solve(ar, n, t):
    """
    Tìm kiếm nhị phân độ cao thấp nhất có thể đạt được
    """
    ans = min(ar)

    high = ans - 1
    low = ans - t

    while (low <= high):
        mid = (low + high)//2

        # Giả sử ta có số giá trị của độ cao thấp nhấp là mid, 
        # ta kiểm tra lại xem chi phí đào thêm có vượt quá t hay không.

        if check(mid, ar, t):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
    
if __name__ == "__main__":
    inp = open('input.txt', 'r')
    out = open('output.txt', 'w')
    n, t = map(int, inp.readline().split())
    ar = list(map(int, inp.readline().split()))
    
    ans = solve(ar, n, t)
    print(ans)
    inp.close()
    out.write(f"{ans}")
    out.close()    