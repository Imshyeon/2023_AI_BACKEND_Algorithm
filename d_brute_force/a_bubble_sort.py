# 나
def bubble_sort(arr):
    n = len(arr)
    for _ in range(n):
        for i in range(n-1):
            if arr[i] > arr[i+1] : 
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(bubble_sort([5,6,1,23,55,667,26,67]))    

# 풀이
def bubble_sort_ans1(arr):   # 0.050s
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1) :
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 회차가 갈수록 가장 배열의 마지막 요소는 해당 배열에서 가장 큰 값이 된다. 따라서, 회차가 갈수록 비교 연산의 수를 하나씩 줄이면 된다.
def bubble_sort_ans2(arr):   # 0.031s => 절반으로 감소
    for i in range(len(arr) - 1 , 0, -1):   # 역순으로 진행
        for j in range(i) :
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort_ans3(arr):   # 
    for i in range(len(arr) - 1 , 0, -1):   
        flag = False    
        for j in range(i) :
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # 큰 값을 뒤로 보내는 작업
                flag = True # 한번이라도 정렬이 된다면 flag = True
                
        if not flag:    # 정렬 단계를 진행하다가 어떠한 단계에서 flag가 더이상 True가 되지 않고 False라면(정렬이 완료가 되었다면) 리턴.
            return arr
        
    return arr



#======내림차순======
def bubble_sort_ans4(arr):   # 
    for i in range(len(arr) - 1 , 0, -1):   
        flag = False    
        for j in range(i) :
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # 작은 값을 뒤로 보내는 작업
                flag = True # 한번이라도 정렬이 된다면 flag = True
                
        if not flag:    # 정렬 단계를 진행하다가 어떠한 단계에서 flag가 더이상 True가 되지 않고 False라면(정렬이 완료가 되었다면) 리턴.
            return arr
        
    return arr