#include <cstdio>

int *afterSort;

void sort(int *before, int first, int mid, int last) {
	int k = first;
	int i = first;
	int j = mid + 1;
	while (i <= mid && j <= last) {
		if (before[i] < before[j]) {
			afterSort[k++] = before[i++];
		}
		else {
			afterSort[k++] = before[j++];
		}
	}

	if (i <= mid) {
		for(;k <= last;)
			afterSort[k++] = before[i++];
	}
	else {
		for (;k <= last;)
			afterSort[k++] = before[j++];
	}

	for (int a = first; a <= last; a++) {
		before[a] = afterSort[a];
	}
}

void merge(int *before, int first, int last) {
	if (first < last) {
		int mid = (first + last) / 2;
		merge(before, first, mid);
		merge(before, mid + 1, last);
		sort(before, first, mid, last);
	}
}

int main() {
	int size;
	scanf("%d", &size);

	int *beforeSort = new int[size];
	afterSort = new int[size];
	for (int i = 0; i < size; ++i) {
		scanf("%d", beforeSort + i);
	}

	if (size == 1) {
		printf("%d", beforeSort[0]);
		return 0;
	}
	merge(beforeSort, 0, size - 1);

	for (int i = 0; i < size; ++i) {
		printf("%d\n", *(afterSort + i));
	}

}