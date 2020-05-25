
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

#define REP(i,N) for (int i=0; i<N; i++) 

using namespace std;


int main() {
	long long T, a, b;
	long long K, N;
	cin >> T;
	REP(cs, T) {
		cin >> N >> K;
		long long x=1;
		while (x <= K) {
			x *= 2;
		}
		long long spaces = max(0LL, N-x+1);
		a = b = spaces / x;
		if (K - x/2 < spaces%x) a++;
		if (K < spaces%x) b++;
 		cout << "Case #" << cs+1 << ": " << a << " " << b << endl;
	}
}
