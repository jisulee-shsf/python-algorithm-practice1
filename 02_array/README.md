####  
### Array
<img src="https://user-images.githubusercontent.com/109773795/184686533-a9bfff10-551b-4be8-b611-91adbbddd488.png" width="900" height="140"/>  

##
#### ► [two_sum_03_220816](https://leetcode.com/problems/two-sum/) / one loop
- 2개의 for문을 사용한 two loops 방식을 하나의 for문으로 합쳐 문제 처리 방식을 개선
- 모든 input을 딕셔너리로 저장하지 않고 정답을 찾을 시 함수를 빠져나올 수 있으나, 두 번째 값을 찾는 비교 작업으로 풀이 속도에 큰 향상은 없음
####  
#### ► [two_sum_02_220816](https://leetcode.com/problems/two-sum/) / two loops
- target에서 input 첫 번째 수를 빼면 합쳐서 target이 되는 두 번째 수를 알 수 있으므로, 딕셔너리 키 조회 방식을 활용해 정답 인덱스 추출
- 해시 테이블로 구현된 딕셔너리를 조회할 경우 평균 O(1)의 시간 복잡도를 나타내며, brute-force 방식에 비해 풀이 속도가 매우 향상됨
####
#### ► [two_sum_01_220815](https://leetcode.com/problems/two-sum/) / brute-force
- 배열을 2번 반복해 가능한 모든 조합을 더한 뒤, 정답을 찾을 때까지 확인하는 무차별 대입의 brute-force 방식 진행  
- brute-force search : 솔루션에 대해 가능한 모든 후보를 열거하고, 각 후보가 문제의 설명을 충족하는지 확인하는 문제 해결 기술 및 알고리즘  
- 문제 해결 여부와 별도로, 지나치게 느린 속도(6558ms)로 인해 다른 최적화 풀이 방식을 고려하는 것이 적절함  
####  
