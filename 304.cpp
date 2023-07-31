#include <iostream>
#include <iomanip> // For std::setprecision

using namespace std;

long double myPow(long double base, unsigned int exp) {
    if (exp == 0) {
        return 1.0;
    } else if (exp % 2 == 0) {
        long double temp = myPow(base, exp / 2);
        return temp * temp;
    } else {
        long double temp = myPow(base, (exp - 1) / 2);
        return base * temp * temp;
    }
}

int main() {
    long double base;
    unsigned int exp;
    cin >> base >> exp;
    
    long double result = myPow(base, exp);
    cout << fixed << setprecision(3) << result << endl;
    
    return 0;
}