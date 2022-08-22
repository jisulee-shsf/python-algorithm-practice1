####  
## Array
#### ► [01_two_sum_01_220815] / brute-force
- 배열을 2번 반복해 가능한 모든 조합을 더한 뒤, 정답을 찾을 때까지 확인하는 무차별 대입의 brute-force 방식 진행  
- brute-force search : 솔루션에 대해 가능한 모든 후보를 열거하고, 각 후보가 문제의 설명을 충족하는지 확인하는 문제 해결 기술 및 알고리즘  
- 문제 해결 여부와 별도로, 지나치게 느린 속도(6558ms)로 인해 다른 최적화 풀이 방식을 고려하는 것이 적절함  
####  
#### ► [02_two_sum_02_220816] / two loops
- target에서 input 첫 번째 수를 빼면 합쳐서 target이 되는 두 번째 수를 알 수 있으므로, 딕셔너리 키 조회 방식을 활용해 정답 인덱스 추출
- 해시 테이블로 구현된 딕셔너리를 조회할 경우 평균 O(1)의 시간 복잡도를 나타내며, brute-force 방식에 비해 풀이 속도가 매우 향상됨
####  
#### ► [03_two_sum_03_220816] / one loop
- 2개의 for문을 사용한 two loops 방식을 하나의 for문으로 합쳐 문제 처리 방식을 개선
- 모든 input을 딕셔너리로 저장하지 않고 정답을 찾을 시 함수를 빠져나올 수 있으나, 두 번째 값을 찾는 비교 작업으로 풀이 속도에 큰 향상은 없음  
##  
#### ► [04_3sum_01_220816] / brute-force & [05_3sum_02_220817] / two pointers
- 04_3sum_01_220816 : brute-force 방식 진행으로 인해, time limit exceeded 발생
- 05_3sum_02_220817 : sum이 0인 경우에 대한 스킵 처리를 하지 않아 test case '[-2,0,0,2,2]'에서 wrong answer 발생
####  
#### ► [06_3sum_03_220817] / two pointers  
- left & right two pointers를 설정해 sum의 합을 조절하며 sum이 0이 되는 3개의 elements 추출  
- two pointers를 사용하기 위해 sort() 함수로 배열을 간소화한 뒤 풀이 진행  
- sum이 0보다 작으면 left pointer를 우측으로 이동하고, 0보다 크면 right pointer를 좌측으로 이동하여 값 확인  
- sum이 0인 경우, left & right 각 pointer 양옆에 동일한 값이 있을 수 있으므로 중복을 제거하기 위한 스킵 처리 조건 설정  
##  
#### ► [07_array_partition_01_220819] / ascending order  
- n개 pair의 min(a, b) 합이 가장 큰 수를 찾기 위해, 정렬된 2n 배열의 len(pair)가 2인 경우의 min 값을 추출  
- 오름차순 또는 내림차순으로 정렬된 배열의 인접 요소를 페어로 만들 경우, 최대 합을 구할 수 있음 / e.g. min(1, 2) + min(3, 4) = 4  
####  
#### ► [08_array_partition_02_220819] / even order 
- 2n 배열을 정렬할 경우, 짝수 번째 index에 항상 min 값이 존재함을 활용해 코드를 간결하게 구현
- e.g. nums = [1, 2, 3, 4] > min(1, 2) + min(3, 4) = nums[0] + nums[2]
####  
#### ► [09_array_partition_03_220819] / pythonic way
- 08_array_partition_02_220819 구현 방식을 python slicing의 pythonic 방법을 통해 코드를 더욱 간결하게 구현
- sum(sorted(nums)[::2]) : 정렬된 nums를 처음부터 끝까지 2칸씩 우측으로 이동하며 각 값을 합산
##  
#### ► [10_best_time_to_buy_n_sell_stock_220821] / replace maximum value  
- 현재 값이 우측으로 이동하며 이전 min_price와의 차이를 계산한 값이 기존 profit보다 클 경우, 최댓값으로 교체하는 방식 진행
- sys를 활용해 -sys.minsize & sys.maxsize를 사전 설정하나, 입력값이 []인 경우를 대비해 -sys.minsize를 0으로 대체
##   
#### ► [submissions]  
<img width="942" alt="image" src="https://user-images.githubusercontent.com/109773795/185763381-84327ff0-25e6-4598-8cb3-e50d46e05250.png">  
