# #include <bits/stdc++.h>

# using namespace std;

# const int N = 1e3 + 10;

# int k, n, m; 
# int f[N][N];
# pair<int, int> a[N]; 

# void solve() {
#     cin >> k >> n >> m; 
#     for (int i = 1; i <= k; ++i) {
#         cin >> a[i].first >> a[i].second; 
#     }
#     sort(a + 1, a + 1 + k, greater<pair<int, int>>()); 
#     for (int i = 1; i <= k; ++i) { 
#         f[i][0] = f[i - 1][0] + (i <= n ? a[i].first : 0); 
#         for (int j = 1; j <= m; ++j) { 
#             f[i][j] = max(f[i - 1][j] + (i - j <= n ? a[i].first : 0), f[i - 1][j - 1] + a[i].second); 
#         }
#     }
#     cout << f[k][m] << endl; 
# }

def solve(arr, k, n, m):
    ar.sort(key=lambda x: (-x[0],-x[1]))
    f = [[0 for i in range(k + 1)] for j in range(k + 1)]
    for i in range(1, k + 1):
        f[i][0] = f[i - 1][0] + (ar[i - 1][0] if i <= n else 0)
        for j in range(1, m + 1):
            f[i][j] = max(f[i - 1][j] + (ar[i - 1][0] if i - j <= n else 0), f[i - 1][j - 1] + ar[i - 1][1])
    return f[k][m]

if __name__ == "__main__":
    inp = open('input.txt', 'r')
    out = open('output.txt', 'w')
    k, n, m = map(int, inp.readline().split())
    ar = []
    for i in range(k):
        first, second = map(int, inp.readline().split())
        ar.append((first, second))
    ans = solve(ar, k, n, m)
    
    inp.close()
    out.write(f"{ans}")
    out.close()    