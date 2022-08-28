####  
## Linked list  
#### ► [01_palindrome_linked_list_01_220824] / list  
- linked list를 python list로 변환하여 pop(0) & pop()을 활용해 인덱스 지정 비교 후 palindrome 여부 판별  
- 동적 배열로 구성된 list는 pop(0)에서 매우 느린 속도(2860ms)로 아이템을 추출하므로, 다른 최적화 풀이 방식을 고려하는 것이 적절함  
####  
#### ► [02_palindrome_linked_list_02_220825] / Deque  
- 이중 연결 리스트 구조인 deque 자료형을 활용해 popleft() q.pop() 인덱스 지정 비교 후 palindrome 여부 판별  
#### ► [03_palindrome_linked_list_03_220826] / Runner  
- runner 기법의 fast & slow runner를 출발시켜 linked list인 rev와 slow runner의 나머지를 비교 후 palindrome 여부 판별  
##  
