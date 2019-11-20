#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	
	int size;
	cin >> size;
	vector<int> vec;
	while (size--) {
		int value;
		cin >> value;
		vec.push_back(value);
	}
	sort(vec.begin(), vec.end());

	for (int i = 0; i < vec.size(); ++i)
		cout << vec[i] << endl;
}