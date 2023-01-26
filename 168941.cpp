#include <bits/stdc++.h>

using namespace std;

typedef long double LD;
typedef long long int LL;
typedef pair <int,int> pii;

#define L first
#define R second

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	LD p, d;
	cin >> p >> d;
	if (d < p) {
		cout << "1.000000\n";
		return 0;
	}
	LD ans = 1; 
	for (int i = 0; i < p; i++)
		ans = (ans * (d - i)) / d;
	cout.precision(6);
	cout << fixed << 1 - ans << endl;

	return 0;
}