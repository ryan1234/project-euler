#include <iostream>

using namespace std;

main() {
	int i = 1;
	int num = 0;

	while (num == 0) {
		int j = 1;

		while (j <= 20) {
			if (i % j != 0) { break; }
			if (j == 20) { num = i; }
			j++;
		}
		i++;	
	}

	cout << num << endl;
}
