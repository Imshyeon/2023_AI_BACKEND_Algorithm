# 기존방식(a_merge_sort.py)이 2n개의 배열이 메모리에 올라간다면 (매개변수가 2개니까)
# 이 방식은 n개의 배열만 메모리에 올라간다. -> 공간복잡도 감소
# 얕은 복사 : 원본 배열의 주소값을 넘겨줌
def merge2(arr, low, mid, high):    #def merge(arr1, arr2)를 사용한 것과 대신에 low, mid, high 인덱스 값을 넘겼다.
    res = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1
    if i <= mid : #i가 mid까지 탐색을 못했다면
        res += arr[i : mid + 1] 
    else:
        res += arr[j : high + 1]
    
    for i in range(low, high+1):
        arr[i] = res[i - low]   # res는 low+1, low+2,,니까 res[i-low]하면 res의 인덱스가 나옴
        
def mergesort2(arr, low, high): # len(arr) = 300
    if low < high:
        mid = (low + high) // 2
        mergesort2(arr, low, mid)   # low = 0, mid = 149 -> (0,74), (75,149) -> ,,,
        mergesort2(arr, mid+1, high)    # mid+1 = 150, high = 299 -> (150, 224), (225, 299) -> ,,,
        merge2(arr, low, mid, high)  # ex. low = 0, mid = 0, high = 1
                                    #     low = 2,        , high = 3 ?