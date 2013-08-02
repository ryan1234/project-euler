#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <unordered_map>

using namespace std;

vector<unsigned long> get_primes(unsigned long max){
    vector<unsigned long> primes;
    char* sieve;
    sieve = new char[max/8+1];
    
    // Fill sieve with 1  
    memset(sieve, 0xFF, (max/8+1) * sizeof(char));
    for(unsigned long x = 2; x <= max; x++)
        if(sieve[x/8] & (0x01 << (x % 8))){
            primes.push_back(x);
            // Is prime. Mark multiplicates.
            for(unsigned long j = 2*x; j <= max; j += x)
                sieve[j/8] &= ~(0x01 << (j % 8));
        }
    delete[] sieve;

    return primes;
}


main() {
	vector<unsigned long> primes = get_primes(1000000);
	unordered_map<unsigned long, int> map;

	for (int i = 0; i < primes.size(); i++) {
		map[primes[i]] = 1;
	}

	int largest = 0;
	int largest_a = 0;
	int largest_b = 0;

	for (int a = -1000; a < 1000; a++) {
		for (int b = -1000; b < 1000; b++) {
			int count = 0;

			for (int n = 0; n < 1000; n++) {
				unsigned long answer = pow(n, 2) + (a * n) + b;
				if (map[answer] == 1) {
					count++;
				}
				else { break; }
			}

			if (count > largest || (a == 1 && b == 41)) {
				cout << "a: " << a << ", b: " << b << ", count: " << count << endl;

				largest = count;
				largest_a = a;
				largest_b = b;
			}
		}
	}
}
