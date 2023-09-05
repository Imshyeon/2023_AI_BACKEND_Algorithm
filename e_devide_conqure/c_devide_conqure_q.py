# 거듭제곱 최적화   ** 다시 풀어보기
# 매개변수 A,B를 받아 A를 B번 곱한 값을 반환하는 함수를 작성하시오
# B가 짝수일 경우, A^B = A^(B//2) * A^(B//2)
# B가 홀수인 경우, A^B = A^(B//2) * A^(B//2) * A

def pow(a, b):
    if b == 0 : return 1
    if b == 1 : return a    # 재귀 탈출문
    if b % 2 == 0:
        return pow(a, b//2) * pow(a, b//2)
    else:
        return pow(a, b//2) * pow(a, b//2) * a

print(pow(5,100)) 