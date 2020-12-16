#include <iostream>
#include "dll.h"
using namespace std;

int square(const int n) {
	int sqr;
	for (int i = 0; i < n; i++) {
		sqr = sqr + n;
	}
	return sqr;
}

int main() {

	List<int> intList;
	list_init(intList);

	/*list_insert_back(intList, 21);
	 list_insert(intList, 20);
	 list_insert_back(intList, 11);
	 list_insert(intList, 19);
	 list_insert_back(intList, 2);
	 list_insert_back(intList, 43);
	 list_insert_back(intList, 21);
	 list_insert(intList, 14);
	 list_insert_back(intList, 19);
	 list_insert_back(intList, 4);
	 list_insert(intList, 31);
	 list_insert(intList, 8);
	 list_insert_back(intList, 9);*/

	for (int i = 0; i < 5; ++i) {
		list_insert(intList, i);
	}

	for (int i = 91; i < 96; ++i) {
		list_insert_back(intList, i);
	}

	//list_print(intList, std::cout);
	//std::cout << std::endl;

	ListIterator<int> iter = list_iter_init(intList);
	while (list_iter_has_next(iter)) {
		int * v = list_iter_next(iter);
		cout << *v << endl;
	}
	while (list_iter_has_prev(iter)) {
		int * v = list_iter_prev(iter);
		cout << *v << endl;
	}

	//list_remove(intList, 1);
	//list_print(intList, std::cout);
	//cout << "\n" << intList.begin->data << "  " << intList.end->data << endl;
	//list_print_inverse(intList, std::cout);
	list_destroy(intList);
	return 0;
}
