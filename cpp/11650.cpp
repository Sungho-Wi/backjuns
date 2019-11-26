#include <cstdio>
#include <vector>
#include <algorithm>

int main() {
	std::vector< std::vector<int> > vec(200001);
	int size;
	scanf("%d", &size);

	while (size--) {
		int a, b;
		scanf("%d %d", &a, &b);
		vec[a + 100000].push_back(b);
	}

	for (int i = 0; i < 200001; i++) {
		if (!(vec[i].empty())) {
			std::sort(vec[i].begin(), vec[i].end());
			for (int j = 0; j < vec[i].size(); j++) {
				printf("%d %d\n", i - 100000, vec[i][j]);
			}
		}
	}
}