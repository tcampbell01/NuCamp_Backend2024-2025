my_list = [5, 4, 1, 2, 3]


def sort_part(the_list, low_index, pivot_index):
    pivot_val = the_list[pivot_index]

    while pivot_index != low_index:
        low_val = the_list[low_index]

        print(the_list, low_val, pivot_val)
        if low_val <= pivot_val:
            low_index += 1

        else:
            the_list[low_index] = the_list[pivot_index-1]
            the_list[pivot_index] = low_val
            the_list[pivot_index-1] = pivot_val
            pivot_index -= 1

    return pivot_index


def quicksort(the_list, low_index, high_index):
    if low_index > high_index:
        return
    pivot_index = sort_part(the_list, low_index, high_index)
    quicksort(the_list, low_index, pivot_index-1)
    quicksort(the_list, pivot_index+1, high_index)


quicksort(my_list, 0, len(my_list)-1)
print(my_list)
