from b_hashtable import *
from c_stack import *

def is_pair(text):
    
    # # 1번
    # stack = Stack()
    
    # for ch in text:
    #     if ch == '(' or ch == '[' or ch =='{':
    #         stack.push(ch)
    #     else:
    #         #스택이 비어있는 경우(닫힌 괄호).. 이미 짝이 안맞는다.
    #         if stack.is_empty(): return False
    #         open = stack.pop()
            
    #         if open == '(':
    #             if ch != ')' : return False
                
    #         elif open == '{' :
    #             if ch != '}' : return False
                
    #         elif open == '[' :
    #             if ch != ']' : return False

    # return True if stack.is_empty() else False    
    # # 스택이 비어있는 경우, 그니까 다 매칭이 끝난경우에 True
    # # 열린괄호가 하나 더 있어서 매칭 안되는 경우 False
    
         
    # 2번
    hashtable = HashTable()
    hashtable.add('(',')')
    hashtable.add('{','}')
    hashtable.add('[',']')  
    
    stack = Stack()
    
    for ch in text:
        if ch in hashtable:
            stack.push(ch)
            continue
        
        #스택이 비어있는 경우(닫힌 괄호).. 이미 짝이 안맞는다. ex. ](){} 인 경우, ]는 이미 안들어감. 안맞음.
        if stack.is_empty(): return False
        k = stack.pop()
            
        if ch != hashtable.get(k): return False

    return True if stack.is_empty() else False 
            
            
print(is_pair('{}()[]'))  #T
print(is_pair('{([])}'))  #T
print(is_pair('{([}])}')) #F


#------------------1급 객체--------------------
# 예시
def hello():
    print('안녕')

def bye():
    print('잘가')
    
def study():
    print('공부')
    
dict = {'hello':hello, 'bye':bye, 'study':study}

def translate_eng_to_kor(eng):  # 등위비교(같을때)는 이렇게 쓰라.
    dict[eng]()
    
translate_eng_to_kor('hello')
translate_eng_to_kor('bye')
translate_eng_to_kor('study')