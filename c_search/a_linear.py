# 선형 검색 : 무작위로 늘여놓은 데이터에서 검색을 수행
# O(N)만큼의 시간복잡도

# 1-1. 배열에서 key와 같은 요소를 찾아 인덱스를 반환하자.
# 종료 조건 1 : key와 같은 요소를 찾았다.
# 종료 조건 2 : 전체를 모두 탐색하였으나 key와 같은 요소를 찾지 못하였다.
def seq_search(arr,key):
    i = 0
    while True: # for를 사용해도 되지만 종료 조건을 알아보기 위해서 while 사용
        if i == len(arr) : return -1
        if key == arr[i] : return i
        i += 1
    return i

print(seq_search([5,2,3,4,6,77,1,23],1))    # 1값을 찾음 -> 인덱스는 6
# while을 할 때마다 검증을 2번해야함..

# 1-2. 보초법
# 두 가지 종료 조건 중, 종료조건 2번(탐색이 끝날 때 까지 요소를 못찾는다면)을 생략하는 방법
# 배열의 마지막 인덱스에 찾고자하는 값과 같은 값을 저장
# 만약 마지막 인덱스가 찾고자하는 값으로 나온다면 검색 실패로 처리
# 시간복잡도는 O(N)이지만 실제 연산은 반으로 줄어듦
def seq_search_sen(arr, key):
    last_idx = len(arr) - 1
    if arr[last_idx] == key: # 마지막 인덱스가 찾고자 하는 값이라면 인덱스 반환
        return last_idx    
    arr[last_idx] = key # 아니라면 보초 투입
    '''
    # python은 이게 되지만, 다른데에선 안될 수 있다.
    last_idx = len(arr)   
    arr[last_idx] = key # 보초 투입
    '''
    i = 0
    while True:
        if key == arr[i] :
            return -1 if i == last_idx else i
        i += 1
        
print(seq_search_sen([5,2,3,4,6,77,1,23],1))    # 6으로 잘 나옴.