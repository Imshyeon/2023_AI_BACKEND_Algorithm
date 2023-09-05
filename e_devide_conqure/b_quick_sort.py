def partition(arr, low, high):
    pivot_item = arr[low]
    j = low
    for i in range(low + 1, high + 1):
        if arr[i] < pivot_item: 
            j += 1  # j는 pivot item보다 작은 애들인 몰려잇는 애들의 끝 인덱스! => pivot_item(기준값), ----, [j] 이런식으로 될 것이다. 따라서 초반에는 j와 i의 위치는 같다..
            arr[i], arr[j] = arr[j], arr[i] # [15, 1, 3, 50, 14 ,,]를 생각해보자, pivot_item=15이고, i = j = 1 이다.
                                            # 15, 1(i,j), 3, 50, 14 ,,
                                            # 15, 1, 3(i,j), 50, 14 ,,
                                            # 15, 1, 3(j), 50(i), 14 => pivot_item < 50 이라서 j값이 증가하지 않는다.
                                            # 15, 1, 3, 14(j), 50, (i) ,, => pivot item의 위치는 j의 뒤로 와야한다.
    pivot_point = j
    arr[low], arr[pivot_point] = arr[pivot_point], arr[low] # 결국 최종적으로 pivot은 j값이 됨.
    return pivot_point

def quicksort(arr, low, high):
    if low < high:
        pivotpoint = partition(arr, low, high)
        quicksort(arr, low, pivotpoint-1)
        quicksort(arr, pivotpoint+1, high)  # pivot point는 위치가 확정이니까 나머지를 재귀적으로 분할 -> 정렬