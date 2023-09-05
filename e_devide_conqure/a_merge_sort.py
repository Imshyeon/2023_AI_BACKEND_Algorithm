# 정렬된 배열 두 개를 매개 변수로 받아 하나의 정렬된 배열로 합쳐주는 함수
# [1,5,7,13] -> i 인덱스를 가지게 함
# [2,4,9,12,15] -> j 인덱스를 가지게 함.
# 각 배열을 i, j 인덱스를 하나씩 이동하면서 비교. 만약에 i=0 이고 j=0 인 인덱스를 비교했을 때, i<j 이면 배열에 i=0의 값을 입력하고 i+=1, j는 그대로
def merge(arr1, arr2):  #새 배열 생성 : 깊은복사
    res = [] 
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):  # 둘 중 하나라도 False면, while문 종료
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else: # arr1[i] > arr2[j]
            res.append(arr2[j])
            j += 1
    if i < len(arr1) :  # arr1을 끝까지 탐색하지 못했다면
        res += arr1[i : len(arr1)]
    else:   #arr2을 끝까지 탐색하지 못했다면
        res += arr2[j : len(arr2)]
    
    return res


def mergesort(arr):
    n = len(arr)
    if n <= 1 : 
        return arr    # 정렬할 게 없다.
    else:   # 반씩 쪼갬 (분할 작업 시작)
        mid = n // 2
        arr1 = mergesort(arr[0 : mid])
        arr2 = mergesort(arr[mid : n])
        return merge(arr1, arr2)
