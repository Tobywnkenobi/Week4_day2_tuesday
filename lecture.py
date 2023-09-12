#In-place Al Gore Rythem

l_1 = [10, 4, 3, 8, 4, 2, 6]

print(f"{l_1 = } before")
sorted_list = l_1.sort()
print(f"{l_1 = }after\n{sorted_list}")

def inplace_swap(alist):
    alist[0], alist[-1] = alist[-1], alist[0]
    return alist
#Out of place Al Gore

print(f"{l_1 = } before")
sorted_new_list = sorted(l_1)
print(f"{l_1 = } after")

def outplace_swap(alist):
    alist_copy = alist[::]
    alist_copy[0], alist_copy[-1] = alist_copy[-1], alist_copy[0]


