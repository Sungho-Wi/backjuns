#include <cstdio>
#include <vector>

using namespace std;

int main() {
	int size;
	scanf("%d", &size);

	if (size == 0) {
		printf("0");
		return 0;
	}
	vector<int> k;

	k.push_back(1);
	k.push_back(1);

	for (int i = 2; i <= size; ++i) {
		k.push_back((k[i - 2] + k[i - 1]) % 15746);
	}

	printf("%d", k[size]);

}