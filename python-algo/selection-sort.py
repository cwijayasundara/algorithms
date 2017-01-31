# finds the smallest in an []
def findSmallestItem(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        # if ith element is less than the smallest then ith elem=smallest
        if arr[i] < smallest:
            smallest = arr[i]
            # posision of the ith elem = smallest index
            smallest_index = i
    return smallest_index

# Sort an array using selection sort - O(n^2)
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallestItem(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print selectionSort([20,3,4,0,70,45,100])