
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#define REP(i,N) for (int i=0; i<N; i++) 

using namespace std;


int main() {
	int T;
	long long N;
	string s;
	cin >> T;
	REP(cs, T) {
		cin >> s;
		bool found = false;
		char c;
		REP(i, s.length()-1) {
			if (s[i] > s[i+1]) {
				found = true;
				c = s[i];
				break;
			}
		}
		if (found) {
			bool seen = false;
			REP(i, s.length()) {
				if (seen) {
					s[i] = '0';
				}
				if (s[i] == c) {
					seen = true;
				}
			}
		}
		stringstream(s) >> N;
		if (found) N--;
		cout << "Case #" << cs+1 << ": " << N << endl;
	}
}
