#include <bits/stdc++.h>

using namespace std;

typedef long long int LL;
typedef pair <LL, LL> point;

#define X first
#define Y second

const int maxn = 100;
LL t[maxn], s[maxn], f[maxn];

LL cross(point A, point B)
{
	return A.X * B.Y - A.Y * B.X;
}

point mnus(point A, point B)
{
	return make_pair(A.X - B.X, A.Y - B.Y);
}

bool intersect(point A_1, point B_1, point A_2, point B_2)
{
	LL c_1 = cross(mnus(B_1, A_1), mnus(B_2, A_1));
	LL c_2 = cross(mnus(B_1, A_1), mnus(A_2, A_1));

	if ((c_1 > 0 && c_2 > 0) || (c_1 < 0 && c_2 < 0))
		return false;

	LL c_3 = cross(mnus(B_2, A_2), mnus(B_1, A_2));
	LL c_4 = cross(mnus(B_2, A_2), mnus(A_1, A_2));

	if ((c_3 > 0 && c_4 > 0) || (c_3 < 0 && c_4 < 0))
		return false;

	return true;
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> t[i] >> s[i] >> f[i];

	for (int i = 0; i < n; i++)
	{

		point A_1 = make_pair(t[i], s[i]);
		point B_1 = make_pair(t[i] + abs(f[i] - s[i]), f[i]);


		int r = 0;
		for (int j = 0; j < n; j++)
			if (j != i)
			{
				point A_2 = make_pair(t[j], s[j]);
				point B_2 = make_pair(t[j] + abs(f[j] - s[j]), f[j]);

				if (intersect(A_1, B_1, A_2, B_2))
					r++;
			}

		cout << r << " \n"[i == n - 1];
	}

	return 0;
}