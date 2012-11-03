/**
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we
 * get 3, 5, 6 and 9. The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */

#include <iostream>

using namespace std;

const int max_number = 1000;

int main(int argc, char* args[])
{
	int multiples[max_number];
	int sum = 0;
	int i = 0;

	for(int x = 0; x < max_number; x++)
	{
		if(x % 3 == 0 || x % 5 == 0)
		{
			multiples[i] = x;
			i++;
			sum += x;
		}
	}

	cout << "Multiples: ";
	for(int x = 0; x < i; x++)
	{
		cout << multiples[x];

		if(x != i - 1)
		{
			cout << ", ";
		}
	}
	cout << endl;
	cout << "Sum: " << sum << endl;

	return 0;
}
