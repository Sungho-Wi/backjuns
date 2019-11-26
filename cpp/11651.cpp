#include <cstdio>
#include <vector>
#include <algorithm>

int main() {
	std::vector< std::vector<int> > vec(200001);
	int size;
	scanf("%d", &size);

	while (size--) {
		int y, x;
		scanf("%d %d", &x, &y);
		vec[y + 100000].push_back(x);
	}

	for (int i = 0; i < 200001; i++) {
		if (!(vec[i].empty())) {
			std::sort(vec[i].begin(), vec[i].end());
			for (int j = 0; j < vec[i].size(); j++) {
				printf("%d %d\n", vec[i][j], i - 100000);
			}
		}
	}
}