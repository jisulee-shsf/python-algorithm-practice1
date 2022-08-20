####  
## String manipulation  
#### ► [valid_palindrome_01_220809] / list  
- pop(0) & pop() 함수를 통해, input의 맨 앞 값과 마지막 값을 매칭해 palindrome 여부 판별  
- palindrome : 앞 또는 뒤로 뒤집어도 같은 말이 되는 단어 또는 문장 / e.g. "소주 만 병만 주소"  
- isalnum() : 영숫자(alphanumeric) 여부를 판별하는 함수  
- pop(0) : list 요소의 맨 앞 값을 가져오며, 해당 값은 list 내 삭제  
- pop() : list 요소의 마지막 값을 가져오며, 해당 값은 list 내 삭제  
####  
#### ► [valid_palindrome_02_220810] / slicing  
- 기존 문자열과 slicing으로 역순한 문자열을 비교하여 palindrome 여부 판별  
- slicing : 내부적으로 C로 구현되어 있어 매우 빠른 속도로 처리 진행 / 대부분의 문자열 작업은 slicing 처리가 가장 빠름  
- re.sub('[^a-z0-9]', '', s) : 정규식으로 영숫자 외 불필요 문자 필터링  
- s[::-1] : 기존 문자열을 역순으로 변경  
####  
#### ► [reorder_data_in_log_files_220814] / lambda expression  
- 별도 함수 선언 없이 하나의 식으로 함수를 표현할 수 있는 lambda expression을 활용해 식별자 외 문자열을 키로 input 순서 정렬  
- letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) : 식별자 외 문자열[1:] 정렬 / 문자열이 동일한 경우, 후순위 식별자[0]로 정렬  
####  
#### ► [most_common_word_220814] / list comprehension  
- 단어 수를 카운팅하는 Counter 클래스와 최빈값을 리턴하는 most_common() 함수를 사용해 가장 흔한 단어를 추출  
- re.sub(r'[^\w]', ' ', paragraph) : '\w'는 단어 문자(word character)를 의미하며, 단어 문자 외 모든 문자는 공백으로 치환  
- collections.Counter() : hashable한 객체의 수를 카운팅하는 딕셔너리의 서브 클래스  
- counts.most_common(1)[0][0] : 최빈 단어의 첫번째 값을 리턴한 뒤, [0][0]로 첫 번째 인덱스 키 추출  
<img src="https://user-images.githubusercontent.com/109773795/184552333-90075e05-7666-4cb8-abac-4d12a104281d.png" width="600" height="120"/>  
<img src="https://user-images.githubusercontent.com/109773795/184552334-e1648472-9668-417f-a0b9-de62f2448464.png" width="800" height="90"/>  

#### ► [longest_palindromic_substring_220814] / two pointers  
- two pointer가 input을 슬라이딩 윈도우처럼 조회할 때, palindrome을 판별할 경우 중앙을 중심으로 pointer를 확장해 가장 긴 값을 저장  
- input 길이가 two pointers 조회에 적합지 않거나 문자열 역순이 이미 palindrome일 경우를 사전 예외 처리하여 풀이 속도를 향상 시킴  
####  
#### ► [submissions]  
<img width="942" alt="image" src="https://user-images.githubusercontent.com/109773795/184543800-473203d3-c02b-4889-b30c-6150d031ce0f.png">  
