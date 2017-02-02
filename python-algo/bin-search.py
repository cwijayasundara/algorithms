
def bin_search(list, item):

    low = 0
    high = len(list) - 1

    while low <= high:
        middle = (low + high) / 2
        # say we guess the item is the middle one
        guess = list[middle]

        if guess == item:
            return middle

        if guess > item:
            high = middle - 1

        else:
            low = middle + 1

    # Item doesn't exist
    return None

my_list = [2,4,6,8,10,12]

print bin_search(my_list, 4) # => 1

print bin_search(my_list, 5) # => None