import random
import time

# 生成长度为10^n的递增随机数列
# 修改数字
def generate_random_list():
    random_list = []
    num = 0
    for _ in range(10000):
        num += random.uniform(0, 1)
        random_list.append(num)
    return random_list

# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# 快速排序
def quick_sort(arr):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        while low < high:
            pi = partition(arr, low, high)

            if pi - low < high - pi:
                quick_sort_helper(arr, low, pi - 1)
                low = pi + 1
            else:
                quick_sort_helper(arr, pi + 1, high)
                high = pi - 1

    quick_sort_helper(arr, 0, len(arr) - 1)


# 插入排序
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 生成三组递增随机数列
random_list1 = generate_random_list()
random_list2 = generate_random_list()
random_list3 = generate_random_list()

# 归并排序并计时
start_time = time.perf_counter()
sorted_list1 = merge_sort(random_list1)
end_time = time.perf_counter()
merge_sort_time = end_time - start_time

# 快速排序并计时
start_time = time.perf_counter()
sorted_list2 = quick_sort(random_list2)
end_time = time.perf_counter()
quick_sort_time = end_time - start_time

# 插入排序并计时
start_time = time.perf_counter()
insertion_sort(random_list3)
end_time = time.perf_counter()
insertion_sort_time = end_time - start_time

# 输出排序所需的时间
print("归并排序所需时间：", "{:.6f}".format(merge_sort_time))
print("快速排序所需时间：", "{:.6f}".format(quick_sort_time))
print("插入排序所需时间：","{:.6f}".format(insertion_sort_time))

'''
插入排序所需时间随着长度增加而增加。长度变为十倍，时间几乎变为十倍。所有情况下耗时是三种排序中最少的。
这是因为插入排序在对递增数列排序时时间复杂度时O(n)。
归并排序所需时间随着长度增加而增加。长度变为十倍，时间几乎变为十倍。所有情况下耗时是三种排序中中间的。
这是因为归并排序在对递增数列排序时时间复杂度时O(nlog2n)。
归并排序所需时间随着长度增加而增加。所有情况下耗时是三种排序中最多的。
这是因为快速排序(以最后一个数为基准)在对递增数列排序时时间复杂度时O(n^2)。
'''