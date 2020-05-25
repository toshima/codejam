
#include <iostream>

#define REP(i,N) for (int i = 0; i < N; i++)

using namespace std;

// const int MAXE = 1000000001;
long long T, N, Q, E[200], S[200], D[200][200], U[200], V[200], u, v;
double dp[200][200]; // min time from start


// int ok(t) {
// 	REP(i, 200) dp[i] = -1;
// 	q.insert(u)
// 	while (!q.empty()) {
//        int top = *q.begin();
//        q.erase(q.begin());
// 	}
// }


int main() {
	cin >> T;
	REP(tc, T) {
		cin >> N >> Q;
		REP(i, N) cin >> E[i] >> S[i];
		REP(i, N) REP(j, N) cin >> D[i][j];
		REP(i, Q) cin >> U[i] >> V[i];
		cout << "Case #" << tc+1 << ":";
		REP(q, Q) {
			u = U[q] - 1;
			v = V[q] - 1;
			REP(i, N) REP(horse, N) dp[i][horse] = 1e129;
			dp[0][0] = 0.0;
			// cout << "dp" << endl;
			REP(i, N) {
				REP(horse, i+1) {
					long long d = 0;
					for (int j = horse; j <= i; j++) d += D[j][j+1];
					if (d <= E[horse]) {
						// cout << "time" << dp[i][horse] + 1.0 * D[i][i+1]/S[horse] << endl;
						dp[i+1][horse] = min(1.0*dp[i+1][horse], dp[i][horse] + 1.0*D[i][i+1]/S[horse]);
						dp[i+1][i+1] = min(1.0*dp[i+1][i+1], dp[i][horse] + 1.0*D[i][i+1]/S[horse]);
					}
					// cout << dp[i][horse] << " ";
				}
				// cout << endl;
			}
			double ans = 1e129;
			REP(horse, N) ans = min(ans, dp[N-1][horse]);
			cout << " " << ans;
		}
		cout << endl;
	}
	return 0;
}
