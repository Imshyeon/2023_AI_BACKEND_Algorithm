# 알고리즘
1. 알고리즘 : 문제를 해결하기 위한 것, 명확하게 정의되고 순사가 있는 유한개의 규칙으로 이루어진 집합
- 하나의 문제에 대해 여러 접근 방법을 고려할 수 있는 힘과 단순히 실행되는 코드가 아닌 더 잘 실행되는 코드를 알아가는 능력을 알 수 있다.

2. Big O 표기법

    ![Big_O](https://images.velog.io/images/gillog/post/1506c01a-ba40-4255-b549-03c8bb038049/1.png)


## a_basic
1. [a_condition](https://github.com/Imshyeon/Algorithm/blob/main/a_basic/a_condition.py) : 최대, 최소, 중간값 구하기
2. [b_loop](https://github.com/Imshyeon/Algorithm/blob/main/a_basic/b_loop.py) : 덧셈, 다이아몬드 별 찍기
3. [c_math](https://github.com/Imshyeon/Algorithm/blob/main/a_basic/c_math.py) : 소수 판별, 최대공약수, 최소공배수, 팩토리얼, 피보나치 수열

<br>

## b_datastructure
1. [a_list](https://github.com/Imshyeon/Algorithm/blob/main/b_datastructure/a_list.py) : Linked List 구현
    - [a_list_q](https://github.com/Imshyeon/Algorithm/blob/main/b_datastructure/a_list_q.py) : 앞에서 구현한 Linked List를 이용해 문제풀기
        - 자연수 배열에서 가장 큰 수 찾기
        - 자연수 배열에서 가장 큰 두 수를 찾아 배열로 반환하기
        - 회문검사

2. [b_hashtable](https://github.com/Imshyeon/Algorithm/blob/main/b_datastructure/b_hashtable.py) : HashTable 구현
    - [b_hashtable_q](https://github.com/Imshyeon/Algorithm/blob/main/b_datastructure/b_hashtable_q.py) : 앞에서 구현한 Hash Table를 이용해 문제풀기
    
3. [c_stack](https://github.com/Imshyeon/Algorithm/blob/main/b_datastructure/c_stack.py) : Stack 구현
    - [c_stack_q](https://github.com/Imshyeon/Algorithm/blob/main/b_datastructure/c_stack_q.py) : 앞에서 구현한 Stack를 이용해 문제풀기
        - 괄호 문제
        
4. [d_queue](https://github.com/Imshyeon/Algorithm/blob/main/b_datastructure/d_queue.py) : Queue 구현
    - [d_queue_q](https://github.com/Imshyeon/Algorithm/blob/main/b_datastructure/d_queue_q.py) : : 앞에서 구현한 Queue를 이용해 문제풀기
        - 카드 문제
        - 요세푸스 순열 문제

5. [e_bst](https://github.com/Imshyeon/Algorithm/blob/main/b_datastructure/e_bst.py) : 이진탐색트리 구현

<br>

## c_search
1. [a_linea](https://github.com/Imshyeon/Algorithm/blob/main/c_search/a_linear.py) : 선형 검색
2. [b_binary](https://github.com/Imshyeon/Algorithm/blob/main/c_search/b_binary.py) : 이진 검색

## d_brute_force
1. [a_bubble_sort](https://github.com/Imshyeon/Algorithm/blob/main/d_brute_force/a_bubble_sort.py) : 버블 정렬
2. [b_selection_sort](https://github.com/Imshyeon/Algorithm/blob/main/d_brute_force/b_selection_sort.py) : 선택 정렬
3. [c_brute_force_q](https://github.com/Imshyeon/Algorithm/blob/main/d_brute_force/c_brute_force_q.py) : brute force를 이용한 문제 풀기
    - 종말
    - 일곱난쟁이

## e_devide_conqure
1. [a_merge_sort](https://github.com/Imshyeon/Algorithm/blob/main/e_devide_conqure/a_merge_sort.py), [a_merge_sort2](https://github.com/Imshyeon/Algorithm/blob/main/e_devide_conqure/a_merge_sort2.py) : merge sort
2. [b_quick_sort](https://github.com/Imshyeon/Algorithm/blob/main/e_devide_conqure/b_quick_sort.py), [b_quick_sort2](https://github.com/Imshyeon/Algorithm/blob/main/e_devide_conqure/b_quick_sort2.py) : quick sort
3. [c_devide_conqure_q](https://github.com/Imshyeon/Algorithm/blob/main/e_devide_conqure/c_devide_conqure_q.py) : 분할정복을 이용한 문제 풀기
    - 거듭제곱 최적화

## f_greedy
1. [a_coin_q](https://github.com/Imshyeon/Algorithm/blob/main/f_greedy/a_coin_q.py) : 탐욕법을 이용한 코인 문제
2. [b_meeting](https://github.com/Imshyeon/Algorithm/blob/main/f_greedy/b_meeting.py) : 탐욕법을 이용한 회의 시간 잡기 문제

## g_dynamic_programming
1. [a_fibo_dp](https://github.com/Imshyeon/Algorithm/blob/main/g_dynamic_programming/a_fibo_dp.py) : a_basic에 있던 피보나치 수열을 가지고 와서 dynamic programming으로 구현하기
2. [b_sum_dp](https://github.com/Imshyeon/Algorithm/blob/main/g_dynamic_programming/b_sum_dp.py) : dynamic programming을 이용해서 수열의 부분합 문제 풀기