class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None
    
    def __str__(self):
        return self.data
        
class Stack :
    def __init__(self):
        self.top = None
        
    def push(self,data):
        node = Node(data)
        
        # 처음 들어오거나, 더이상 가져갈게 없을 경우
        if self.top is None:
            self.top = node
        else: 
            node.next = self.top
            self.top = node
    
    # 가장 위에 있는 데이터를 꺼내고 삭제
    def pop(self):
        if self.top is None:
            return None
        
        node = self.top # self.top이 node를 유일하게 참조하고 있었음
        self.top = node.next # self.top에 node.next를 넣어주면 node는 이제 아무도 참조 안함 -> node 데이터를 지우는 건 garbage collector가 함
        return node.data
    
    # 가장 위에 있는 데이터를 꺼내기만 함
    def peek(self):
        if self.top is None: return None
        return self.top.data
    
    def is_empty(self): # self.top이 None인지 아닌지 확인
        return self.top is None
            
    def __str__(self):
        if self.top is None:
            return '빈 스택입니다.'
        link = self.top
        res = '[ top << ' + str(link.data)
        
        while link.next is not None:
            temp = link.next
            res += ', ' + str(temp.data)
            link = temp
        res += ' ]'
    
        return res