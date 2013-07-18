#include <iostream>
#include <vector>

using namespace std;

vector<unsigned long> get_all_factors(unsigned long x, unsigned long max) {
	vector<unsigned long> factors;

	for (unsigned long i = 1; i <= max; i++) {
		if (x % i == 0 && x != i) { factors.push_back(i); }
	}

	return factors;
}

main() {
	vector<int> nums;

	for (int i = 0; i < 10000; i++) {
		vector<unsigned long> factors = get_all_factors(i, 10000);
		
		int sum = 0;

		for (int j = 0; j < factors.size(); j++) {
			sum += factors[j];
		}

		nums.push_back(sum);
	}

	int counted = 0;

	for (int i = 0; i < 10000; i++) {
		if (nums[i] < 10000) {
			int num1 = nums[i]; // 284
			int num2 = nums[num1]; // 220
			if (i == num2 && i != nums[i]) {
				cout << ", " << nums[i] << ", " << nums[nums[i]] << endl;
				counted++;
			}
		}
	}

	cout << nums[496] << endl;
	cout << "Total 1: " << counted << ", total 2: " << counted / 2 << endl;
}
