#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<unsigned long> get_triangle_numbers(unsigned long max) {
	vector<unsigned long> nums;
	int root = 0;

	for (unsigned long i = 1; i <= max; i++) {
		root = sqrt((8*i) + 1);
		if (root * root == ((8*i) + 1)) { nums.push_back(i); }
	}

	return nums;
}

vector<unsigned long> get_all_factors(unsigned long x, unsigned long max) {
	vector<unsigned long> factors;

	for (unsigned long i = 1; i <= max; i++) {
		if (x % i == 0) { factors.push_back(i); }
	}

	return factors;
}

main() {
	unsigned long max = 240000000;

	//vector<unsigned long> triangles = get_triangle_numbers(max);
	// http://www.shyamsundergupta.com/triangle.htm with highly composite numbers.
 
	vector<unsigned long> factors = get_all_factors(17907120, max);

	int count = 0;

	for (int i = 0; i < factors.size(); i++) {
		cout << factors[i] << endl;
		count++;
	} 

	cout << "Factors: " << count << endl;

/*
	int count = 0;

	for (unsigned long i = 1; i < 10000000000; i++) {
		if (tri % i == 0) { count++; }
	}
	cout << count << endl;
*/
}
