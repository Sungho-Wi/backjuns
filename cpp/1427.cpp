#include <cstdio>
#include <vector>

int main() {
	std::vector<int> vec;
	while (1) {
		char insert = getchar();
		if (insert == '\n')
			break;
		vec.push_back(insert - '0');
	}

	for (int i = 0; i < vec.size(); i++) {
		int min = i;
		for (int j = i+1; j < vec.size(); j++) {
			if (vec[j] > vec[min])
				min = j;
		}
		int temp = vec[i];
		vec[i] = vec[min];
		vec[min] = temp;
	}

	for (int i = 0; i < vec.size(); i++)
		printf("%d", vec[i]);

}