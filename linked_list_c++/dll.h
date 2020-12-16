#ifndef DLL_H_
#define DLL_H_
#include <ostream>
using namespace std;

#define nullptr     NULL

template<typename DataType>
struct tNode {
	DataType data;
	tNode* next;
	tNode* prev;
};

template<typename DataType>
struct List {
	tNode<DataType> *begin;
	tNode<DataType> *end;
	int size;
};

template<typename DataType>
void list_init(List<DataType> &lst) {
	lst.begin = nullptr;
	lst.end = nullptr;
	lst.size = 0;
}

//Iterator
template<typename DataType>
struct ListIterator {
	tNode<DataType> * current;
};

template<typename DataType>
ListIterator<DataType> list_iter_init(List<DataType> &l) {
	ListIterator<DataType> it;
	it.current = l.begin;
	return it;
}

template<typename DataType>
bool list_iter_has_next(ListIterator<DataType> &it) {
	return it.current->next != nullptr;
}

template<typename DataType>
bool list_iter_has_prev(ListIterator<DataType> &it) {
	return it.current->prev != nullptr;
}

template<typename DataType>
DataType * list_iter_next(ListIterator<DataType> & it) {
	if (it.current) {
		DataType * ptr = &(it.current->data);
		it.current = it.current->next;
		return ptr;
	}
	return nullptr;
}

template<typename DataType>
DataType * list_iter_prev(ListIterator<DataType> & it) {
	if (it.current) {
		DataType * ptr = &(it.current->data);
		it.current = it.current->prev;
		return ptr;
	}
	return nullptr;
}
///////////////////////////////////////
template<typename DataType>
tNode<DataType> * insert_node(tNode<DataType> *p_begin, List<DataType> &lst,
		DataType data) {
	tNode<DataType> *p = new tNode<DataType>;
	p->data = data;
	p->next = p_begin;
	if (lst.size > 1)
		lst.begin->prev = p;
	return p;
}

template<typename DataType>
void list_insert(List<DataType> &lst, const DataType &value) {
	lst.size += 1;
	lst.begin = insert_node(lst.begin, lst, value);
	if (lst.size == 1) {
		lst.end = lst.begin;
	}
}

template<typename DataType>
tNode<DataType> * insert_node_back(tNode<DataType> *p_end, List<DataType> &lst,
		DataType data) {
	tNode<DataType> *p = new tNode<DataType>;
	p->data = data;
	p->prev = p_end;
	if (lst.size > 1)
		lst.end->next = p;
	return p;
}

template<typename DataType>
void list_insert_back(List<DataType> &lst, const DataType &value) {
	lst.size += 1;
	lst.end = insert_node_back(lst.end, lst, value);
	if (lst.size == 1) {
		lst.begin = lst.end;
	}
}

template<typename DataType>
bool list_remove(List<DataType> & lst, int i) {
	if (i > 0 && i <= lst.size) {
		tNode<DataType> *p_i = lst.begin;
		if (i == 1) {
			lst.begin->next->prev = nullptr;
			lst.begin = lst.begin->next;
			delete p_i;
		} else if (i == lst.size) {
			p_i = lst.end;
			lst.end->prev->next = nullptr;
			lst.end = lst.end->prev;
			delete p_i;
		} else {
			for (int k = 1; k < i; k++)
				p_i = p_i->next;
			p_i->prev->next = p_i->next;
			p_i->next->prev = p_i->prev;
			delete p_i;
		}
		lst.size--;
		return true;
	} else {
		return false;
	}
}

template<typename DataType>
void list_print(const List<DataType> &lst, std::ostream &out) {
	tNode<DataType> *p = lst.begin;
	for (; p; p = p->next) {
		out << p->data << " ";
	}
}

template<typename DataType>
void list_print_inverse(List<DataType> & lst, std::ostream &out) {
	tNode<DataType> *p = lst.end;
	for (; p; p = p->prev) {
		out << p->data << " ";
	}
}

template<typename DataType>
void list_destroy(List<DataType> &lst) {
	tNode<DataType> *p = lst.begin;
	tNode<DataType> *prev;
	while (p) {
		prev = p;
		p = p->next;
		delete prev;
	}
	lst.size = 0;
	lst.begin = nullptr;
	lst.end = nullptr;
}


template<typename DataType>
void make_cycle(List<DataType> &lst, int cycle_start){
	if(lst.size <= cycle_start) return;
	tNode<DataType> *p_begin_cycle = lst.begin;
	for (int i = 1;i < cycle_start; p_begin_cycle = p_begin_cycle->next, i++){}
	lst.end->next = p_begin_cycle;
}


//Проверяем лист на циклы: Повторная трассировка
// Функция возвращает позицию с которой начинается цикл, если цикла нет - -1
template<typename DataType>
int retrace(List<DataType> &lst){
	tNode<DataType> *tracer = lst.begin;

	for (; tracer; tracer = tracer->next){
		tNode<DataType> *follower = lst.begin;
		for (int i = 1; follower != tracer; follower = follower->next, i++){
			if(follower->next == tracer->next){
				return ++i;
			}
		}
	}

	return -1;
}

// Проверяем лист на циклы: Повторная трассировка
// Функция возвращает true, если цикл есть и false, если цикла нет


template<typename DataType>
tNode<DataType>* reverse(tNode<DataType> * begin){
	tNode<DataType> *current = begin;
	tNode<DataType> *previous = nullptr;

	while (current) {
		tNode<DataType> *next = current->next;
		current->next = previous;

		previous = current;
		current = next;
		}

	return previous;
}


template<typename DataType>
bool is_cycle(List<DataType> &lst){
	if(lst.begin == nullptr || lst.size == 0) return false;

	tNode<DataType> *sentinel = lst.begin;
	tNode<DataType> *new_sentinel = reverse(lst.begin);
	reverse(new_sentinel);

	if(new_sentinel == sentinel) return true;
	return false;

}


template<typename DataType>
void hare_turtle(List<DataType> &lst, std::ostream &out){
	tNode<DataType> *hare = lst.begin;
	tNode<DataType> *turtle = lst.begin;
	while(hare){
		hare = hare->next->next;
		turtle = turtle->next;

		if(hare == turtle){

			hare = lst.begin;
			while(hare != turtle){
				hare = hare->next;
				turtle = turtle->next;
			}
			out<<"Cycle begins from cell: "<<hare->data<<endl;
			return;
		}
	}

	out<<"There is no cycle"<<endl;

}

#endif /* DLL_H_ */
