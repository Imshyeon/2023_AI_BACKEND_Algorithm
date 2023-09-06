# 한 개의 회의실이 있다.
# 이를 사용하고자 하는 n개의 회의들에 대해 회의실 사용표를 만들려고 한다.
# 각 각 회의 i에 대해 시작시간과 끝나는 시간이 주어져있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라.
# 단, 회의는 한번 시작하면 중간에 중단될 수 없고 한 회의가 끝나는 것과 동시에 다음 회의 시작될 수 있다.

# 나
def schedule_meeting(meetings):
    min = meetings[0]['end'] - meetings[0]['start']
    
    scheduled = []
    day=[]
    day+=[i for i in range(0,25)]
    cnt = 0
    while cnt != 24:
        for i in meetings:
            start = i['start']
            end = i['end']
            
            if end - start < min:
                min = end - start
                scheduled.append(i)
                for j in range(start, end+1):
                    if j in day:
                        day.remove(j)
                        
            if start in day and end in day:                    
                for j in range(len(scheduled)):
                    if scheduled[j]['end'] <= start and start < scheduled[j]['end']+scheduled[j]['start']:
                        scheduled.append(i)
                        for k in range(start, end):
                            if k in day:
                                day.remove(k) 
        cnt += 1
        
    print(scheduled)        


#====================================================

# 풀이
# hint : 최대한 많은 회의가 열리려면, end가 최대한 빨리 끝나는 애들이 배정. 그 다음에 시작시간이 이전의 끝나는 시간보다 크거나 같은.. 그들 중 가장 빠른 애들
# dict를 end 기준으로 정렬
def schedule_meeting2(meetings):
    res = []
    sorted_meetings = sorted(meetings, key=lambda e : e['end'])  # end시간이 가장 작은 것부터.  <lambda 인자 : 표현식 > : 함수에 전달되는 매개변수, 람다함수가 실행될 때 반환할 식
    # print(sorted_meetings)
    res.append(sorted_meetings[0])
    
    for e in sorted_meetings[1:]:
        if res[-1]['end'] <= e['start']:
            res.append(e)
            
    print(res)
    
 
meetings = [
      {'idx':1,'start':1, 'end':10} #9
     ,{'idx':2,'start':5, 'end':6}  #1  -> 1
     ,{'idx':3,'start':13,'end':15} #2
     ,{'idx':4,'start':14,'end':17} #3  -> 3
     ,{'idx':5,'start':8, 'end':14} #6  -> 2
     ,{'idx':6,'start':3, 'end':12} #9
     ]


# schedule_meeting(meetings)   # 2 - 5 - 4 회의

schedule_meeting2(meetings) 