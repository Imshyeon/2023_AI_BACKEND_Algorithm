from d_queue import *
#제일 위 있는 카드를 바닥에 버리고, 그 다음 제일 위에 있는 카드를 제일 밑으로 옮긴다. 버린 카드들을 순서대로 출력
def queue_card(card):
    queue = Queue()
    result = []

    # 카드 초기화
    for c in range(1, card + 1):
        queue.enqueue(c)

    while len(queue) > 1:
        # 제일 위에 있는 카드를 버리고, 그 다음 카드를 맨 아래로 옮김
        discarded_card = queue.dequeue()
        moved_card = queue.dequeue()
        queue.enqueue(moved_card)
        result.append(discarded_card)

    # 마지막에 남은 카드를 결과 리스트에 추가
    result.append(queue.dequeue())

    return result

#------
def queue2(n ,k):
    queue = Queue()
    if k > n : return None
    for i in range(1,n+1):
        queue.enqueue(i)
    # print(queue)
    
    no=[]
    result=[]
    cnt = 1
    while len(queue) > 1:
        if cnt == k:
            result.append(queue.dequeue())
            for j in range(len(no)):
                queue.enqueue(no[j])
            no=[] 
            cnt = 1
            # print(queue)
        else:
            no.append(queue.dequeue())
            cnt += 1  
    result.append(queue.dequeue())     
    result = result + no        
    return result

print('1번 문제 : ', queue_card(4))
print('2번 문제 : ', queue2(7,3))



#========1번 풀이=======
def queue_card_ans(n):
    trash = Queue()
    cards = Queue()
    
    for i in range(1, n+1):
        cards.enqueue(i)
        
    while len(cards) > 1:
        t1 = cards.dequeue()    # 제일 위에 있는 카드를 버려서 trash에 삽입
        trash.enqueue(t1)
        t2 = cards.dequeue()    # 그 다음에 있는 카드를 카드의 마지막에 넣는다.
        cards.enqueue(t2)
    
    print(trash,end='')
    print(f', {cards}') #마지막 남은 한 장 출력
    
queue_card_ans(4)


#========2번 풀이=======
# 요세푸스 순열 문제 : 1번부터 n번까지 n명의 사람이 원을 이루면서 앉아있고, 양의 정수 k(<=n)이 주어진다.
# 1번부터 n번 사람이 있는 방향으로 k번째 사람을 순차적으로 제거
# 모든 사람이 제거되었을 때, 제거되는 사람의 순서를 담은 배열을 반환하시오.

def josephus(n, k):
    q = Queue()
    dead = []
    
    for i in range(1, n+1):
        q.enqueue(i)

    while not q.is_empty(): # q가 비어있지 않다면
        cnt = 1
        while cnt < k:
            q.enqueue(q.dequeue())  # dead target이 아닌 애들은 빼서 뒤로 보냄
            cnt += 1
        dead.append(q.dequeue())    # dead target이 되면 제거해서 dead list에 append
        
    return dead

print(josephus(7,3))