#include <iostream>
using namespace std;

template <typename Data>
void swap(Data* list, Data * sorted_list, int start, int const& end){
    for(int i = 0; start != end; ++start, ++i)
        list[start] = sorted_list[i];
}

template <typename Data>
void merge(Data* list, int const& start, int const& barrier, int const& end) {
    int left_it = start;
    int right_it =  barrier;

    int l_stop = barrier;
    int r_stop = end;

    Data* sorted_list = new Data[end - start];
    int sort_it = 0;

    while (left_it != l_stop && right_it != r_stop) {
        if (list[left_it] > list[right_it]) {
            sorted_list[sort_it] = list[right_it];
            //cout << *left_it << " ? " << *l_stop << " :: " << *right_it << " ? " << *r_stop << " :: " << *sorted_list << " right_it" << endl;
            ++right_it;
            ++sort_it;
        }
        else
        {
            sorted_list[sort_it] = list[left_it];
            ++left_it;
            ++sort_it;
        }
    }

    while (left_it != l_stop) {
        sorted_list[sort_it] = list[left_it];
        ++left_it;
        ++sort_it;
    }

    while (right_it != r_stop) {
        sorted_list[sort_it] = list[right_it];
        ++right_it;
        ++sort_it;
    }

    swap(list, sorted_list, start, end);
    delete [] sorted_list;

}

template <typename Data>
void sort(Data* list, int const& start, int const& end) {
    if (start < end) {
        int mid = (end + start) / 2;
        sort(list, start, mid);
        sort(list, mid + 1, end);
        merge(list, start, mid, end);
    }
}

int main()
{
    int* array{ new int[8]{ 5, 2, 4, 6, 1, 3, 2, 6} };
    sort(array, 0, 8);

    for (int i = 0; i != 8; ++i)
        cout << array[i] << " ";

    return 0;
}

