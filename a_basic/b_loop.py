# 1 + 2 + 3+ .. + n = sum
# 매개변수로 n을 입력받아 위와같은 형태로 출력하시오
def q1(n):
    st='1'
    sum=1
    
    for i in range(2,n+1):
        st += '+' + str(i)
        sum += i
    st += '=' + str(sum)
    return st
            
print(q1(10))


def q(n):
    st='1'
    sum=1

    for i in range(2,n+1):
        st += '+'+str(i)
        sum+=i
    st += '=' + str(sum)
    return st

print(q(10))    
        
# 다이아몬드 별찍기
# 사용자로 부터 2이상의 자연수를 입력 받아
# 한 변의 길이가 사용자의 입력값인 다이아몬드를 그려보시오
#     *      
#    ***    
#   *****    
#  *******  
# *********   
#  *******   
#   *****   
#    ***    
#     *   
  
# 1. 문제 -- 공백까지 해서 만들어보자..
def q2(n):
    st='*'
    blank=' '
    for i in range(1,n+1):
        print(blank*(2*n-i),st*(i-1)+st*i)
    for j in range(n-1,0,-1):
        print(blank*(2*n-j),st*(j-1)+st*j)
    
print('==')
q2(5)

# 2. 답
# *의 개수는 홀수로 증가 : 2n-1
# 공백의 개수 : cnt-n
# n은 1부터 1씩 증가하는 자연수
# cnt는 입력값
# ---------
# *의 개수는 홀수로 감소 : 2n-1
# 공백의 개수는 1부터 1씩 증가
# n은 cnt-1부터 1씩 감소하는 자연수

def print_diamon(cnt):
    print('=====')
    for i in range(cnt):
        n=i+1
        for j in range(cnt-n):
            print(' ', end='')
        for k in range(2*n-1):
            print('*',end='')
        print()
        
    white_space=1
    for i in range(cnt-1,-1,-1): 
        for j in range(white_space):
            print(' ',end='')
        for k in range(2*i-1):
            print('*',end='')
        white_space += 1
        print()
    

print_diamon(5)