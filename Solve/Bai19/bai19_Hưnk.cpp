/**
 *    author:    hungt1
 *    created:   01-01-2023   13:17:39
**/

#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(false); cin.tie(0)

const long long INF = 1e18;
const int N = 1e5 + 1;
int n;
long long T, a[N], sum[N];

int main()
{
    fastio;
    cin >> n >> T;
    for (int i = 1; i <= n; i++){
        cin >> a[i];
        sum[i] = sum[i - 1] + a[i];
    }

    long long low = -INF / n, high = *min_element(a + 1, a + n + 1);
    
    auto check = [&](long long x) -> bool {
        long long minCost = INF;
        int l = 0, r = 0;
        for (int i = 1; i <= n; i++){
            r = max(r, i);
            while (l < i && a[l + 1] <= (x + (i - l))) l++;
            while (r < n && a[r + 1] > (x + (r - i + 1))) r++;
            long long curCost = -x * (r - l + 1) + sum[r] - sum[l];
            minCost = min(minCost, curCost);
        }
        return minCost <= T;
    };
    
    long long ans = high;
    while (low <= high){
        long long mid = (low + high) / 2;
        if (check(mid)){
            ans = mid;
            high = mid - 1;
        }
        else low = mid + 1;
    }

    cout << ans << '\n';
    return 0;
}