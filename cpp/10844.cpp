#include <cstdio>
#include <vector>

using namespace std;
int main() {
	int size;
	scanf("%d", &size);

	vector< vector<int> > vec(size, vector<int>(10));

	for (int i = 0; i < 10; ++i) {
		vec[0][i] = 1;
	}
	for (int i = 1; i < size; ++i) {
		for (int k = 0; k < 10; ++k) {
			if (k == 0)
				vec[i][0] = vec[i - 1][1] % 1000000000;
			else if(k == 9)
				vec[i][9] = vec[i - 1][8] % 1000000000;
			else 
				vec[i][k] = (vec[i - 1][k - 1] + vec[i - 1][k + 1]) % 1000000000;
		}
	}
	int sum = 0;
	for (int i = 1; i < 10; ++i) {
		sum = (sum +vec[size - 1][i]) % 1000000000;
	}
	printf("%d", sum%1000000000);
}