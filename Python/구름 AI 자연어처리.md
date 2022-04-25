> 본 문서는 [코드업 기초100제 정리](Python/%EC%BD%94%EB%93%9C%EC%97%85%20%EA%B8%B0%EC%B4%88100%EC%A0%9C%20%EC%A0%95%EB%A6%AC.md) 및 [서울시 공공데이터를 활용한 데이터 분석](Python/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D.md)에 작성된 내용을 제외하고 작성되었습니다.

## 목차
* [Lecture 0 - Python Overview](#파이썬-특징)
* [Lecture 1 - Environment](#파이썬-환경)
* [Lecture 2 - Variable & Operator](#변수--연산자)
* [Lecture 3 - Data Structure](#자료구조)

### 파이썬 특징
* 플랫폼 독립적인 인터프리터 언어
* 완전 객체 지향 언어
* 동적 타이핑 언어
* 쉬운 문법 & 다양한 기능
* 다양한 라이브러리
* 널리 쓰임
* 쉽고 다양한 문법
* 매우 높은 생산성

## 파이썬 환경
* Linux 운영체제 권장
    - 서버 호환 쉬움
    - 라이브러리 설치 용이, 무료
    - 대부분의 사용자가 친숙하지 않은 편
* MAC : 서버사용이 용이하나 비쌈
* Window : 친숙함, 워드, 한컴 등 사용가능하나 특정 라이브러리 설치가 어려움

### 윈도우 유저를 위한 옵션
* 가상 환경 사용
* WSL 사용
* 클라우드 기반 서비스 사용(colab, goormide)

### IDE(Integrated Development Enviroment)
* Visual Studio Code
* PyCharm
* Web-based IDE
    - Jupyter Notebook
    - Jupyter Lab
* Cloud-based IDE
    - Google Colab (이후 강의에서 메인으로 사용 예정)
    - Goorm IDE

### Package & Environment Manager
* 설치 및 관리 자동화 도구 필요
* 다양한 환경 간 쉬운 전환 필요
* PIP + Virtual env : Python 기본 패키지 관리 프로그램
* Anaconda3 : 기계학습 및 수치해석 특화 패키지 관리 프로그램

### Jupyter
* 파이썬의 기본 실행 환경 = Interactive Shell
* Jupyter
    - Ipython 커널을 기반으로 한 interactive 파이썬 셀 프로그래밍
    - 미디어, 코드, 수식 등을 하나의 문서 형태 표현 가능
    - .ipynb 파일 확장자
    - Code Cell : 코드를 실행시키고 결과를 확인
    - Markdown Cell : 마크다운/HTML 문법으로 문서화

## 변수 & 연산자
* 파이썬 변수의 특징
    - 모든 변수는 메모리 주소를 가르킨다. (즉, 모든 것은 포인터다.)
    - 선언한 변수에 특정 공간이 생기는 개념이 아니라, 필요하면 공간을 만들고 변수명을 붙이는 격

### 변수 대입
* C와 달리 대입 연산이 반환 값을 가지지 X
* 연속해서 대입 가능 (뒤에서부터 대입)
* := 연산으로 대입과 동시에 반환 가능
```python
print((a := 2) == 2 #True
# := 연산이 아닌 = 연산을 사용하면 Error
```
### 비트연산자
* ~ : 비트 부정
* | : 비트합(or)
* & : 비트곱(and)
* ^ : 배타적 비트합(값이 같으면 0, 다르면 1)
* <<, >> : 비트 시프트

### 연산자 특징
* 산술 연산자와 비트 연산자는 대입 연산자와 함께 축약 가능
    - a+=1은 in-place 연산이고 a=a+1은 out-place 연산
    - out-place 연산은 명시적으로 새로운 객체 생성
    - in-place 연산은 기존 객체 수정 시도하고, 불가능할 시 새로운 객체 생성

### 비교연산자
* x == y / x != y : x와 y의 값이 같다/다르다
* x is y / x is not y : x와 y의 주소가 같다/다르다

### 연산자 우선순위
* 생성연산자 : 괄호
* 참조연산자 : 인덱싱, 함수 호출, 속성 참조 등
* 산술연산자 : 거듭제곱 → 단항 연산자 → 곱셈, 나눗셈 → 덧셈, 뺄셈
* 비트연선자 : 비트 시프트 → 비트곱 → 배타적 비트합 → 비트합
* 비교연산자 : 포함&비교 연산자
* 논리연산자 : 논리 부정 → 논리곱 → 논리합
* 삼항연산자 : A if 조건 else B

### 원시자료형 특징
* 원시자료형(Primitive Data Type)은 **불변타입(Immutable Type)**이다.
    - 파이썬의 모든 것은 객체이기 때문에 원시자료형들 역시 객체
    - 그러나 불변 타입들은 저장된 값이 변하지 x
    - 모든 타입은 물리적 메모리 주소를 가르킴(C에서의 pointer)
    - 원시자료형과 Tuple을 제외한 다른 모든 파이썬 객체는 가변 타입(Mutable Type)

### 불변 타입과 가변 타입
* 파이썬에서 대입은 원칙적으로 메모리 주소 복사
    - 즉, 값을 복사하지 않고 같은 주소를 공유
    - 불변형의 경우 수정이 필요하면 **새로운 객체를 생성**
    - ex)
    ```python
    a = 10 # int는 불변타입
    b = a # a와 b는 같은 메모리 주소
    a += 1 # a는 불변타입이므로 객체 새로 생성
    print(a, b, a is b) # 11 10 False 출력

    # 가변타입/in-place 예시
    a = [1,2,3] # List는 가변타입
    b = a # a와 b는 같은 메모리 주소
    a += [4] # append와 같은 기능. 가변타입이므로 객체 수정
    print(a, b, a is b) # [1,2,3,4] [1,2,3,4] True 출력
    # (b는 a와 메모리 주소가 같으므로 함께 변경됨)

    # 가변타입/out-place 예시
    a = a + [5] # a에 [5]를 추가한 객체를 새로 생성
    print(a, b, a is b) # [1,2,3,4,5] [1,2,3,4] False 출력
    - 불변타입에서는 사실상 항상 out-place

### 데이터 할당
* 파이썬에서 적당한 크기의 원시 자료형 대입은 기존 객체를 할당
    - 불변 타입이라 상관 x
    - ex)
    ```python
    a = 1
    b = 1
    print(a is b) # True 출력
    # 123456789과 같이 큰 수를 넣으면 False 출력, 짧은 텍스트와 같은 텍스트도 같음
    ```
    - bool값은 True, False뿐이므로 같은 메모리 주소 가짐
    - None도 하나의 메모리 주소
        + None 값을 비교할때는 주로 is 연산자 사용

### 암시적 형 변환(Implicit Type Conversion)
* bool → int → float → complex
* None과 str 타입은 별개

### 명시적 형 변환
* 실수를 정수로 변환할 때 소수점 내림 (즉, 0에 가까워지는 방향으로)
ex)
```python
int(75.75) # 75
int(-163.7) # -163
```
* 빈 문자열, 0, None은 False로 반환
ex)
```python
bool(None) # False
bool('False') # True, 문자열 내용과 상관없이 값이 있으므로
bool('') # False
```

### 타입 확인
* isinstance 함수로 변수가 지정 타입인지 확인
    - bool값 반환
    - isinstance(변수, 타입)

## 자료구조
### 슬라이싱(Slicing)
* ex)
```python
seq = [1,2,3,4,5,6,7,8,9,10]
seq[3:-1] # [4,5,6,7,8,9] → 앞 3번째부터 뒤 1번째 전까지
seq[-3:-1] # [8,9]
seq[-2:2:-1] # [9,8,7,6,5,4]
```

### 예약어 & 내장함수 & 메소드
* 예약어
    - 일종의 문법적인 요소
    - 괄호 사용 x
    - 재정의 불가능
    - ex) del, if, for, assert, None 등
* 내장함수
    - 기본 정의된 함수, 괄호 사용
    - 별개의 함수 사용
    - 재정의 가능
    - 편의성 향상
    - ex) len(), sum(), range(), input() 등
* 메소드
    - 객체 내에 정의된 함수
    - .method()으로 접근
    - Overriding
    - 해당 객체를 다룸
    - ex) .append(), .insert(), .extend()

### List 시간복잡도
* 빅오표기법
* l=[1,2,3]이라고 할 때, l.clear는 in-place 연산이고 l=[]는 결과는 유사하나 out-place 연산이다.

### 튜플(Tuple)
* **불변 타입 리스트**
* 문맥에 따라 괄호() 생략 가능
    - ex) t = 1,2,3,4 # t = (1,2,3,4)로 출력
* 일반적으로 함수에서 2개 이상 요소를 반환할 때 사용 (+ 딕셔너리의 키값으로도 사용)
* Tuple은 불변타입이지만, 내부 요소는 가변 타입 가능 (ex : Tuple의 요소인 List는 수정 가능)
* 문자열 타입(str)의 경우 일종의 문자 튜플로 생각 가능 → 인덱싱 및 슬라이싱 가능

### 패킹(Packing) & 언패킹(Unpacking)
```python
t = [1,2,3,4,5] # 패킹 : 여러 데이터 묶기
a, b, c, _, _ = t # 언패킹 : 묶인 데이터 풀기
                  # '_'는 관습적으로 사용하지 않는 변수 지칭
a, *b, c = t # *로 남는 요소 리스트로 묶음
print(a,b,c) # 1 [2,3,4] 5 출력
```
* 튜플에서도 마찬가지로 사용 가능

### 딕셔너리(Dictionary)
* 불변타입으로만 이루어져 있으면 key로 사용 가능
* key가 튜플일때 괄호 생략 가능

### Dictionary 시간복잡도
* 딕셔너리는 Hash로 구현 : indexing 속도가 O(1)
* Delete, Clear : O(1)
    - d.clear : s = {} or dict()와 유사
        + in-place

### Set
* 딕셔너리의 key만 모여있는 형태 → 집합형
* 선언 : {} 또는 set()
    - 빈 중괄호는 빈 딕셔너리로 인식
```python
s = set([1,2,3,])
s.add(4) # 요소 추가
s.add('text') # 중복된 요소는 추가 x
print(s) # {1,2,3,4,'text'} 출략

s.remove(2) # 요소 삭제
s.remove(99) # 존재하지 않는 요소 삭제는 error
s.discard(99) # 요소 삭제, 존재하지 않을 경우 무시
s.update([1,99,None,True])
print(s) # {1, None,3,4,99,'text} 출력
         # True는 1과 중복이므로 출력 x
```
* 수학적 집합 연산자가 존재
```python
s1 = set([1,2,3,4])
s2 = set([3,4,5,6])
s1 & s2 # {3,4} 교집합
s1 | s2 # {1,2,3,4,5,6} 합집합
s1 - s2 # {1,2} 차집합
s1 ^ s2 # {1,2,5,6} 배타적 합집합
```

### Frozenset
* 불변 타입의 set
* 딕셔너리의 key 값으로 사용 가능(set은 불가)
