
#include <iostream>

#define REP(i,N) for (int i = 0; i < N; i++)

using namespace std;


int T, n, k;
double p[400];


int bitsum(int s) {
    if (s == 0) return 0;
    return 1 + bitsum(s & (s-1));
}


double brute() {
    double ans = 0.0;
    REP(subset, 1<<n) if (bitsum(subset) == k) {
        double ptie = 0.0;
        REP(yes, 1<<n) if ((yes & subset) == yes && bitsum(yes) == k/2) {
            double x = 1.0;
            REP(i, n) if ((subset & (1<<i)) > 0) {
                if ((yes & (1<<i)) > 0) x *= p[i];
                else x *= 1.0 - p[i];
            }
            ptie += x;
        }
        ans = max(ans, ptie);
    }
    return ans;
}


int main() {
    cin >> T;
    REP(tc, T) {
        cin >> n >> k;
        REP(i, n) cin >> p[i];
        double ans = brute();
        cout << "Case #" << tc+1 << ": " << ans << endl;        
    }
    return 0;
}

