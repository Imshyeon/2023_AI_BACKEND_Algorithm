from d_queue import *

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
    print(queue)
    
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
            print(queue)
        else:
            no.append(queue.dequeue())
            cnt += 1  
    result.append(queue.dequeue())     
    result = result + no        
    return result

print(queue_card(4))
print(queue2(7,3))