#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
	int size;
	scanf("%d", &size);
	vector<int> vec;
	vector<int> dp1(size);
	vector<int> dp2(size);
	int max = 0;
	for (int i = 0; i < size; ++i) {
		int val;
		scanf("%d", &val);
		vec.push_back(val);
		dp1[i] = 1;
		for (int k = 0; k < i; ++k) {
			if (val > vec[k]) {
				if (dp1[i] < dp1[k] + 1)
					dp1[i] = dp1[k] + 1;
			}
		}
	}

	int maxValue = 0;
	for (int i = size - 1; i >= 0; --i) {
		dp2[i] = 1;
		for (int k = size - 1; k > i; --k) {
			if (vec[k] < vec[i]) {
				if (dp2[i] < dp2[k] + 1)
					dp2[i] = dp2[k] + 1;
			}
		}
		if (maxValue < dp1[i] + dp2[i] - 1)
			maxValue = dp1[i] + dp2[i] - 1;
	}
	printf("%d\n", maxValue);
}