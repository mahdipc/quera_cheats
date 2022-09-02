#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    vector<int> data;
    cin >> n;
    int x;
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        data.push_back(x);
    }
    long long int place = n - 1;
    long long int result = 0;
    long long int index = -1;
    long long int maxi = 0;
    while (place > 0)
    {
        int x;
        index = -1;
        for (int i = place - 1; i >= 0; i--)
        {
            if (data[place] <= data[i])
            {
                index = i;
                break;
            }
        }
        if (index != -1)
        {
            long long int badsum = 0;
            for (int i = index + 1; i < place; i++)
            {
                badsum += data[i];
            }
            result += (place - index - 1) * data[place] - badsum;
            place = index;
        }
        else
        {
            maxi = 0;
            for (int i = 0; i < place; i++)
            {
                if (data[i] >= maxi)
                {
                    maxi = data[i];
                    index = i;
                }
            }

            long long int badsum = 0;
            for (int i = index + 1; i < place; i++)
            {
                badsum += data[i];
            }
            result += (place - index - 1) * data[index] - badsum;
            place = index;
        }
    }
    cout << result << endl;
    return 0;
}