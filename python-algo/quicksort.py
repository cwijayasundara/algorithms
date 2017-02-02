def qsort(array):
    if len(array) < 2:
        # if array has 1 element its already sorted
        return array
    else:
        # set the 1st elem as the pivot
        pivot = array[0]
        # sub array for elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # sub array for elements grater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        # return qsort(less) + [pivot] + qsort(greater)
        return qsort(greater) + [pivot] + less

print qsort([23, 13, 345, 2000, 1, 0])

