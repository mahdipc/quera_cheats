#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> matrix(n, vector<int>(n, 0));

    int x, y;
    for (int i = 0; i < m; i++) {
        cin >> x >> y;
        matrix[x-1][y-1] = matrix[y-1][x-1] = 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] != 1) {
                matrix[i][j] = 0;
            }
            cout << matrix[i][j];
        }
        cout << endl;
    }

    return 0;
}