#include <bits/stdc++.h>

using namespace std;

const int maxn = 1000;
int a[maxn][maxn];

bool is_two_power(int n)
{
	int m = n, k = 1;
	while (m > 1)
	{
		m /= 2;
		k *= 2;
	}

	return (k == n);
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);

	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> a[i][j];

	int ans = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			vector <int> v;
			for (int x = max(0, i - 1); x <= min(i + 1, n - 1); x++)
				for (int y = max(0, j - 1); y <= min(j + 1, m - 1); y++)
					if (x != i || y != j)
						v.push_back(a[x][y]);

			bool okay = false;
			for (int r = 0; r < (int)v.size(); r++)
				for (int s = r + 1; s < (int)v.size(); s++)
					for (int t = s + 1; t < (int)v.size(); t++)
						if (is_two_power(v[r] + v[s] + v[t]))
							okay = true;
			
			if (okay)
				ans++;
		}

	cout << ans << '\n';
	return 0;
}