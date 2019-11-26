#include <iostream>
#include <string>
#include <vector>

using namespace std;

class id {
public:
	int number;
	string name;

	id(int n, string na) { number = n, name = na; }
};

int main() {
	int size;
	cin >> size;
	vector< vector< id > > vec(200);
	for (int i = 0; i < size; ++i) {
		int age;
		string name;
		cin >> age >> name;
		vec[age - 1].push_back(*(new id(i, name)));
	}
	for (int i = 0; i < 200; ++i) {
		if (!vec[i].empty()) {
			for (int j = 0; j < vec[i].size(); ++j) {
				cout << i + 1 << vec[i][j].name << "\n";
			}
		}

	}
}