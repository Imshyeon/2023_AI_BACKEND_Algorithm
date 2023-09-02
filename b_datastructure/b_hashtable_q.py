from b_hashtable import *

def find_uniq_char(text):
    '''
    # 나
    
    table = HashTable()
    table.add(text,text) # 추가
    for i in table:
        charlist=[]
        result=[]
        for n in range(0,len(i.data)):
            # flag=0
            if i.data[n] in charlist and i.data[n] not in result:
            #    flag+=1
                result.append(i.data[n])
            charlist.append(i.data[n])
            # if flag != 0 :
                # result.append(i.data[n])
        return result
    '''
    # 강사 -> 이게 더 좋은 코드로 보인다.
    hashtable = HashTable()
    for ch in text:
        if ch not in hashtable:
            hashtable.add(ch, 1)
        else:   #이미 해시테이블에 존재한다면
            cnt = hashtable.get(ch) # 중복된 값이라면 키 값을 받아와서
            hashtable.set(ch,cnt+1) # cnt만 중복
    
    res = []
    max = 1
    
    for e in hashtable:
        if max < e.data: max = e.data
    for e in hashtable:
        if max == e.data : res.append(e.key)  
    
    return res      
    