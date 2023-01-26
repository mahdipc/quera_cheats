#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

const int maxn = 1e5, maxl = 20;
vector <int> adj[maxn];
int h[maxn], par[maxn][maxl];

void dfs(int v)
{
	for (int i = 1; par[v][i - 1] != -1; i++)
		par[v][i] = par[par[v][i - 1]][i - 1];

	for (int u : adj[v])
		if (u != par[v][0])
		{
			par[u][0] = v;
			h[u] = h[v] + 1;
			dfs(u);
		}
}

int lca(int v, int u)
{
	if (h[v] < h[u])
		swap(v, u);

	for (int i = maxl - 1; i >= 0; i--)
		if (par[v][i] != -1 && h[par[v][i]] >= h[u])
			v = par[v][i];

	if (v == u)
		return v;

	for (int i = maxl - 1; i >= 0; i--)
		if (par[v][i] != par[u][i])
			v = par[v][i], u = par[u][i];

	return par[v][0];
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);

	int n, k;
	cin >> n >> k;

	for (int i = 1; i < n; i++)
	{
		int u, v;
		cin >> u >> v;
		u--, v--;
		adj[v].push_back(u);
		adj[u].push_back(v);
	}

	memset(par, -1, sizeof par);
	dfs(0);

	int ans;
	cin >> ans;
	ans--;

	for (int i = 1; i < k; i++)
	{
		int u;
		cin >> u;
		u--;
		ans = lca(ans, u);
	}

	cout << 1 + ans << '\n';
	return 0;
}