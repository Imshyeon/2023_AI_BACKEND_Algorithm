
# 1. 자연수 배열에서 가장 큰 수 찾기
def check_max(arr):
    max_num = arr[0]
    for i in range(1,len(arr)):
        if max_num < arr[i]:
            max_num = arr[i]
    return max_num
    
            
    # 2. 자연수 배열에서 가장 큰 두 수를 찾아 배열로 반환
def check_max2(arr):
    #나
    max_num1=arr[0]
    max_num2=arr[1]
    if max_num1 < max_num2:
        max_num1, max_num2 = max_num2, max_num1
        
    for i in range(1, len(arr)):
        if max_num1 < arr[i]:
            max_num1, max_num2 = arr[i], max_num1
        elif max_num2 < arr[i]:
            max_num2=arr[i]
    
    return [max_num1, max_num2]
    
    # 강사
def check_max3(arr):    
    if len(arr) < 2: return arr
    max, second = arr[:2]
    if max<second : 
        max, second = second, max
        
    # max : e > max
    # second : e <= max, e > second
    for e in arr[2:]:
        if e > max : 
            max, second = e, max
        elif e > second:
            second = e
    return [max, second]


# 3. 앞으로 읽어도, 뒤로 읽어도 같은 단어(회문)인지 검사하는 함수를 작성
# aabaa -> True
# aaabaa -> False
# hint ; 문자열도 배열이다. // 기러기, 토마토, 역삼역
from math import floor
def check_palindrome(text):
    # t_list = []
    # for t in text:  #한글자씩
    #     t_list.append(t)
    
    # tl=len(t_list)-1
    
    # 1. 첫번째
    # if t_list[0] == t_list[tl]:
    #     return True
    # else : False
    
    # 2. 두번째
    # n = floor(tl/2)
    # if n%2==1:
    #     if t_list[floor(tl/2)-n] == t_list[floor(tl/2)+n]:
    #         return True
    # else:
    #     if t_list[floor(tl/2)-1] == t_list[floor(tl/2)]:
    #         return True
    
    # 3. 세번째
    n= len(text)//2 # n = floor(len(text)/2) 의 수정
    print(n)
    for i in range(n):
        if text[i] == text[-(i+1)]:
            return True
    return False
            
            
    # 강사
    # left, right = 0, len(text)-1
    # while(left < right):
    #     if text[left] != text[right]:
    #         return False
    #     left, right = left+1, right-1
    # return True