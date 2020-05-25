
#include <iostream>
#include <string>

#define REP(i,N) for (int i=0; i<N; i++) 

using namespace std;



struct MaxFlow {
	int n;
	vector<vector<int> > adj;
	map<pair<int, int>, int> flow, cap; 

	MaxFlow(int n) : adj(n), n(n) {}

	void add(int a, int b, int capacity) {
		adj[a].push_back(b);
		cap[make_pair(a, b)] = capacity;
		flow[make_pair(a, b)] = 0;
	}

	void dfs(int source, int sink) {
		if (source == sink) {
			return 0;
		}
		for (int i = 0; i < adj[source].size(); i++) {
			make_pair(source, adj[i]);
		}
	}

	int calc(int source, int sink) {
		while (true) {
			dfs(source, sink);
		}
	}
};


const int MAXN = 999;
bool A[MAXN][MAXN], B[MAXN][MAXN], Y[MAXN], X[MAXN], D1[MAXN], D2[MAXN];

// g1: left node to right node
// g2: right node to left node
// seen: right node seen in dfs
int g1[MAXN], g2[MAXN], seen[MAXN];


bool bipartite_match(int start, int N) {
	REP(i, 2*N-1) if (!seen[i]) {
		int i2 = i - N + 1;
		int y2 = start - i2;
		int x2 = start + i2;
		if (y2 % 2 != 0 || x2 % 2 != 0 || y2 < 0 || y2 >= 2*N || x2 < 0 || x2 >= 2*N) continue;
		seen[i] = true;
		if (g2[i] == -1 || bipartite_match(g2[i], N)) {
			g2[i] = start;
			g1[start] = i;
			return true;
		}
	}
	return false;
}


int main() {
	int T, N;
	string a, b;
	cin >> T;
	REP(tc, T) {
		map<string, int> words1, words2;
		cin >> N;
		REP(i, N) {
			cin >> a >> b;
			if (!words1.count(a)) {
				words1[a]
			}
		}
		cout << "Case #" << tc+1 << ":" << endl;
	}
	return 0;
}
