#include <bits/stdc++.h>

using namespace std;

const int N = 1e3 + 10;

int k, n, m; 
int f[N][N];
pair<int, int> a[N]; 

void solve() {
    cin >> k >> n >> m; 
    for (int i = 1; i <= k; ++i) {
        cin >> a[i].first >> a[i].second; 
    }
    sort(a + 1, a + 1 + k, greater<pair<int, int>>()); 
    for (int i = 1; i <= k; ++i) { 
        f[i][0] = f[i - 1][0] + (i <= n ? a[i].first : 0); 
        for (int j = 1; j <= m; ++j) { 
            f[i][j] = max(f[i - 1][j] + (i - j <= n ? a[i].first : 0), f[i - 1][j - 1] + a[i].second); 
        }
    }
    cout << f[k][m] << endl; 
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int testCase = 1;
    // cin >> testCase;
    while (testCase--) {
        solve();
    }

    return 0;
}