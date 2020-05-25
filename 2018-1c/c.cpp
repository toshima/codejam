#include <cstring>
#include <iostream>
#include <vector>


#define REP(i,N) for (int i = 0; i < (long long)N; i++)

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

const int MAXN = 100000;
const ll INF = 1LL<<59;

ll dp[MAXN+1][2];  // length, index


int solve(vll v) {
    int n = v.size();
    int best = 0;

    REP(j, n) {  // index
        REP(i, j+2) {  // length
            ll x = INF;
            if (j > 0 && dp[i][(j-1)%2] > 0) x = min(x, dp[i][(j-1)%2]);
            if (i == 1) x = min(x, v[j]);
            if (i > 0 && j > 0 && v[j] * 6 >= dp[i-1][(j-1)%2] && dp[i-1][(j-1)%2] > 0) x = min(x, dp[i-1][(j-1)%2] + v[j]);
            if (x < INF) {
                best = max(best, i);
            }
            dp[i][j%2] = x;
            // cout << i << '\t' << j << '\t' << dp[i][j%2] << '\t' << v[j] << '\t' << dp[i-1][(j-1)%2] << endl;
        }
    }
    return best;
}

int main() {
    ll T, N, x;
    cin >> T;
    REP(cs, T) {
        cin >> N;
        vll v;
        REP(i, N) {
            cin >> x;
            v.push_back(x);
        }
        cout << "Case #" << cs+1 << ": " << solve(v) << endl;        
    }
    return 0;
}

