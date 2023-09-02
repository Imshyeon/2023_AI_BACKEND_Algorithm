# Q1. 매개변수로 전달받은 숫자가 소수인지 판별하는 함수를 만들자.
def is_prime(num):
    if num == 2 : return True
    for x in range(2,num):
        if num%x == 0:
            return False
    return True

def is_prime_ans(num):
    # if num==2 : return True   # 1.
    if num % 2 == 0 and num != 2 : return   # 2. 
    
    # for i in range(3,num):  # 1. range(2,num)하고 위에 if를 없애도 되긴 함.. but 그래도 적어주자
    #     if num%i==0:
    #         return False
    # return True

    for i in range(3,num,2):  # 2. range(2,num)하고 위에 if를 없애도 되긴 함.. but 그래도 적어주자
        if num%i==0:
            return False
    return True

from math import sqrt
def is_prime_plus(num):
    for i in range(2,int(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


# Q2. 2부터 매개변수로 입력받은 값 사이에 존재하는 소수를 구해 리스트로 반환하는 함수를 작성
def prime_numbers(num):
    prime_list=[]
    for i in range(2,num):
        if is_prime_plus(i):
            prime_list.append(i)
        
    return prime_list


# Q3. 최대공약수
def gcd1(a, b):
    # 나 
    # gcd_list=[]
    # if a < b:
    #     for i in range(1, b+1):
    #         if a % i == 0 and b % i == 0:
    #             gcd_list.append(i)
    # else:
    #     for i in range(1, a+1):
    #         if a % i == 0 and b % i == 0:
    #             gcd_list.append(i)
    
    # for i in gcd_list:
    #     max=i
    #     if max<i:
    #         max=i
    # return max
    
    min = b
    if a < b:            
        min = a
        
    for i in range(min, 0, -1):
        if a % i ==0 and b % i == 0 :
            return i

# 유클리드 호제법을 활용한 최대공약수 구하기
# a, b 두 수가 있을 때(a>b)
# a를 b로 나눈 나머지는 두 수의 최대 공약수의 배수이다.
def gcd2(a, b): 
    while b > 0 :
        a, b = b, a % b        
    return a

# G가 a와 b의 최대공약수일 때 a = MG, b = NG라 표현할 수 있다.
# a > b일 때
# a mod b
# a = bq + r -----q는 몫, r은 나머지
# a는 MG로 b는 NG로 표현이 가능하므로, MG = NGq + r
# r = MG - NGq
# r = G(M - Nq)   ----- > r은 G의 (M - Nq)만큼의 배수 => 최대공약수의 배수이다.
#  
# G의 배수인 두 수의 나머지는 G의 배수임으로 b와 r의 나머지연산의 결과도 G의 배수

# b mod r
# b = NG
# r = PG --> PG = (M - Nq)
# c = QG

# ... 반복될 수록 Q값은 작아짐

# x = XG
# y = G
# z = 0 ---> 나머지 => 이런 시점이 온다.




# Q4. 최소공배수
def lcm1(a, b):
    gcdVal=gcd2(a,b)
    # return gcdVal * (a / gcdVal) * (b / gcdVal) # a * b * gcdVal / gcdVal / gcdVal
    return a * b / gcdVal    


# Q5. 팩토리얼
# 0 이상의 정수
def fac1(num):
    # 나
    # if num == 0:
    #     res = 1
    #     return res
    # else:
    #     res = 1
    #     for i in range(num,1,-1):
    #         res = res*i
    #     return res
    if num < 0 : return -1
    res = 1
    for i in range(1,num+1):
        res *= i
    return res

# 팩토리얼 재귀함수 사용
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1) # 재귀함수(꼬리재귀는 아님! 수식의 일부니까..)
# 꼬리재귀 : 재귀호출 명령이 함수의 제일 마지막에 오면서, 함수의 리턴값이 수식의 일부이지 않은 방식
# 꼬리재귀로 작성된 코드는 컴파일러가 내부적으로 반복문으로 변경하여 실행 -> 프레임이 열리고 닫히는 비용이 발생하지 않음.
#   => 대부분의 언어들은 꼬리재귀로 작성된 코드의 경우 stack overflow가 발생하지 않음 
#   -> stack overflow : 스택 영역에 열 수 있는 프레임의 숫자를 초과할 경우 발생하게 되는 에러

# 파이썬은 꼬리재귀 최적화를 지원하지 않는다. 그래서 파이썬으로는 재귀를 쓰지않는게...

def factorial_tail(n, result=1):
    if n == 0:
        return result
    else:
        return factorial_tail(n-1,n*result) # 반환되는 값을 추가적으로 저장이 되지 않는다.. 하지만 파이썬은 안됨...
    
    
    
# 피보나치 수열 **
def fibonacci(num):
    if num < 1: return -1
    prev, cur = 1, 1
    for i in range(3,num+1):
        prev, cur = cur, prev+cur
    return cur

# 피보나치 재귀 **이렇게하면 안된다!!
def fibo_recursive(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2 :
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)
    
def fibo_tail(n, before=0, next=1):
    if n == 0:
        return 0
    elif n == 1:
        return next
    else:
        return fibo_tail(n-1, next, before+next)