class Node:
    def __init__(self,data):
        self.data=data
        self.next=None # 다음 노드의 주소를 저장
        
# __메서드__(매직메서드, 던더메서드)
# 파이썬에서 제공해주는 내장함수 또는 구문에서 호출하기 위해 작성하는 함수

# 덕타이핑 : 객체의 속성 및 메서드의 집합이 객체의 타입을 결정한다.
# 만약 어떤 새가 오리처럼 걷고, 헤엄치고, 소리를 낸다면 그 새를 오리라고 부를 수 있다.

        
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0 # List의 길이
        
    # print 함수에 객체를 매개 변수로 전달할 경우 출력될 문자열을 반환하는 매직메서드
    def __str__(self):
        node=self.head
        if node is None: return f'비어있음'
        res = "["
        while node.next:
            res += str(node.data) + ', '
            node = node.next
        res += str(node.data) + "]" # 마지막 데이터 담기
        return res
    
    def __len__(self):
        return self.length
    
     
    # 매개변수로 전달받은 데이터를 리스트에 추가
    def append(self, data):
        
        node = Node(data)
        if self.head is None : # 첫번째 헤드가 None이면
            self.head = node
        else:
            prev = self.head    # 우선, 제일 첫번째 노드는 이전 노드라고 선언
            while prev.next:    # prev.next가 None이면 해당 반복문 종료. next가 None인 Node를 탐색
                prev = prev.next    # 노드 이동,,
                
            prev.next=node  # 제일 마지막 노드가 되었을 때, 새로운 노드를 이전 노드의 다음으로 설정. 
                            # next가 None(현재 마지막 요소인) 노드에 새로운 노드를 링크
            
        self.length += 1
        
    # 매개변수로 전달받은 데이터를 리스트의 가장 앞에 추가 **
    def prepend(self,data):
        node = Node(data) # 데이터를 추가, 만들기.. 이런거를 할 때는 새로운 Node를 불러와서 다시 만들어야 한다
        node.next = self.head   # 제일 첫번째 노드를 새로운 노드의 next 노드로 연결
        self.head = node    # 새로운 노드를 첫번째 노드로 설정
        self.length += 1    # 길이 + 1
        
    def insert(self, i, data):
        if i < 0 : raise IndexError('인덱스 음수 불가능')
        if i == 0 : 
            self.prepend(data) 
            return
        if i >= self.length: 
            self.append(data)
            return
        
        node = Node(data)   # 데이터를 추가, 만들기.. 이런거를 할 때는 새로운 Node를 불러와서 다시 만들어야 한다.. LinkedList 생각해보면 됨
        prev = self.head    #제일 첫번째를 prev라고 선언
        for _ in range(i-1):    # 만약에 i = 2라고 하면, 2번째 인덱스 삽입이니까
            prev=prev.next # 그 노드 이전만큼 인덱스 이동
            
        node.next= prev.next # prev.next 노드를 node.next로 선언함으로써 [새로운 노드] - [원래 있던 그 다음 노드] 로 연결
        prev.next=node  # [이전 노드] - [새로운 노드]로 완전히 연결
        self.length += 1    # length + 1
    
    # 가장 뒤에 있는 데이터를 반환하고 삭제    
    def pop(self):
        node=self.head
        if node is None:
            return None #아무것도 없을 경우, 아무것도 리턴 안하겠다.
        
        if node.next is None:   # node가 1개인 경우 => node 반환하고, head를 None, length 하나 감소
            self.head = None
            self.length -= 1
            return node.data
        
        while node.next:
            prev=node   # node는 그 데이터 하나의 객체? 라고 생각하면 됨. 그러니까 데이터 한개가 담겨있는 어떤 공간?
            node=node.next  # node=node.next로 함으로써 다음 노드로 이동
        prev.next = None   # 이전노드의 다음노드가 None이니까 마지막 노드 값을 None으로 처리
        self.length -= 1    # 길이를 줄이고
        return node.data    # 마지막 노드의 데이터값을 반환
    
    
    # 가장 왼쪽에 있는 값 출력, 즉 가장 첫번째 데이터 반환 후 삭제
    def popleft(self):
        node = self.head
        if node is None:
            return None
        self.head=self.head.next # 첫번째를 그 다음 노드로 변경
        self.length -= 1
        return node.data
    
    # 매개변수로 전달받은 data를 삭제하고 성공여부를 Boolean으로 반환
    def remove(self,data):
        node = self.head
        if node.data == data:
            self.popleft()
            return True
        
        while node.next:
            if node.next.data == data:
                node.next=node.next.next    #node.next가 일치할 때 걔를 삭제하니까, 현재 노드랑 node.next.next를 연결
                self.length -= 1
                return True
            node=node.next  # node.next의 데이터가 내가 찾는 데이터와 일치하지 않으면 노드 이동
        return False    # 삭제할게 없으면, 삭제에 실패하면
        
            
    def reverse(self):
        # 나
        # node=self.head
        # if node is None: return None
        # while node.next:
        #     prev=node
        #     node=node.next
        #     self.prepend(node.data)
        #     if node.next is None:
        #         self.pop()
    
        if self.length <= 1 : 
            return
        
        prev = None
        while self.head.next:
            tmp = self.head.next    # self.head의 다음 노드를 tmp라고 이름 붙임
            self.head.next=prev     # 이전에 있던 노드를 self.head의 다음이라고 설정
            prev=self.head          # 현재 self.head를 prev라고 설정
            self.head=tmp
        self.head.next=prev
        
        

    def __iter__(self):
        return LinkedList.Iterator(self.head)
    
    
    # 파이썬에서는 __iter__와 __next__(이터레이터 프로토콜)가 선언되야지, 이 객체가 이터레이터로 정의가 됨.
    class Iterator:
        def __init__(self, node):
            self.node = node
            self.call_cnt = 1
        
        def __iter__(self):
            return self
    
        def __next__(self):
            if self.node is None:
                raise StopIteration  
            
            print(f'{self.call_cnt}번째 호출입니다. {self.node.data}')
               
            data=self.node.data
            self.node=self.node.next
            self.call_cnt += 1
            return data