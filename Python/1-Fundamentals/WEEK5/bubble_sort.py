# considered brute force

unsorted_list = [101, 49, 3, 12, 56]


def bubblesort(the_list):
    high_index = len(the_list) - 1

    # default is starting at 0, incrementing at 1
    for i in range(high_index):
        list_changed = False
        for j in range(high_index):
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_changed = True
            print(the_list, i, j)
        print(list_changed)

        if list_changed == False:
            break


bubblesort(unsorted_list)
