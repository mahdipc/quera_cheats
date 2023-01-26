#include <bits/stdc++.h>

using namespace std;

typedef long double LD;
typedef long long int LL;
typedef pair <int,int> pii;

#define L first
#define R second

const int maxn = 1e5 + 100;
int f[maxn], s[maxn];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	int n, q;
	cin >> n >> q;
	for (int i = 1; i <= n; i++)
		cin >> f[i], f[n + 1] ^= f[i];

	for (int i = 1; i <= n + 1; i++)
		s[i] = s[i - 1] ^ f[i];

	while (q--) {
		int idx;
		cin >> idx;
		idx = ((idx - 1) % (n + 1)) + 1;
		cout << s[idx] << '\n';
	}

	return 0;
}