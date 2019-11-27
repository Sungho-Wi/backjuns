#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int *num;

void ultari(int left, int right, vector<int> *result) {
	if (left >= right) {
		result->push_back(num[right]);
		return;
	}
	int mid = (left + right) / 2;
	ultari(left, mid, result);
	ultari(mid + 1, left, result);

	int back = mid;
	int forward = mid + 1;

	int boardSize = min(num[back], num[forward]);
	int count = 1;
	int maxValue = 0;
	while (left <= back && forward <= right) {
		if (num[back] > num[forward]) {
			boardSize = min(boardSize, num[back--]);
			int currValue = boardSize * count++;
			maxValue = max(currValue, maxValue);
		}
		else {
			boardSize = min(boardSize, num[forward++]);
			int currValue = boardSize * count++;
			maxValue = max(currValue, maxValue);
		}
	}

	if (left <= back) {
		while (left <= back) {
			boardSize = min(boardSize, num[back--]);
			int currValue = boardSize * count++;
			maxValue = max(currValue, maxValue);
		}
	}
	else {
		while (forward <= right) {
			boardSize = min(boardSize, num[forward++]);
			int currValue = boardSize * count++;
			maxValue = max(currValue, maxValue);
		}
	}
	result->push_back(maxValue);

}


int main() {
	int size;
	scanf("%d", &size);

	while (size--) {
		int board;
		scanf("%d", &board);

		num = new int[board];
		vector<int> result;
		for (int i = 0; i < board; ++i) {
			scanf("%d", &num[i]);
		}

		ultari(0, board - 1, &result);

		printf("%d\n", *(max_element(result.begin(), result.end())));

	}
}