# 매개변수로 금액을 전달하면 해당 금액을 최소한의 동전개수로 구할수 있는 동전의 조합을 구하는함수
# 동전 종류 : 500, 100, 50, 10, 1
def coin_combi1(change): # 나
    
    coin = {500 : [], 
            100 : [], 
            50 : [], 
            10 : [], 
            1 : []}
    
    print(coin.keys())
    
    while change != 0:
        for i in coin.keys():
            if change % i >= 0:
                j = change % i
                k = change // i
                coin.get(i).append(k)
                change = j
        
    print(coin)

coin_combi1(3465)   #결과 : {500 : 6, 100 : 4, 50 : 1, 10 : 1, 1 : 5}


def coin_combi(change): # 풀이
    coins = {500 : 0,
             100 : 0,
             50 : 0,
             10 : 0,
             1 : 0}
    
    for coin in coins:
        coins[coin] = change // coin
        change %= coin
    print(coins)
    
coin_combi(4780)
