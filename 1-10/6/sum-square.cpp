#include <iostream>

using namespace std;

main() {
	int sum = 0;

	for (int i = 1; i <= 100; i++) {
		sum += (i * i);
	}

	int square = 0;

	for (int i = 1; i <= 100; i++) {
		square += i;
	}

	cout << (square * square) - sum << endl;
}
