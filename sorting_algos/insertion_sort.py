nums = [100,5,88,4,9,19,15]
# [5,88,4,9,19,100]
# [5,4,9,19,15,88,100]
# [4,5,9,15,19,88,100]


def insertion_sort(alist):
    for i in range(1, len(alist)):
        while i > 0 and alist[i-1] > alist[i]:
            alist[i], alist[i-1] = alist[i-1], alist[i]
            i -= 1

insertion_sort(nums)

print(nums)