#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
	int size;
	scanf("%d", &size);

	vector<int> dp;


	dp.push_back(INT32_MIN);
	for (int i = 0; i < size; ++i) {
		int in;
		scanf("%d", &in);
		if (in > dp.back())
			dp.push_back(in);
		else {
			auto it = lower_bound(dp.begin(), dp.end(), in);
			*it = in;
		}
	}
	printf("%d", dp.size() - 1);
}