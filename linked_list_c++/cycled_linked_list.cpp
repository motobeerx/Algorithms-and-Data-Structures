#include <iostream>
#include "/home/anton/eclipse_workspace/chap_four/src/dll.h"
using namespace std;


int main() {


	List<int> linked_list;
	list_init(linked_list);

	int data[26] = {1, 2, 3, 4, 5, 12, 32, 43, 23, 85, 1, 23, 119, 34, 62, 123, 43, 54, 86, 43, 44, 45, 92, 75, 10, 19 };
	for (int i = 0; i < 26; ++i)  list_insert(linked_list, data[i]);
	list_print(linked_list, cout);
	cout<<endl;


	hare_turtle(linked_list, cout);
	make_cycle(linked_list, 5);
	hare_turtle(linked_list, cout);


	return 0;
}
