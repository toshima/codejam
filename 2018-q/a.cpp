#include <cstring>
#include <iostream>

#define REP(i,N) for (int i = 0; i < N; i++)

using namespace std;


int calc_damage(string s) {
    int n = s.size(), strength = 1, damage = 0;
    REP(i, n) {
        if (s[i] == 'C') {
            strength <<= 1;
        } else {
            damage += strength;
        }
    }
    return damage;
}


int solve(int d, string s) {
    int hacks = 0;
    while (1) {
        if (calc_damage(s) <= d) {
            return hacks;
        }
        size_t pos = s.rfind("CS");
        if (pos == string::npos) {
            return -1;
        }
        char tmp = s[pos];
        s[pos] = s[pos+1];
        s[pos+1] = tmp;
        hacks++;
    }
}


int main() {
    int num_cases;
    cin >> num_cases;
    REP(cs, num_cases) {
        int d;
        string s;
        cin >> d >> s;
        int ans = solve(d, s);
        if (ans >= 0) {
            cout << "Case #" << cs+1 << ": " << ans << endl;
        } else {
            cout << "Case #" << cs+1 << ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
