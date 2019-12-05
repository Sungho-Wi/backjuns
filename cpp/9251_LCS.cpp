#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
int main() {
	string one, two;
	cin >> one >> two;
	vector< vector<int> > vec(one.length() + 1);
	vec[0] = vector<int>(two.length() + 1, 0);

	for (int i = 1; i < one.length() + 1; ++i) {
		for (int k = 0; k < two.length() + 1; ++k) {
			if (k == 0) {
				vec[i].push_back(0);
				continue;
			}
			if (one[i - 1] == two[k - 1]) {
				vec[i].push_back(vec[i - 1][k - 1] + 1);
			}
			else {
				vec[i].push_back(max(vec[i][k - 1], vec[i - 1][k]));
			}
		}
	}
	int maxValue = 0;
	for (vector<int> v : vec) {
		auto it = max_element(v.begin(), v.end());
			if (maxValue < *it)
				maxValue = *it;
	}
	cout << maxValue;
}