#include <iostream>
#include <cmath>

using namespace std;

main() {
	int nums[1001] = {0};

	for (int i = 1; i <= 1000; i++) {
		nums[i] = i * i;
	}

	for (int i = 0; i < 1001; i++) {
		for (int j = 0; j < 1001; j++) {
			for (int k = 0; k < 1001; k++) {
				if (sqrt(nums[i]) + sqrt(nums[j]) + sqrt(nums[k]) == 1000 && nums[i] + nums[j] == nums[k]) { cout << i << ", " << j << ", " << k << endl; }
			}
		}
	}
}
