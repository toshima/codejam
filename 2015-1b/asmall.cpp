
#include <iostream>
#include <cstring>
#include <sstream>

#define REP(i,N) for (int i = 0; i < N; i++)

using namespace std;

long long dp[2000000];

int main() {
	long long T, N, flip;
	cin >> T;
	REP(tc, T) {
		cin >> N;
		dp[0] = 0;
		for (int i = 1; i <= N; i++) {
			dp[i] = dp[i-1] + 1;
			stringstream ss;
			ss << i;
			string s = ss.str();
			reverse(s.begin(), s.end());
			stringstream ss2(s);
			ss2 >> flip;
			if (i % 10 > 0 && flip < i) dp[i] = min(dp[i], dp[flip] + 1);
			// cout << i << " " << flip << " " << dp[i] << endl;
		}
		cout << "Case #" << tc+1 << ": " << dp[N] << endl;
	}
	return 0;
}
