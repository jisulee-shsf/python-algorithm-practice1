####  
## Linked list  
#### ► [01_palindrome_linked_list_01_220824] / list  
- linked list를 python list로 변환하여 pop(0) & pop()을 활용해 인덱스 지정 비교 후 palindrome 여부 판별  
- 동적 배열로 구성된 list는 pop(0)에서 매우 느린 속도(2860ms)로 아이템을 추출하므로, 다른 최적화 풀이 방식을 고려하는 것이 적절함  
####  
#### ► [02_palindrome_linked_list_02_220825] / deque  
- 이중 연결 리스트 구조인 deque 자료형을 활용해 popleft() & pop() 인덱스 지정 비교 후 palindrome 여부 판별  
- pop()은 O(n)이나 popleft()는 O(1)으로, deque 자료형 선언만으로 기존 대비 매우 빠른 속도(1037ms)로 풀이 가능 확인  
#### ► [03_palindrome_linked_list_03_220826] / runner  
- runner 기법의 fast & slow runner를 출발시켜, 역순 linked list인 rev와 slow runner의 나머지를 비교 후 palindrome 여부 판별  
- runner : linked list를 순회할 경우, 2개의 pointer를 동시에 사용해 병합 지점 / 중간 위치 / 길이 등을 판별할 때 유용하게 사용되는 방법
##  
#### ► [submissions]  
<img width="941" alt="image" src="https://user-images.githubusercontent.com/109773795/187320269-6da12533-71aa-471f-a436-8d7aaa3f334b.png">
