#include <bits/stdc++.h>

using namespace std;

const int MAXN = 5010;
const int MAXPRICE = 5010;

int n, m, totalPrice;
vector<long long> albums[MAXN];

long long dp[MAXN][MAXPRICE], albumPrice[MAXN];

int main() {
	cin >> n >> m >> totalPrice;
	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		albums[x].push_back(y);
	}
	for (int i = 1; i <= m; i++)
		cin >> albumPrice[i];
	int idx = 0;
	for (int i = 1; i <= m; i++) {
		for (auto song: albums[i]) {
			idx++;
			for (int price = 0; price <= totalPrice; price++) {
				dp[idx][price] = max(dp[idx - 1][price], (price >= song) ? dp[idx - 1][price - song] + 1 : 0);
			}
		}
		idx++;
		for (int price = 0; price <= totalPrice; price++) {
			dp[idx][price] = max(dp[idx - 1][price], (price >= albumPrice[i]) ? dp[idx - (int)albums[i].size() - 1][price - albumPrice[i]] + (int)albums[i].size() : 0);
		}
	}
	cout << dp[idx][totalPrice] << endl;
	return 0;
}