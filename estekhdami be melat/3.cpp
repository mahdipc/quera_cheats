#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n, q;
    cin >> n >> q;
    cin.ignore();
    string s;
    cin >> s;
    for (int i = 0; i < q; i++)
    {
        string queryType;
        cin >> queryType;
        if (queryType == "?")
        {
            string t;
            cin >> t;
            cout << (s.find(t) != string::npos ? "YES" : "NO") << endl;
        }
        else
        {
            int k;
            cin >> k;
            k--;
            s[k] = (s[k] == '0' ? '1' : '0');
        }
    }
    return 0;
}