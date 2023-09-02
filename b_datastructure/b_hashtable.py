class Node:
    def __init__(self, key : str, data):
        self.key = key
        self.data = data
        self.next = None
        
    def __hash__(self): # __hash__를 override 함과 동시에 __eq__도 해줘야함. 왜냐하면 비교해야 할 필요가 있기 때문이다.
        # ord : 유니코드 문자를 나타내는 문자열이 주어지면 해당 유니코드 리턴..
        return 31 * sum([ord(s) for s in self.key]) # 31은 해쉬 만들 때 많이 넣는 값

    def __eq__(self, other):
        print('eq 매직메서드 호출')
        return self.key == other.key
    
    def __str__(self):
        # return f'[ key = '+ self.key + ' : data = ' + str(self.data) + ']'
        return f'[key = {self.key} : data = {str(self.data)}]'



class DuplicatedKey(RuntimeError): # 커스텀 에러 생성.. add와 set을 private로 한다음에 추가.
    pass        
        
        
        
class HashTable:
    def __init__(self, length = 30):
        self.max_len = length   # 테이블의 크기
        self.table = [None for _ in range(self.max_len)] # 배열생성
        self.length = 0
    
    def __str__(self):
        res='['
        for link in self.table:
            if link is None: continue
            
            while True: # link가 있는 경우
                res += str(link)
                
                if link.next is None: break
                link = link.next    # link.next가 None이 아니면.. 연결
        
        return res + ']'
        
        
    def hash(self, node):
        return abs(hash(node)) % self.max_len   # 위에서 정의한 __hash__ 가 적용됨.




    def __add(self, link, node):
        if link == node : raise DuplicatedKey   #link와 node가 같으면 중복된 키라고 에러를 올림. 코드 가독성 향상
        
    def __set(self, link, node):
        if link == node :
            link.data = node.data  
            raise DuplicatedKey   
        
        
        
    def __add_data(self, key : str, data, fn):
        # add
        if type(key) is not str:
            raise TypeError('문자열만 key로 사용이 가능합니다.')
        
        node = Node(key, data)
        # print(self.hash(node))  # 유니코드를 이용했기 때문에 key에 대해 일정한 해쉬 값이 나옴.
        index = self.hash(node) # 해당 hash(node)한 결과를 index로 설정
        
        if self.table[index] is None:
            self.table[index] = node
        else:
            link = self.table[index]    # 해당 인덱스에 저장된 첫번째 노드
            
            while True: # 현재 연결 리스트의 노드들 순회
                # if link == node:    # (== 했으니까 위의 eq 호출,, 따라서 key값 비교) 만약 link의 key값과 node의 key값이 같다면, 데이터를 추가히자 않고 return
                #     return
                try:
                    fn(link, node)    # 콜백으로 받아온 함수를 실행
                except:     # DuplicatedKey라는 예외가 발생하니까 except를 타서, return을 실행
                    return
                
                if link.next is None:   # 현재 노드가 연결 리스트의 마지막 노드임. 새 노드를 link.next로 추가하고 루프를 종료.
                    link.next = node
                    break
                
                link = link.next    # link변수를 다음 노드로 업데이트해서 다음 노드로 이동.
            
        self.length += 1
        
        # set
        # if type(key) is not str:
        #     raise TypeError('문자열만 key로 사용이 가능합니다.')
        
        # node = Node(key, data)
        # # print(self.hash(node))  # 유니코드를 이용했기 때문에 key에 대해 일정한 해쉬 값이 나옴.
        # index = self.hash(node) # 해당 hash(node)한 결과를 index로 설정
        
        # if self.table[index] is None:
        #     self.table[index] = node
        # else:
        #     link = self.table[index]    # 해당 인덱스에 저장된 첫번째 노드
            
        #     while True:
        #         if link == node:    # (== 했으니까 위의 eq 호출,, 따라서 key값 비교) 만약 link의 key값과 node의 key값이 같다면, 데이터를 추가히자 않고 return
        #             link.data = node.data
        #             return
                
        #         if link.next is None:
        #             link.next = node
        #             break
                
        #         link = link.next
            
        # self.length += 1    

#---------------------------------------------------------------------      
    # 키를 해싱해 data를 저장, 사용자가 이미 등록한 키로 다시 데이터를 저장할 수 없음.
    def add(self, key : str, data): #추가
        self.__add_data(key, data, self.__add)
        # 파이썬의 함수는 1급 객체
        # 1급 객체 : 값으로 다루어 질 수 있음, 매개변수로 넘길 수 있고, 변수에 담을 수 있고, return 값으로 쓸 수 있다.
 
# 처음에 set(수정)은 복붙해서 while - if 뺴고 다 복붙  ==> 이러면 가독성 넘 떨어지고 add 수정해야하면 set도 해야해서 불편..       
#---------------------------------------------------------------------        
    # 키를 해싱해 data를 저장, 사용자가 이미 등록한 키로 접근해 데이터를 수정 가능(데이터 덮어쓰기)
    def set(self, key : str, data): # 수정
        self.__add_data(key, data, self.__set)
        
