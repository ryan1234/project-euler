#include <iostream>

using namespace std;

int get_collatz(long i) {
	int count = 1;

	while (i > 1) {
		if (i % 2 == 0) { 
			i = i / 2; 
		}
		else { 
			i = 3*i + 1; 
		}

		count++;
	}

	return count;
}

main() {
	int largest = 0;
	int index = 0;

	for (int i = 1; i <= 1000000; i++) {
		int collatz = get_collatz(i);
		if (collatz > largest) { largest = collatz; index = i; }
	}

	cout << "Largest chain: " << largest << " Index: " << index << endl;
}
