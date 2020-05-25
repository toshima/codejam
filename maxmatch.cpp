
struct MaxMatch {
	int n;
	vector<vector<int> > adj;
	vector<int> p; // right node to left node
	vector<bool> seen;

	MaxMatch(int n, int m): n(n), adj(n), p(m,-1), seen(n) {}

	void add(int a, int b) {
		adj[a].push_back(b);
	}

	bool dfs(int a) {
		if (seen[a]) {
			return false;
		}
		seen[a] = true;
		for (int i = 0; i < adj[a].size(); i++) {
			int b = adj[a][i];
			if (p[b] == -1 || dfs(p[b])) {
				p[b] = a;
				return true;
			}
		}
		return false;
	}

	int solve() {
		int ans = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				seen[j] = false;
			}
			if (dfs(i)) {
				ans++;
			}
		}
		return ans;
	}
};
