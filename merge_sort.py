# 每一回合的合併處理是O(n)，總共需要O(logn)回合才完成(樹高約=logn)
# https://www.youtube.com/watch?v=nCNfu_zNhyI
# https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/analysis-of-merge-sort
'''
The divide step takes constant time.
The conquer step, where we recursively sort two subarrays of approximately O(n/2)
The combine step merges a total of n elements, taking O(n).
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)

def merge_two_sorted_lists(a,b):
    len_a = len(a)
    len_b = len(b)
    sorted_list = []

    i = 0
    j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    while i < len_a:
        sorted_list.append(a[i])
        i+=1

    while j < len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list

if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        sorted_list = merge_sort(arr)
        print(sorted_list)