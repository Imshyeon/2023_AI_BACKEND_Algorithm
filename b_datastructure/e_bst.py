from d_queue import *

# 이진탐색트리
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def __str__(self):
        return self.data
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        node = Node(data)
        if self.root is None:   # 데이터가 하나도 안들어왔다면
            self.root = node
            return
        
        # root가 None이 아니라면
        link = self.root
        
        while True:
            if data <= link.data :  # 왼쪽 노드
                if link.left_child is None: # 왼쪽 노드에 어떤 데이터가 차있지 않다면
                    link.left_child = node
                    break
                link = link.left_child  # 왼쪽 노드에 어떤 데이터가 차있다면
            else :  # 오른쪽 노드
                if link.right_child is None:
                    link.right_child = node
                    break
                link = link.right_child
               
                
    def find(self,data):
        link = self.root
        
        while True:
            if self.root is None : return False # root 노드가 None
            elif link.data == data : return True    # data 찾았으면
            elif data < link.data : link = link.left_child  # 내가 찾고자하는 데이터가 현재 노드의 데이터보다 작다면 왼쪽 노드로 이동
            else : link = link.right_child  # 내가 찾고자하는 데이터가 현재 노드의 데이터보다 작다면 오른쪽 노드로 이동
        
     
    # 깊이 우선 탐색 (전위, 중위, 후위 탐색)
    def dfs(self, type):
        type_dict = {'inorder' : self.__in_order,
                     'preorder' : self.__pre_order,
                     'postorder' : self.__post_order}
        return type_dict.get(type)(self.root)
    
    def __in_order(self, link):
        res = []
        #참고 : 재귀함수를 사용하기 때문에 res에서 처음 들어가는 요소는 가장 밑에 있는 애가 들어오게 될 것임
        if link.left_child is not None: # 왼쪽 탐색
            res += self.__in_order(link.left_child) # 재귀 : link.left_child가 노드가 됨! 그래서 또 탐색을 하게..
        
        if link is not None:    # 현재 위치에 데이터가 있다면, 데이터를 담아준다. 
            res += [link.data]
        
        if link.right_child is not None:
            res += self.__in_order(link.right_child)
        
        return res
    
    def __pre_order(self,link):
        res = []
        #현재 노드 출력
        if link is not None:
            res += [link.data]
        #왼쪽 노드 방문
        if link.left_child is not None:
            res += self.__pre_order(link.left_child)
        #오른쪽 노드 방문
        if link.right_child is not None:
            res += self.__pre_order(link.right_child)
        return res
        
    def __post_order(self,link):
        res = []
        # 왼쪽 노드 방문
        if link.left_child is not None:
            res += self.__post_order(link.left_child)
        # 오른쪽 노드 방문
        if link.right_child is not None:
            res += self.__post_order(link.right_child)
        # 현재 노드 출력
        if link is not None:
            res += [link.data]
        return res
    
    
    # 너비우선탐색 BFS
    
    def bfs(self):
        queue = Queue()
        queue.enqueue(self.root)
        level = 0   # depth level
        
        while not queue.is_empty() : # queue가 안빌때까지
            print(f'level {level} : ',end=' ')
            length = len(queue)
            
            for i in range(length):
                node = queue.dequeue()
                print(node.data, end='  ')
                
                if node.left_child is not None:
                    queue.enqueue(node.left_child)
                    
                if node.right_child is not None:
                    queue.enqueue(node.right_child)
                    
            print()
            level += 1