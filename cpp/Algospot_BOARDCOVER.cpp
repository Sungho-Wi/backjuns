#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int board[4][3][2] = {
	{ { 0,0 },{ 1,0 },{ 0,1 } },
	{ { 0,0 },{ 0,1 },{ 1,1 } },
	{ { 0,0 },{ 1,0 },{ 1,1 } },
	{ { 0,0 },{ 1,0 },{ 1,-1 } }
};

bool set(int b, int y, int x, int hasCover, vector< vector<int> > &vec) { // hasCover 1 : 씌우기 , -1 : 되돌리기
	bool result = true;
	for (int i = 0; i < 3; ++i) {
		int newY = y + board[b][i][0];
		int newX = x + board[b][i][1];
		if (newY < 0 || newY >= vec.size() || newX < 0 || newX >= vec[0].size()) {
			result = false;
		}
		else if ((vec[newY][newX] += hasCover) > 1)
			result = false;
	}
	return result;
}

int cover(vector< vector<int> > &vec) {
	int y = -1, x = -1;
	for (int i = 0; i < vec.size(); ++i) {
		for (int j = 0; j < vec[i].size(); ++j) {
			if (vec[i][j] == 0) {
				y = i; 
				x = j;
				break;
			}
		}
		if (y != -1)
			break;
	}
	if (y == -1) // '.' 을 못찾을경우
		return 1;

	int value = 0;
	for (int b = 0; b < 4; ++b) { // 4가지 경우
		if (set(b, y, x, 1, vec))
			value += cover(vec);
		set(b, y, x, -1, vec);
	}
	return value;

}

int main() {

	int testcase;
	cin >> testcase;

	while (testcase--) {
		int y, x, count = 0;
		cin >> y >> x;
		vector< vector<int> > vec(y, vector<int>());
		for (int i = 0; i < y; ++i) {
			string str;
			cin >> str;
			for (char c : str) {
				if (c == '.') {
					count++;
					vec[i].push_back(0);
				}
				else
					vec[i].push_back(1);
			}
		}
		if (count % 3 != 0) { // 공간이 더 남거나 모자르다면
			cout << "0\n";
			continue;
		}
		cout << cover(vec) << endl;
	}
}