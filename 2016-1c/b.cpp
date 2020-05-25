
#include <iostream>
#include <cassert>

#define REP(i,N) for (int i = 0; i < N; i++)

using namespace std;

bool slide[100][100];


int dfs(int x, int n) {
	if (x == n-1) {
		return 1;
	}
	int ans = 0;
	REP(i, n) if (slide[x][i]) ans += dfs(i, n);
	return ans;
}


int main() {
	int T;
	cin >> T;
	REP(tc, T) {
		long long B, M, M2;
		cin >> B >> M;
		M2 = M;
		if (M > 1LL<<(B-2)) {
			cout << "Case #" << tc+1 << ": IMPOSSIBLE" << endl;
			continue;
		}

		REP(i, B) REP(j, B) slide[i][j] = (j > i) && (i > 0);
		if (M == 1LL<<(B-2)) {
			M--;
			slide[0][B-1] = true;
		}
		long long ind = B-2;
		while (M > 0) {
			slide[0][ind] = M % 2 == 1;
			M /= 2;
			ind--;
		}

		cout << "Case #" << tc+1 << ": POSSIBLE" << endl;
		REP(i, B) {
			REP(j, B) cout << (slide[i][j] ? 1 : 0);
			cout << endl;
		}
		// assert(dfs(0, B) == M2);
	}
}