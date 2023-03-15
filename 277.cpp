#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    cin >> n;
    int count = 0;
    for (int i = 1; i <= n; i++) {
        string s = to_string(i);
        bool is_binary = true;
        for (int j = 0; j < s.length(); j++) {
            if (s[j] != '0' && s[j] != '1') {
                is_binary = false;
                break;
            }
        }
        if (is_binary) {
            count++;
        }
    }
    cout << count << endl;
    return 0;
}