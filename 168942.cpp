#include <bits/stdc++.h>

using namespace std;

const int maxn = 2000;
int a[maxn];

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];

	int ans = 0;
	for (int i = 0; i < n; i++)
	{
		int min_idx = i;
		for (int j = i + 1; j < n; j++)
			if (a[min_idx] > a[j])
				min_idx = j;

		ans += min_idx - i;

		for (int j = min_idx - 1; j >= i; j--)
			swap(a[j], a[j + 1]);
	}

	cout << ans << '\n';

	return 0;
}