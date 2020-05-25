
#include <iostream>
#include <string>

#define REP(i,N) for (int i=0; i<N; i++) 

using namespace std;


int main() {
	int T;
	string s;
	cin >> T;
	REP(tc, T) {
		cin >> s;
		string ans;
		REP(i, s.length()) ans =(ans + s[i] > s[i] + ans) ? ans + s[i] : s[i] + ans;
		cout << "Case #" << tc+1 << ": " << ans << endl;
	}
	return 0;
}
