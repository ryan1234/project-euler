#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<unsigned long> get_all_factors(unsigned long x) {
        vector<unsigned long> factors;

        for (unsigned long i = 1; i <= x; i++) {
                if (x % i == 0 && i != x) { factors.push_back(i); }
        }

        return factors;
}

vector<int> get_abundant_numbers() {
	vector<int> abundant;

        for (int i = 1; i < 28123; i++) {
                vector<unsigned long> factors = get_all_factors(i);

                int sum = 0;

                for (int j = 0; j < factors.size(); j++) {
                        sum += factors[j];
                }

                if (sum > i) { abundant.push_back(i); }
        }

	return abundant;
}

main() {
	vector<int> abundant = get_abundant_numbers();

	for (int i = 0; i < abundant.size(); i++) {
		cout << abundant[i] << endl;
	}

	return 0;
}
