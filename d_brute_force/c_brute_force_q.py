# 종말 : 종말의 수란 어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수. 제일 작은 종말의 수는 666 그다음으로 는 1666,2666,3666 이다. 
# 사용자로부터 전달받은 n번째 에 해당하는 종말의 수 구하시오
# 매개변수로 전달받은 숫자까지 존재하는 모든 종말의 수를 담은 배열을 반환하시오.
def dooms_day(n):
    dooms=[]
    num = 666
    #while로 조건
    # for i in range(0,10000):
    #     if '666' in str(i) and cnt != n:
    #             dooms.append(i)
    #             cnt += 1
    #     elif cnt == n:
    #         return dooms
        
    while True:
        if '666' in str(num):
            dooms.append(num)
        elif len(dooms) == n:
            return dooms
        num += 1
        
#========풀이========
def doom_day(n):
    cnt = 0
    doom = 666
    arr = []
    
    while True:
        if '666' in str(doom) : 
            cnt += 1
            arr.append(doom)
        if cnt == n:
            break
        doom += 1
        
    return arr




# 일곱 난쟁이
# 일과를 마치고 아홉명의 난쟁이가 돌아왔다. 아홉명의 난쟁이는 모두 자신이 '백설공주와 일곱난쟁이'의 주인공이라고 주장했다.
# 백설공주는 일곱난쟁이의 키의 합이 100이 됨을 기억해냈다. 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱난쟁이를 찾는 프로그램을 작성하시오.
# 전달받은 배열의 요소 중 7 요소의 부분합이 100이 되게끔 하는 로직은 작성하고 부분합이 100이 되는 요소 7개를 배열로 반환하시오
def dwarf(arr):
    print(arr)
    dwarf_h=[]
    # while tot > 0:
    #     for i in range(len(arr)-1):
    #         if tot != 0 : 
    #             tot -= arr[i]
    #             dwarf_h.append(arr[i])
    #             print('tot=', tot, 'arr[i]=',arr[i])
    # while tot > 0 :
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            tot = sum(arr) - (arr[i] + arr[j])   
            # print('--->',tot, arr[i], arr[j])
            
            if tot == 100:
                res = arr[:i] + arr[i+1:j] + arr[j+1:]
                return res, tot
            
#========풀이========
# 얘는 역으로 접근해야함. 전체 합을 구하고, 어떤 두 난쟁이 값을 뺐을 때 100이 되는가?
def dwarf_ans(arr):
    s = sum(arr)
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if s - (arr[i] + arr[j]) == 100:
                a, b =arr[i], arr[j]
                arr.remove(a)
                arr.remove(b)
                return arr, sum(arr)
    return arr , sum(arr) # 실패인 경우

    