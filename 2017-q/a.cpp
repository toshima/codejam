
#include <iostream>
#include <string>
#include <vector>

#define REP(i,N) for (int i=0; i<N; i++) 

using namespace std;


int main() {
	int T, K;
	string s;
	cin >> T;
	REP(cs, T) {
		cin >> s >> K;
		int ans = 0;
		REP(i, s.length()) {
			if (i + K > s.length() && s[i] == '-') {
				ans = -1;
			} else if (s[i] == '-') {
				ans++;
				REP(j, K) {
					s[i+j] = (s[i+j] == '+') ? '-' : '+';
				}
			}
		}
		cout << "Case #" << cs+1 << ": ";
		if (ans == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << ans;
		}
		cout << endl;
	}
}
