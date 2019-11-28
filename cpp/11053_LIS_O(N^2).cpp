#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
	int size;
	scanf("%d", &size);

	vector<int> val;
	vector<int> dp(size);

	for (int i = 0; i < size; ++i) {
		int num;
		scanf("%d", &num);
		val.push_back(num);
	}

	for (int i = 0; i < size; ++i) {
		dp[i] = 1;
		for (int j = 0; j < i; ++j) {
			if (val[i] > val[j]) {
				if (dp[i] < dp[j] + 1)
					dp[i] = dp[j] + 1;
			}
		}
	}
	printf("%d", *max_element(dp.begin(), dp.end()));
}