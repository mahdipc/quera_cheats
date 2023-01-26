#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1010;
const long double EPS = 1e-6;

#define X first
#define Y second
#define R second

typedef pair<long double, long double> Point;

int n, ans, e, v, sum, comps;
long double x[MAXN], r[MAXN];
map<Point, int> mp;
set<Point> st, st2;
vector<Point> circles;
bool mark[MAXN];
vector<int> adj[MAXN];

bool equals(long double a, long double b) {
	return fabs(a - b) < EPS;
}

bool equals(const Point& a, const Point& b) {
	return equals(a.first, b.first) && equals(a.second, b.second);
}

void insertToSet(const Point& p) {
	Point p2 = Point(p.first - EPS, p.second - EPS);
	auto q = st.lower_bound(p2);
	if (q == st.end() || !equals(p, *q)) {
		st.insert(p);
		mp[p]++;
	} else if (q != st.end() && equals(p, *q)) {
		mp[*q]++;
	}
}

void insertToSet2(const Point& p) {
	Point p2 = Point(p.first - EPS, p.second - EPS);
	auto q = st2.lower_bound(p2);
	if (q == st2.end() || !equals(p, *q)) {
		st2.insert(p);
	}
}

void dfs(int v) {
	mark[v] = true;
	for (auto u: adj[v])
		if (!mark[u])
			dfs(u);
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x, r;
		cin >> x >> r;
		circles.push_back(Point(x, r));
	}
	sort(circles.begin(), circles.end());
	circles.erase(unique(circles.begin(), circles.end()), circles.end());
	n = circles.size();
	for (int i = 0; i < n; i++) {
		st2.clear();
		insertToSet2(Point(circles[i].X - circles[i].R, 0));
		insertToSet2(Point(circles[i].X + circles[i].R, 0));
		for (int j = 0; j < n; j++) {
			if (i == j)
				continue;
			long double d = fabs(circles[i].X - circles[j].X);
			long double rSum = circles[i].R + circles[j].R;
			long double rDif = fabs(circles[i].R - circles[j].R);
			if (d + EPS < rSum && d - EPS > rDif) {
				long double r1 = circles[i].R;
				long double r2 = circles[j].R;
				long double x1 = circles[i].X;
				long double x2 = circles[j].X;
				long double pointX = (r1 * r1 - r2 * r2 - x1 * x1 + x2 * x2) / (2 * (x2 - x1));
				long double tmp = r1 * r1 - (pointX - x1) * (pointX - x1);
				long double pointY = sqrt(tmp);
				insertToSet2(Point(pointX, -pointY));
				insertToSet2(Point(pointX, +pointY));
				adj[i].push_back(j);
			}
			else if (equals(d, rSum) || equals(d, rDif)) {
				adj[i].push_back(j);
			}
		}
		Point last = Point(-1e18, -1e18);
		for (auto p: st2) {
			if (!equals(p, last))
				insertToSet(p);
			last = p;
		}
	}
	sum = 0;
	for (auto p: st) {
		sum += 2 * mp[p];
	}

	v = 0;
	Point last = Point(-1e18, -1e18);

	for (auto p: st) {
		if (!equals(p, last)) {
			// cout << p.X << " " << p.Y << endl;
			v++;
		}
		last = p;
	}

	e = sum / 2;
	for (int i = 0; i < n; i++) {
		if (!mark[i]) {
			comps++;
			dfs(i);
		}
	}
	// cout << e << " " << v << " " << comps << endl;
	ans = e - v + 1 + comps;
	cout << ans << endl;
	return 0;
}