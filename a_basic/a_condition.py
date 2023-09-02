# 세 수 중 최대값 구하기
def max(a, b, c):
    max = a
    if(b > max): max = b
    if(c > max) : max = c
    return max

# 세 수 중 최소값 구하기
def min(a, b, c):
    min = a
    if(b < min) : min = b
    if(c < min) : min = c
    return min
 
# 세 수 중 중간값 구하기
def med(a, b, c):
    if(a >= b):
        if(b >= c) : return b
        if(a <= c) : return a
    elif(a > c) : return a
    elif(b > c) : return c
    else: return b
    
# ? 이게 맞나?? 좀 더 찾아보기
def mid(a,b,c):
    if(a > b):
        if(b > c) : return b
        elif(a < c) : return a
        elif(b < c) : return c
    elif(a<b):
        if(b<c):return b
        elif(b>c) : return c
        elif(c<a) : return a

print('max:',max(50,255,30))
print('min:',min(50,255,30))
print('med:',med(50,255,30))
print('mid:',mid(100,300,200)) # 답은 맞게 나옴