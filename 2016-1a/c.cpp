
#include <iostream>
#include <string>

#define REP(i,N) for (int i=0; i<N; i++) 

using namespace std;


int A[2000], seen[2000];


int main() {
	int T, N, x, a, b;
	cin >> T;
	REP(tc, T) {
		cin >> N;
		REP(i, N) {
			cin >> x;
			A[i] = x-1;
		}
		int ans = 0;
		REP(i, N) REP(j, N) {
			REP(k, N) seen[k] = false;
			a = i;
			seen[a] = true;
			int count = 1;
			while (!seen[A[a]]) {
				a = A[a];
				seen[a] = true;
				count++;
			}
			if (A[a] == i || A[A[a]] == a) ans = max(ans, count);
			if (A[A[a]] == a && !seen[b]) {
				b = j;
				seen[b] = true;
				count++;
				while (!seen[A[b]]) {
					b = A[b];
					seen[b] = true;
					count++;
				}
				if (A[b] == a) ans = max(ans, count);
			}
		}
		cout << "Case #" << tc+1 << ": " << ans << endl;
	}
	return 0;
}
