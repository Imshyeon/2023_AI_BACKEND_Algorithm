# n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
# 단, 수는 한 개 이상 선택해야 한다.

#       0   1   2   3   4   5   6   7   8   9
# arr  10  -4   3   1   5   6  -35  12  21  -1
# sum  10   6   9   10  15  21 -14  12  33  32  <- 여기에 부분합 저장 arr[i] + sum[i-1] => 얘가 arr[i]보다 크면 더한 값이 sum값이 되고, 작으면 arr[i]

# => 부분합 max: 33 (7번과 8번을 더한 값)

def sub_sum(arr):
    # sub = []
    # sub.append(10)
    # for i in range(1,len(arr)):
    #     j=arr[i]+sub[i-1]
    #     if j > arr[i]:
    #         sub.append(j)
    #     else: sub.append(arr[i])
    
    # return max(sub)
    sub=[]
    sub.append(10)
    
    for i in range(1,len(arr)):
        j = arr[i]+sub[i-1]
            
        if j > arr[i]:
            sub.append(arr[i] + sub[i-1])
        else:
            sub.append(arr[i])
        
    return max(sub)
    

print(sub_sum([10,-4,3,1,5,6,-35,12,21,-1]))


# 풀이
def sub_sum2(arr):
    sum_arr = [arr[0]]
    
    for e in arr[1:]:
        sum_arr.append(max(sum_arr[-1]+e, e))   # 둘 중에 큰 값이 담김
    
    return max(sum_arr)
    
print(sub_sum2([10,-4,3,1,5,6,-35,12,21,-1]))