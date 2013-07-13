#include <iostream>

using namespace std;

main() {
	int sum = 2;
	int previous1 = 1;
	int previous2 = 2;

	while (previous2 < 4000000) {
		int temp = previous2;
		previous2 += previous1;
		previous1 = temp;

		//cout << previous2 << endl;
		if (previous2 % 2 == 0) { sum += previous2; }
	}

	cout << sum << endl;
}
