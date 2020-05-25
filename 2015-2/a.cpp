
#include <iostream>
#include <cstring>

#define REP(i,N) for (int i = 0; i < N; i++)
#define REPD(i,N) for (int i = N-1; i >= 0; i--)

using namespace std;


int T, R, C;
string A[1000];


int main() {
    cin >> T;
    REP(tc, T) {
        cin >> R >> C;
        REP(i, R) cin >> A[i];
        bool imp = false;
        REP(i, R) REP(j, C) {
            if (A[i][j] == '.') continue;
            bool seen = false;
            REP(k, R) if (k != i && A[k][j] != '.') {
                seen = true;
                break;
            }
            REP(k, C) if (k != j && A[i][k] != '.') {
                seen = true;
                break;
            }
            if (!seen) imp = true;
        }
        if (imp) {
            cout << "Case #" << tc+1 << ": IMPOSSIBLE" << endl;
            continue;
        }

        int ans = 0;
        REP(i, R) {
            REP(j, C) {
                if (A[i][j] == '<') ans++;
                if (A[i][j] != '.') break;
            }
            REPD(j, C) {
                if (A[i][j] == '>') ans++;
                if (A[i][j] != '.') break;
            }
        }
        REP(j, C) {
            REP(i, R) {
                if (A[i][j] == '^') ans++;
                if (A[i][j] != '.') break;
            }
            REPD(i, R) {
                if (A[i][j] == 'v') ans++;
                if (A[i][j] != '.') break;
            }
        }
        cout << "Case #" << tc+1 << ": " << ans << endl;
    }
    return 0;
}