#---------------------------------------------------------------------  
    def get(self, key : str):
        if type(key) is not str: raise TypeError('key는 str 타입')
        
        index = self.hash(Node(key,-1)) # value는 의미 없으니까 아무 값.
        link = self.table[index]
        
        # if link is None : return None  # while문의 조건으로 인해서 없어도 되긴 함
        
        while link is not None:
            if link.key == key:
                return link.data
            link=link.next  # 만약에 link.key == key가 아니면 다음 노드로 이동해서 계속 찾게
            
        return None # 만약 끝까지 없다면, None을 리턴
                
#---------------------------------------------------------------------              
    def __contains__(self, key):  # in ~ 을 쓸 수 있다. 포함 여부를 확인할 때 호출되는 매직 메서드
        return True if self.get(key) is not None else False

    def __iter__(self): # 해쉬테이블의 모든 데이터를 탐색할 수 있도록..
        return HashTable.Iterator(self)
    '''
    class Iterator: # None까지 리턴.. (나) // 값이 있는 부분만 출력하도록 바꿔보자
        def __init__(self, hashtable):
            self.hashtable=hashtable    # HashTable 객체
            self.index = 0  # 해시값. => None, None, 01, 02, ..., None
        
        def __iter__(self):
            return self
        
        # next는 Node를 반환하도록 구현
        def __next__(self):            
            if self.index == len(self.hashtable.table):    # 끝
                raise StopIteration
            else:
                node = self.hashtable.table[self.index] # self.hashtable.table은 list 타입
                if node is None : 
                    self.index += 1   # 만약에 해시테이블과 연결된 LinkedList의 노드값이 None이면, 해시테이블의 다음 인덱스로 이동
                else:   #만약에 해시테이블과 연결된 LinkedList의 노드값이 None이 아니라 값이 있으면
                    node = self.hashtable.table[self.index] # 값이 있는 노드 값을 리턴할 것이고
                    if node.next is None:   # 해당 노드의 다음 노드의 값이 None이면
                        self.index += 1 # 해시테이블의 인덱스를 다음으로 이동
            return node
    '''   
        
    # '''    
    class Iterator: # None은 제외하고 실제 값이 있는 부분만 리턴
        def __init__(self, hashtable):
            self.table=hashtable.table    
            self.size = hashtable.length
            self.table_idx = 0
            self.node = None
            self.iter_return_cnt = 0
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.iter_return_cnt >= self.size:
                raise StopIteration
            
            while self.table[self.table_idx] is None:   #table에 None이 아닌 다른 값이 있으면 종료
                self.table_idx += 1                     # 해당 인덱스 값을 가진 채로..
            
            #self.node가 None인 경우에만 self.table의 각 인덱스에서 첫번째 노드를 받아와야 하기 때문에 필요합니다!
            if self.node is None:   # 더이상 탐색할 노드가 없는 경우거나 위에 초기화한 값이면
                self.node = self.table[self.table_idx] # 노드 반환
                
            tmp = self.node
            self.node =self.node.next   # 밑의 if의 else부분을 위로 뺌.
            
            if self.node is None:   # 더이상 탐색할 노드가 없으면
                self.table_idx += 1 # 테이블 인덱스 증가
                 
            self.iter_return_cnt += 1
            return tmp
        
    '''
        <다른 버전 1>
            if self.index == len(self.hashtable.table):    # 끝
                raise StopIteration
            else:
                node = self.hashtable.table[self.index] # self.hashtable.table은 list 타입
                if node is None : self.index += 1   # 만약에 해시테이블과 연결된 LinkedList의 노드값이 None이면, 해시테이블의 다음 인덱스로 이동
                elif node.next is None:
                    self.index += 1
                    return node
                else:
                    self.index += 1
            return node
            
        <다른 버전 2>
            if self.index == len(self.hashtable.table):    # 끝
                raise StopIteration
            else:
                node = self.hashtable.table[self.index] # self.hashtable.table은 list 타입
                if node is None : self.index += 1   # 만약에 해시테이블과 연결된 LinkedList의 노드값이 None이면, 해시테이블의 다음 인덱스로 이동
                elif node.next is None:
                    self.index += 1
            return node
       
        <또다른 코드 1>
            while self.index < len(self.hashtable.table):
                node = self.hashtable.table[self.index]  # 현재 인덱스의 노드를 가져옴

                if node is None:  # 노드가 None이면 다음 인덱스로 이동
                    self.index += 1
                elif node.next is None:  # 노드가 존재하고, 다음 노드가 없으면 현재 노드를 반환하고 다음 인덱스로 이동
                    self.index += 1
                    return node
                else:
                    self.index += 1  # 노드가 존재하고, 다음 노드가 있으면 다음 인덱스로 이동

            raise StopIteration  # 모든 인덱스를 순회한 경우
        
        <또다른 코드 2>
            if self.index == len(self.hashtable.table):    # 끝
                raise StopIteration
            else:
                node = self.hashtable.table[self.index] # self.hashtable.table은 list 타입
                self.index += 1   # 인덱스 증가
                
                if node is not None and node.next is None:
                    return node
                
                return node
        
        '''
            
