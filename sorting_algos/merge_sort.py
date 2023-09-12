nums = [100,5,88,4,9,19,15]
# [5,88,4,9,19,100]
# [5,4,9,19,15,88,100]
# [4,5,9,15,19,88,100]

def merge_sort(alist):

        middle = len(alist) // 2       
        left_half = alist[:middle]
        right_half = alist[middle:]

        if len(alist) > 2:
            merge_sort(left_half)
            merge_sort(right_half)

    #left_point, right_point, main_point = 0,0,0
        left_point = right_point = main_point = 0

        while left_point < len(left_half) and right_point < len(right_half):
            if left_half[left_point] < right_half[right_point]:
                alist[main_point] = left_half[left_point]
                left_point += 1
            else:
                alist[main_point] = right_half[right_point]
                right_point += 1
            main_point += 1

        while left_point < len(left_half):
            alist[main_point] = left_half[left_point]
            left_point += 1
            main_point += 1

        while right_point < len(right_half):
            alist[main_point] = right_half[right_point]
            right_point += 1
            left_point += 1
            main_point +=1

merge_sort(nums)

print(nums)