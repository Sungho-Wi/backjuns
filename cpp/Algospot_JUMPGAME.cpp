#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int **jump;
int **check;

bool game(int y, int x, int size) {
	if (y > (size - 1) || x > (size - 1))
		return false;
	if (y == (size - 1) && x == (size - 1))
		return true;
	if (check[y][x] <= -1)
		return false;
	if (check[y][x] >= 1)
		return true;
	bool result1 = game(y, (x + jump[y][x]), size);
	bool result2 = game((y + jump[y][x]), x, size);
	if (result1 || result2) {
		check[y][x]++;
		return true;
	}
	check[y][x]--;
	return false;
}

int main() {
	int test;
	scanf("%d", &test);

	for (int i = 0; i < test; ++i) {
		int size;
		scanf("%d", &size);
		jump = new int*[size];
		for (int a = 0; a < size; ++a)
			jump[a] = new int[size];

		check = new int*[size];
		for (int a = 0; a < size; ++a)
			check[a] = new int[size];
		for (int c = 0; c < size; ++c) {
			fill(&check[c][0], &check[c][size], 0);
		}

		for (int j = 0; j < size; ++j) {
			for (int k = 0; k < size; ++k) {
				scanf("%d", &jump[j][k]);
			}
		}

		printf(game(0, 0, size) ? "YES\n" : "NO\n");
	}
}