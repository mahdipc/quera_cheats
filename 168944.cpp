#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

map <string, long long int> score, goal_dif, goal_sco, goal_awa;
vector <string> names;

long long int to_number(string s)
{
	long long int result = 0;
	for (int i = 0; i < (int)s.size(); i++)
		result = result * 10 + s[i] - '0';
	return result;
}

string strip(string s)
{
	reverse(s.begin(), s.end());
	while (s.back() == ' ')
		s.pop_back();

	reverse(s.begin(), s.end());
	while (s.back() == ' ')
		s.pop_back();

	return s;
}

bool cmp(string teamA, string teamB)
{
	if (score[teamA] != score[teamB])
		return (score[teamA] > score[teamB]);

	if (goal_dif[teamA] != goal_dif[teamB])
		return (goal_dif[teamA] > goal_dif[teamB]);

	if (goal_sco[teamA] != goal_sco[teamB])
		return (goal_sco[teamA] > goal_sco[teamB]);

	return goal_awa[teamA] > goal_awa[teamB];
}


vector <string> parse(string s)
{
	s = strip(s);
	int mid = -1;
	for (int i = 0; i < (int)s.size(); i++)
		if (s[i] == '.')
		{
			mid = i;
			break;
		}

	string fi = "";
	for (int i = 0; i < mid - 2; i++)
		fi += s[i];
	fi = strip(fi);

	string se = "";
	for (int i = mid + 1; i < (int)s.size(); i++)
		se += s[i];
	se = strip(se);

	string fi_number = "";
	for (int i = (int)fi.size() - 1; i >= 0; i--)
		if (fi[i] == ' ')
			break;
		else
			fi_number += fi[i];
	reverse(fi_number.begin(), fi_number.end());
	fi_number = strip(fi_number);

	string fi_name = "";
	for (int i = 0; i < (int)fi.size() - (int)fi_number.size(); i++)
		fi_name += fi[i];
	fi_name = strip(fi_name);

	string se_number = "";
	for (int i = 0; i < (int)se.size(); i++)
		if (se[i] == ' ')
			break;
		else
			se_number += se[i];
	se_number = strip(se_number);

	string se_name = "";
	for (int i = (int)se_number.size() + 1; i < (int)se.size(); i++)
		se_name += se[i];
	se_name = strip(se_name);

	vector <string> result;
	result.push_back(fi_name);
	result.push_back(fi_number);
	result.push_back(se_name);
	result.push_back(se_number);
	return result;
}

int main()
{
	for (int i = 0; i < 12; i++)
	{
		string s;
		getline(cin, s);

		vector <string> v = parse(s);

		string HomeTeamName = v[0];
		long long int HomeTeamGoals = to_number(v[1]);

		string AwayTeamName = v[2];
		long long int AwayTeamGoals = to_number(v[3]);
		
		names.push_back(HomeTeamName);
		names.push_back(AwayTeamName);

		goal_dif[HomeTeamName] += HomeTeamGoals - AwayTeamGoals;
		goal_dif[AwayTeamName] += AwayTeamGoals - HomeTeamGoals;

		goal_sco[HomeTeamName] += HomeTeamGoals;
		goal_sco[AwayTeamName] += AwayTeamGoals;

		goal_awa[AwayTeamName] += AwayTeamGoals;

		if (HomeTeamGoals > AwayTeamGoals)
			score[HomeTeamName] += 3;
		else if (HomeTeamGoals < AwayTeamGoals)
			score[AwayTeamName] += 3;
		else
			score[HomeTeamName] += 1, score[AwayTeamName] += 1;
	}

	sort(names.begin(), names.end());
	names.resize(unique(names.begin(), names.end()) - names.begin());

	sort(names.begin(), names.end(), cmp);

	cout << names[0] << '\n' << names[1] << '\n';

	return 0;
}