
#include <iostream>
#include <string>

#define REP(i,N) for (int i=0; i<N; i++) 

using namespace std;


const int MAXN = 3000;
int A[MAXN];


int main() {
	int T, n, x;
	string s;
	cin >> T;
	REP(tc, T) {
		cin >> n;
		REP(i, MAXN) A[i] = 0;
		REP(i, n * (2*n-1)) {
			cin >> x;
			A[x]++;
		}
		cout << "Case #" << tc+1 << ":";
		REP(i, MAXN) if (A[i] % 2 == 1) cout << " " << i;
		cout << endl;
	}
	return 0;
}
