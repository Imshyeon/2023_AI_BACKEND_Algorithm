# 나
def selection_sort(arr):
    sorted=[]
    unsorted=[]
    for i in range(len(arr)-1):
        min = arr[i]
        for j in range(i, len(arr)-1):
            if min > arr[j]:
                min, arr[j] = arr[j], min
                sorted.append(min)
                unsorted.append(arr[j])
                print(arr)
        return sorted, unsorted
# print(selection_sort([5,6,1,23,55,667,26,67]))    
    
    
# 풀이    
def selection_sort_ans(arr):
    for p in range(len(arr)-1):
        min = p
        for i in range(p,len(arr)):
            if arr[min] > arr[i]:
                min = i
        
        arr[p], arr[min] = arr[min], arr[p]
    return arr

# print(selection_sort_ans([5,6,1,23,55,667,26,67]))  