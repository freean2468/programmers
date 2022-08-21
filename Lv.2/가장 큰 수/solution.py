# https://school.programmers.co.kr/learn/courses/30/lessons/42746#
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = str(arr[len(arr) // 2])
    lesser_arr, equal_arr, greater_arr = [], [], []
    
    for s in arr:
        s = str(s)
        if s + pivot < pivot + s:
            greater_arr.append(s)
        elif s + pivot > pivot + s:
            lesser_arr.append(s)
        else:
            equal_arr.append(s)
    
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


def solution(numbers):
    return str(int(''.join(str(s) for s in quick_sort(numbers))))