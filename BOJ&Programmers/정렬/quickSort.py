def quicksort(x):
    if len(x) < 2:
        return x
    else:
        pivot = x[0]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def reverse_quicksort(x):
    if len(x) < 2:
        return x
    else:
        pivot = x[0]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return reverse_quicksort(greater) + [pivot] + reverse_quicksort(less)


arr = [1, 2, 3, 3, 3, 3, 4, 4]
arr1 = [3, 2, 4, 4, 2, 5, 2, 5, 5]
arr2 = [1,2,3,4,5,6,7]

