#카톡에서 가져오기
'''
def partition2(arr, low, high):
    pivot_item = arr[low]
    i = low + 1
    j = high    # 이 부분이 이전과는 다름
    
    while i <= j :  # 역전 되는 시점에 바꿀 것.
        while arr[i] < pivot_item:
            i += 1
            if i > high : break
            
        while arr[j] > pivot_item:
            j -= 1
            if j < low : break
    
        if i < j:   # 위의 while문을 통과하여 최종적인 i와 j값이 생겼을 때, 만약에 --(피봇보다 큰 값=i)---(피봇보다 작은 값=j)-- 라면, arr[i]와 arr[j]의 위치는 바뀌어야 한다.
                    # 왜냐하면, 피봇을 기준으로 큰 값, 작은 값을 정렬하는데, 큰 값은 피봇 기준으로 뒤에 있어야하기 때문이다.
                    # 따라서 만약 [피봇보다 작은값 - 피봇보다 큰 값] 순으로 있다면, 둘의 위치를 바꿔줄 필요가 있다.
                    # if i<j의 의미는 둘의 값이 [피봇보다 작은값 - 피봇보다 큰 값]임에도 불구하고 인덱스 위치가 i가 더 작은 곳에 있다면 바꾸라는 의미이다.
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1 
              
    pivot_point = j
    arr[low], arr[pivot_point] = arr[pivot_point], arr[low]
    return pivot_point
        


def quicksort2(arr, low, high):
    if low < high:
        pivotpoint = partition2(arr, low, high)
        quicksort2(arr, low, pivotpoint-1)
        quicksort2(arr, pivotpoint+1, high)  # pivot point는 위치가 확정이니까 나머지를 재귀적으로 분할 -> 정렬
'''
        
# '''
import random
def partition2(arr, low, high):
    pivotitem = arr[low]
    i = low + 1
    j = high
    
    while (i <= j) :
        while arr[i] < pivotitem:
            i += 1
            if i > j: break
            
        while arr[j] > pivotitem:
            j -= 1
            if j < i: break
            
        if i <= j :
            arr[i], arr[j] = arr[j], arr[i] # 요소의 위치 바꿈
            i += 1  # 위치를 바꾼 뒤, 인덱스의 한칸 이동
            j -= 1  # 위치를 바꾼 뒤, 인덱스의 한칸 이동
            
    pivotpoint = j
    arr[low], arr[pivotpoint] = arr[pivotpoint], arr[low]
    return pivotpoint


def quicksort2(arr, low, high):
    if low <= high:
        pivotpoint = partition2(arr, low, high)
        quicksort2(arr, low, pivotpoint -1)
        quicksort2(arr, pivotpoint+1, high)
# '''