nums = [100,5,88,4,9,19,15]
# [5,88,4,9,19,100]
# [5,4,9,19,15,88,100]
# [4,5,9,15,19,88,100]


def bubble_sort(alist):
    unsorted = True
    passes = 1
    while unsorted:
        unsorted = False
        for i in range(len(alist) - passes):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                unsorted = True
        passes += 1
        
bubble_sort(nums)

print(nums)
