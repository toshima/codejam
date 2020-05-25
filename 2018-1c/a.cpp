#include <cstring>
#include <iostream>
#include <vector>

#define REP(i,N) for (int i = 0; i < (int)N; i++)

using namespace std;


const int INF = 1<<20;


int count(vector<string> words, string prefix) {
    int n = 0;
    REP(i, words.size()) if (words[i].find(prefix) == 0) n++;
    return n;
}

string solve(vector<string> words) {
    string prefix = "";
    REP(j, words[0].size()) {
        string np;
        int best = INF;
        REP(i, words.size()) {
            int n = count(words, prefix + words[i][j]);
            if (n < best) {
                np = prefix + words[i][j];
                best = n;
            }
        }
        prefix = np;
        // cout << prefix << endl;
    }
    REP(i, words.size()) if (words[i] == prefix) return "-";
    return prefix;
}

int main() {
    int T, N, L;
    cin >> T;
    REP(cs, T) {
        cin >> N >> L;
        vector<string> words;
        REP(i, N) {
            string s;
            cin >> s;
            words.push_back(s);
        }
        cout << "Case #" << cs+1 << ": " << solve(words) << endl;        
    }
    return 0;
}
