#include <iostream>
#include <map>

using namespace std;

map <string, string> ans;

string finished(string state)
{
	char a[3][3];
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			a[i][j] = state[i * 3 + j];

	int cnt_x = 0, cnt_o = 0;
	for (int i = 0; i < 3; i++)
	{
		cnt_x = 0, cnt_o = 0;
		for (int j = 0; j < 3; j++)
		{
			if (a[i][j] == 'X') cnt_x++;
			if (a[i][j] == 'O') cnt_o++;
		}
		if (cnt_x == 3) return "X";
		if (cnt_o == 3) return "O";
	}

	for (int j = 0; j < 3; j++)
	{
		cnt_x = 0, cnt_o = 0;
		for (int i = 0; i < 3; i++)
		{
			if (a[i][j] == 'X') cnt_x++;
			if (a[i][j] == 'O') cnt_o++;
		}
		if (cnt_x == 3) return "X";
		if (cnt_o == 3) return "O";
	}

	cnt_x = 0, cnt_o = 0;
	for (int i = 0; i < 3; i++)
	{
		if (a[i][i] == 'X') cnt_x++;
		if (a[i][i] == 'O') cnt_o++;
	}
	if (cnt_x == 3) return "X";
	if (cnt_o == 3) return "O";

	cnt_x = 0, cnt_o = 0;
	for (int i = 0; i < 3; i++)
	{
		if (a[2 - i][i] == 'X') cnt_x++;
		if (a[2 - i][i] == 'O') cnt_o++;
	}
	if (cnt_x == 3) return "X";
	if (cnt_o == 3) return "O";

	int cnt_q = 0;
	for (int i = 0; i < 3; i++)
		for (int j = 0; j < 3; j++)
			if (a[i][j] == '?')
				cnt_q++;

	if (cnt_q == 0)
		return "Draw";
	return "Unfinished";
}

void bt(string state, char turn)
{
	ans[state] = finished(state);
	if (ans[state] != "Unfinished")
		return;

	for (int i = 0; i < 9; i++)
		if (state[i] == '?')
		{
			state[i] = turn;
			bt(state, (turn == 'X' ? 'O' : 'X'));
			state[i] = '?';
		}
}

int main()
{

	bt("?????????", 'X');

	string state = "", s;
	cin >> s; state += s;
	cin >> s; state += s;
	cin >> s; state += s;

	if (ans.find(state) == ans.end())
		cout << "Invalid\n";
	else
		cout << ans[state] << '\n';

	return 0;
}