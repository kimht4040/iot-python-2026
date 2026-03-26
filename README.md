# iot-python-2026
파이썬 학습 리포지토리

- 참고자료 : https://wikidocs.net/book/18202


## 1일차


### 사전정리

기본 문법,
- 변수, 데이터형
- 제어문
  - 조건문
  - 반복문
- 함수/메서드
- 배열
- 포인터/참조
- 구조체/클래스
- 파일 입출력
- 예외처리

### 이론적 개념 정리
#### 파이썬에 신경 안써도 되는 것
- 학습 난이도를 낮추는 목록
  - 자료형 선언 안함
  - 세미콜론 없음
  - 중괄호 없음 - 들여쓰기 해야함
  - main함수 생성 강제 아님
  - 메모리 할당 해제 거의 안함 - 가비지 컬렉터가 자동으로
  - 헤더 파일 개념 없음
  - 컴파일 과정 신경 거의 안씀
  - 개발환경 설정 어렵지 않다
- 문법 비교표

| 항목 | C++ | Python |
| :--- | :--- | :--- |
| **기본 구조** | 중괄호 `{ }`, 세미콜론 `;` 필수 | 들여쓰기(Indentation), 줄바꿈 구분 |
| **변수 선언** | `int x = 10;` (정적 타이핑) | `x = 10` (동적 타이핑) |
| **출력** | `std::cout << "Hello";` | `print("Hello")` |
| **조건문** | `if (x > 0) { ... }` | `if x > 0:` |
| **반복문 (For)** | `for (int i=0; i<10; i++)` | `for i in range(10):` |
| **함수 정의** | `int func(int a) { return a; }` | `def func(a): return a` |
| **배열/리스트** | `std::vector<int> v;` | `v = [1, 2, 3]` |
| **불리언** | `true`, `false` | `True`, `False` |
| **메모리 관리** | 수동 (Smart Pointer 권장) | 자동 (Garbage Collection) |



### 환경설정
- 미니 콘다 설치
- 주피터 설치
- 가상환경 활성화
- 파이썬 설치
- opencv 설치
- 파이토치 설치
- 주피터 랩 실행
- 테스트




#### 가상환경 주의점
- 파이토치 사용시 PyTorch가 내부적으로 사용하는 OpenMP 라이브러리와 시스템의 다른 라이브러리가 충돌하면서 발생하는 전형적인 문제발생 
- import os
- os.environ['KMP_DUPLICATE_LIB_OK'] = 'True' 파일 최상단에 삽입하여
- 오류 무시



### 파이썬 기본 학습
1. 기본입출력[text](day1/ex01_output.py)
   - py 파일 작성
   - ctrl + f5 실행
   - 디버거 선택
2. 리스트[text](day1/ex02_array.py)
- 어떤 데이터 타입도 추가 가능
- append ~ sort까지 11개 함수만 학습

3. 제어문[text](day1/ex03_logic_control.py)
   - if, for
   - switch-case 많음