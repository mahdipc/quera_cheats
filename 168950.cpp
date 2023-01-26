#include<bits/stdc++.h>
using namespace std;

int main() {
    string month;
    cin >> month;
    if (month == "september" || month == "october" || month == "november") {
        cout << "spring";
    } else if (month == "december" || month == "january" || month == "february") {
        cout << "summer";
    } else if (month == "march" || month == "april" || month == "may") {
        cout << "autumn";
    } else if (month == "june" || month == "july" || month == "august") {
        cout << "winter";
    }


}