
#include <iostream>
#include <string>
#include <cassert>

#define REP(i,N) for (int i=0; i<N; i++) 

using namespace std;


long long T, B, N, M[200000];


int main() {
	cin >> T;
	REP(tc, T) {
		cin >> B >> N;
		REP(i, B) cin >> M[i];
		long long lo = 0, hi = 1LL<<60;
		while (lo < hi) {
			// cout << lo << " " << hi << endl;
			long long mid = lo + (hi - lo) / 2;
			long long count = 0;
			REP(i, B) count += 1 + mid / M[i];
			if (count >= N) hi = mid;
			else lo = mid+1;
		}
		assert(lo == hi);
		// cout << lo << endl;
		long long offset = N-1, ans;
		// cout << offset << endl;
		REP(i, B) offset -= (lo + M[i] - 1) / M[i];
		// cout << lo << " " << offset << endl;
		assert(offset >= 0);
		assert(offset < B);
		REP(i, B) if (lo % M[i] == 0) {
			if (offset == 0) {
				ans = i+1;
				break;
			}
			offset--;
		}
		cout << "Case #" << tc+1 << ": " << ans << endl;
	}
	return 0;
}
