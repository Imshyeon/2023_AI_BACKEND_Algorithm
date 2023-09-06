def fibo_recursive(n):  # 일반 피보나치 수열_재귀 이용 in a_basic/c_math.py
    if n == 0:
        return 0
    elif n == 1 or n == 2 :
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)
    
#---

def fibo_dp(n, memo=[None for _ in range(100)]):
    if n == 0:
        return 0
    
    if n <= 2 :
        return 1
    
    if memo[n] is not None: # 이전에 계산해 둔 값이 있다면 수행 = fibo(n-2) 계산 시 사용됨.
        return memo[n]
    
    # n-1 쪽은 연산을 하고, n-2 재귀가 도는 시점에는 직전에 연산한 값이 들어있다.
    # 아래의 식에서 fibo(n-1)이 우선적으로 모두 계산된 뒤, fibo(n-2)가 수행이 된다.
    memo[n] = fibo_dp(n-1, memo) + fibo_dp(n-2, memo) 
    return memo[n]
    
print(fibo_dp(10))

#---

def fibo_dp2(n):
    tmp = []
    tmp.append(1)
    tmp.append(1)
    
    if n < 2: return tmp[-1]    #이전 피보나치 수열의 값 저장
    
    for i in range(2,n):
        tmp.append(tmp[i-2] + tmp[i-1])
        
    return tmp[-1]

print(fibo_dp2(10))
