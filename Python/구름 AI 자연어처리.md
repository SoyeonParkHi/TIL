> 본 문서는 [코드업 기초100제 정리](Python/%EC%BD%94%EB%93%9C%EC%97%85%20%EA%B8%B0%EC%B4%88100%EC%A0%9C%20%EC%A0%95%EB%A6%AC.md) 및 [서울시 공공데이터를 활용한 데이터 분석](Python/%EC%84%9C%EC%9A%B8%EC%8B%9C%20%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%A5%BC%20%ED%99%9C%EC%9A%A9%ED%95%9C%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D.md)에 작성된 내용을 제외하고 작성되었습니다.

## 목차
* [Lecture 0 - Python Overview](#파이썬-특징)
* [Lecture 1 - Environment](#파이썬-환경)
* [Lecture 2 - Variable & Operator](#변수--연산자)
* [Lecture 3 - Data Structure](#자료구조)
* [Lecture 4 - Condition & Loop](#조건문--반복문)
* [Lecture 5 - Function](#함수)
* [Lecture 6 - Pythonic Programming](#파이써닉한-프로그래밍)
* [Lecture 7 - Object-Oriented Programming](#객체-지향-프로그래밍)
* [Lecture 8 - Module & Package](#모듈--패키지)

### 파이썬 특징
* 플랫폼 독립적인 인터프리터 언어
    - OS와 상관없이 인터프리터만 있으면 실행 가능
* 완전 객체 지향 언어 : 모든 것이 객체
* 동적 타이핑 언어 : 덕 타이핑(Duck Typing)
* 쉬운 문법 & 다양한 기능
* 다양한 라이브러리
* 널리 쓰임
* 매우 높은 생산성

## 파이썬 환경
### OS
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
    - Ipython 커널을 기반으로 한 **interactive** 파이썬 셀 프로그래밍
    - 미디어, 코드, 수식 등을 하나의 문서 형태로 표현 가능
    - .ipynb 파일 확장자
    - Code Cell : 코드를 실행시키고 결과를 확인
    - Markdown Cell : 마크다운/HTML 문법으로 문서화

## 변수 & 연산자
* 파이썬 변수의 특징
    - 모든 변수는 메모리 주소를 가르킨다. (즉, 모든 것은 포인터다.)
    - 선언한 변수에 특정 공간이 생기는 개념이 아니라, 필요하면 공간을 만들고 변수명을 붙이는 격

### 변수 대입(Assigning Variables)
* C와 달리 대입 연산이 반환 값을 가지지 X
    - ex) `(a = 2) == 2`를 실행하면 error
        + (a = 2)의 대입 연산이 반환 값을 가지지 않으므로
* 연속해서 대입 가능 (뒤에서부터 대입)
    - ex) `a = b = 10`
* := 연산으로 대입과 동시에 반환 가능
```python
print((a := 2) == 2 #True
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
* 주소가 같으면 값은 당연히 같지만, 값이 같다고 해서 주소가 같은 것은 x

### 연산자 우선순위
* 생성연산자 : 괄호
* 참조연산자 : 인덱싱, 함수 호출, 속성 참조 등
* 산술연산자 : 거듭제곱 → 단항 연산자(+x,-x,~x) → 곱셈, 나눗셈 → 덧셈, 뺄셈
* 비트연선자 : 비트 시프트 → 비트곱 → 배타적 비트합 → 비트합
* 비교연산자 : 포함&비교 연산자
* 논리연산자 : 논리 부정 → 논리곱 → 논리합
* 삼항연산자 : A if 조건 else B

### 원시자료형 특징
* 원시자료형(Primitive Data Type)은 **불변타입(Immutable Type)** 이다.
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
    - 불변 타입이라 어차피 out-place 연산을 해야하므로 상관 x
    - ex)
    ```python
    a = 1
    b = 1
    print(a is b) # True 출력 = a와 b는 같은 주소 공유
    # 123456789과 같이 큰 수를 넣으면 False 출력, 짧은 텍스트와 같은 텍스트도 같음
    ```
    - bool값은 True, False뿐이므로 같은 메모리 주소 가짐
    - None도 하나의 메모리 주소
        + None 값을 비교할때는 주로 is 연산자 사용

### 명시적 형 변환(Explicit Type Conversion)
* [Type](value) 
    - `int(a)`, `str(1234)`
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
* type 함수
* isinstance 함수로 변수가 지정 타입인지 확인
    - isinstance(변수, 타입)
    - bool값 반환


## 자료구조
### 리스트 슬라이싱(List Slicing)
* ex)
```python
seq = [1,2,3,4,5,6,7,8,9,10]
seq[3:-1] # [4,5,6,7,8,9] → 앞 3번째부터 뒤 1번째 전까지
seq[-3:-1] # [8,9]
seq[-2:2:-1] # [9,8,7,6,5,4], step이 역수일때는 뒤에서 시작
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
    - Overriding 가능
    - 해당 객체를 다룸
    - ex) .append(), .insert(), .extend()

### List 시간복잡도
* 빅오표기법
![Alt text](/Python/List-Big(O).png)

* l=[1,2,3]이라고 할 때, l.clear는 in-place 연산이고 l=[]는 결과는 유사하나 out-place 연산이다.

### 튜플(Tuple)
* **불변 타입 리스트**
* 문맥에 따라 괄호() 생략 가능
    - ex) `t = 1,2,3,4` => t = (1,2,3,4)  출력
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

### Dictionary 시간복잡도
![Alt text](/Python/Dict-Big(O).png)
* 딕셔너리는 Hash로 구현 : indexing 속도가 O(1)
* Delete, Clear : O(1)
    - d.clear : in-place
    - s = {} or dict() : out-place

### Set
* 딕셔너리의 key만 모여있는 형태 → 집합형
* 선언 : {} 또는 set()
    - 빈 중괄호는 빈 딕셔너리로 인식
```python
s = set([1,2,3]) # set expected at most 1 argument
s.add(4)          # 요소 추가
s.add('text')     # 중복된 요소는 추가 x
print(s)          # {1,2,3,4,'text'} 출력

s.remove(2)     # 요소 삭제
s.remove(99)    # 존재하지 않는 요소 삭제는 error
s.discard(99)   # 요소 삭제, 존재하지 않을 경우 무시
s.update([1,99,None,True])
print(s)        # {1, None,3,4,99,'text} 출력
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


## 조건문 & 반복문
* Generator : 리스트와는 다르게 숫자를 하나씩 생성 반환(메모리 효율적)

* 제어문 - 반복문에서의 else
    - Else문으로 반복을 완전히 돌았을 경우 실행되는 block 지정 가능
    - ex)
    ```python
    for i in range(10) :
        print(i)
    else : 
        print('Loop complete with break')
    ```
    - Break로 중간에 나오게 되면 Else 문이 실행되지 x

## 함수
* 인자로 받은 값을 바로 수정하는 것은 권장하지 않음
    - out-place로 복사해서 사용 권장
* 상위 변수 사용 선언
    - 함수 맨 앞에 선언
    - global : 최상위 변수
    - nonlocal : 바로 상위 변수
    - ex)  
    ```python
    var = 1
    def main() :
        var = 10
        
        def func1() :
            global var 
            var += 1 # global var = 2
        
        def func2() :
            nonlocal var
            var += 1 # main의 var = 11
        
        func1()
        print('after f1,', var) # main 함수 안이므로 main의 var = 10 출력
        func2()
        print('after f2,', var) # 11 출력
    
    main()
    print(var) # main에서 func1 실행했으므로 2 출력
    ```
    - 스파게티 코드의 주 원인이므로 사용하지 않는 것 권장
* 순수함수 : 인자 값이 같을 때, 반환 값도 같은 함수
* 프로그램을 스파게티로 만들지 않는 법
    1. 상위 객체엔 가능하면 접근하지 않기
    2. 되는대로 모두 파라미터로 받기
    3. 최상위 선언도 가급적 지양
* Closure를 만드는 방법
    - Closure : 함수가 선언됐을때의 환경을 저장해(Variable Capture) 실행하는 것
    - 파이썬에서 closure는 factory 형식으로 사용
        + factory 형식 : 함수를 실행시켰을 때 output으로 객체를 생성
    - ex)
    ```python
    number = 10
    def print_closure_factory(number) :
        def print_closure() :
            print(number)
        return print_closure
        
    print_5 = print_closure_factory(5) # print_5라는 함수 class의 변수로 지정
    print_10 = print_closure_factory(10)

    number += 10
    print_5()       # 5 출력
    print_10()      # 10 출력
    print(number)   # 20 출력
    ```
    - 파이썬에서는 함수도 일반 객체이므로 변수 및 파라미터, 리턴값 등 할당 가능
    - ex2)
    ```python
    def add(var) : 
        return var + 2          # 2를 더하는 함수
    def multiply(var) :
        return var * 2          # 2를 곱하는 함수
    def factory(function,n) :   # closure라는 함수를 반환하는 함수
        def closure(var) :      # function을 n번 실행하여 값을 반환하는 함수
            for _ in range(n) :
                var = function(var)
            return var
        return closure
    print(factory(add,4)(10))       # 18 출력
    print(factory(multiply,4)(3))   # 48 출력
    ```

### 꾸밈자(Decorator)
* 함수 하나를 인자로 받아 같은 형태의 함수를 반환하는 함수
* @을 사용하여 함수를 꾸미는데 사용 가능 
* ex)
```python
def print_closure_factory(function) :
    def print_closure(var) :
        print('Input:',var)
        out = function(var)
        print('Output:',out)
    return print_closure
def add(var) :
    return var + 2
print_add = print_closure_factory(add)
print_add(10)

# 위의 코드에 꾸밈자(decorator) 사용
def print_decorator(function) :
    def print_closure(var) :
        print('Input:',var)
        out = function(var)
        print('Output:',out)
    return print_closure

@print_decorator
def add(var) :
    return var + 2

add(10)
'''두 코드 다 출력은 아래와 같다
Input : 10
Output : 10'''
```
* Decorator with Argument
    - ex)
    ```python
    def times_decorator_factory(times) :
        def times_decorator(function) :
            def closure(var) :
                for _ in range(times) :
                    var = function(var)
                return var
            return closure
        return times_decorator

    @times_decorator_factory(5)
    def add(number) :
        return number + 2
    print(add(4)) # 14 출력
    ```
    - Decorator에 인자를 추가하기 위해선 함수를 한번 더 wrapping 필요
    - 함수를 wrapping하기 때문에 기존 함수에 접근 불가(함수명 등)
        + functools 라이브러리의 wraps 데코레이터 사용 : `@wraps(funtion)`

### 재귀함수
* 자기 자신을 호출하여 반복적으로 수행
* ex)
```python
def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)
print(factorial(5)) #120
```

### Keyword Variable Length Parameter
* 키워드 가변인자 : 명시적으로 지정되었지만 파라미터가 남으면 남는 키워드 변수를 딕셔너리 형태로 packing
* **(Double asterisk)를 사용
* 파라미터 순서 : 일반 인자 → 기본값(키워드) 인자 → 가변 인자 → 키워드 가변인자
* ex)
```python
def function(var1,var2=10,*args,**kwargs):
    print(var1, var2, args, kwargs)
function(1,2,3,4,5,var1=100,var2=200)
# 1 2 (3,4,5) {'var1':100, 'var2':200} 출력
```

### Parameter Unpacking
* Sequence에 *을 붙이면 unpacking
    - 리스트, 튜플에 적용 가능
    - ex)
    ```python
    def function(a, b, c) :
        print(a, b, c)
    l = [1, 2, 3]
    function(*l) # 1 2 3 출력

    def func(a,*b) :
        print(a,b)
    func(*l) # 1 (2, 3) 출력
    ```
* Dictionary에 **을 붙이면 Keyword unpacking
    - ex)
    ```python
    def function(var1, var2, **kwargs) :
        print(var1, var2, kwargs)
    d = {'var1':10, 'var2':20, 'var3':30, 'var4':40}
    function(**d) # 10 20 {'var3':30, 'var4':40} 출력
    ```
### Type hints
* 파이썬은 동적 타이핑이므로 interface를 알기 어렵고 가독성이 낮아질 수 있음
* 함수에 타입 힌트 제공이 가능
    - 함수명(변수 : 자료형, ...)의 형태
    - ex)
    ```python
    # string과 integer를 받아 string을 반환
    def multiply_text(text : str, n : int) -> str :
        return text * n
    ```
* 타입힌트와 실제 인수의 타입이 달라도 에러 x
    - 타입 검사 하지 x, 코드 가독성을 높이기 위함

## 파이써닉한 프로그래밍

### Comprehension
* List, Dictionary 등을 빠르게 만드는 기법
    - for + append보다 속도 빠름
    - ex)
    ```python
    result = []
    for i in range(10) : 
        result.append(i*2)
    # Comprehension
    result = [i * 2 for i in range(10)]

    result = {}
    for i in range(10) :
        result[str(i)] = i
    # Comprehension
    result = {str(i) : i for i in range(10)}

    result = set()
    for i in range(10) :
        result.add(str(i))
    # Comprehension
    result = {str(i) for i in range(10)}
    ```
* If문을 마지막에 달아 원하는 요소만 추가 가능
```python
evens = [i for i in range(100) if i % 2 == 0]
```
* 이중 for문 사용 가능
```python
result = [(i,j) for i in range(5) for j in range(i)]
# [(1,0),(2,0),(2,1),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3)]
```
* 다차원 배열 만들기가 매우 유용
```python
eye = [[int(i == j) for j in range(5)] for i in range(5)]
# identity matrix(단위행렬)
```

### Generator
* 요소를 하나씩 생성해서 반환하는 객체
    - 함수에 yield를 사용
    - yield 하는 위치에서 값을 반환
    - return과 유사하나 return은 반환 후 반복을 멈춤
    - yield는 다시 값을 요청받을 시 yield 다음 줄부터 실행
    - 시퀀스 전체를 생성하는 것이 아니므로 메모리 효율적
        + 매우 큰 데이터 셋을 처리할 때 사용 권장
    - 괄호로 Generator Comprehension 형태로 선언 가능
        + ex )
        ```python
        even_generator = (i * 2 for i in range(3))
        for j in even_generator :
            print(j)
        # 0 2 4 출력(개행된 형태로)
        ```
        + 함수 등으로 이미 괄호가 쳐져 있다면 괄호 생략 가능

### 내장함수(Built-in Function)
* sum([Iterable])
* any([Iterable]), all([Iterable])
```python
>>> any([False, True, False]) # 하나라도 참
True
>>> all([False, True, False]) # 모두 참
False
```
* max([Iterable]), min([Iterable])
* zip
    - 2개 이상의 순환 가능한 객체를 앞에서부터 한 번에 접근할 때 사용
        + 길이가 다를 때는 남는 것 버림
        + Tuple로 반환
    - Unpacking을 이용하여 2차원 리스트의 열 단위 접근 가능
    ```python
    array = [[1,2,3],[4,5,6],[7,8,9]]
    for col in zip(*array) :
        print(col) # 열 단위 접근
    # (1, 4, 7), (2, 5, 8), (3, 6, 9) 출력(개행된 상태로)
    ```
    - seq2 = zip(*seq1)의 역연산은 seq1 = zip(*seq2) : 전치행렬 원리
* enumerate (Generator)
    - for문에서 시퀀스를 돌면서 index가 필요한 경우에 사용
    ```python
    seq = ['This','is','sentence']
    for i, word in enumerate(seq) :
        print(i,word)
    # 0 This
    # 1 is
    # 2 sentence 출력
    ```
    - zip과 enumerate를 동시에 사용하는 등 여러 Generator를 한번에 사용 가능
        + ex)  
        ```python
        seq1 = ['This','sentence']
        seq2 = [True, False]
        
        for i, (a, b) in enumerate(zip(seq1,seq2)) :
            print(i,a,b)
        # 0 This True
        # 1 sentence False 출력
        ```
    - Generator를 List 형태로 출력하기 위해서 list로 변환 필요
        + ex)  
        ```python
        list(enumerate(['This','is','sentence']))
        # [(0, 'This'), (1, 'is'), (2, 'sentence')] 출력
        ```
* Lambda Function(람다 함수)
    - 여러 줄, 구문을 쓸 수 없음
    - 공식적으로는 사용을 권장하지 않음
        + 문서화 지원 미비
        + 자원 관리에 불편
        + 복잡한 함수 작성 시 가독성 하락
* map(함수, 시퀀스)
* filter(함수, 시퀀스)
    - 각 요소에 function 함수를 적용하여 참이 나오는 것만 반환
    ```python
    seq = [6,-2,8,4,-5]
    list(filter(lambda x : x>0,seq)) # [6,8,4] 출력
    ```
## 객체 지향 프로그래밍
* 객체 단위의 코드 작성 및 분업
* 각 클래스(Class)당 객체(Object)가 하나만 존재하진 않는다. 그러나 각 객체의 속성(Attribute)는 달라도 행동(Method)은 동일하다.

### 클래스
```python
class Courier(object) : # 클래스 선언(Object) 생략 가능 
    NATIONALITY = 'KOR' # 클래스 속성(Attribute)

    def __init__(self, name:str, address:str) : # 생성자
        self.name = name    # 속성
        self.address = address
        self.parcels = []

    def assign(self, parcel:str) -> None :
        self.parcels.append(parcel)
    
    def deliver(self) -> None : 
        for parcel in self.parcels :
            print(parcel, '배달중')

# 객체 생성
courier1 = Courier('김기사', '경기도 성남시 정자동')

# 속성 출력
print(courier1.name,'-',courier1.address,'근무중')

# 메소드 실행
courier1.assign('TV 상자')
courier1.assign('편지')
courier1.deliver()
```

* 클래스 선언부
    - 클래스 이름은 Camel 표기법(단어 첫 알파벳 대문자로)이 관습적으로 사용됨
    - 부모 클래스가 지정되지 않았을 시 object가 자동 상속(python3)
* 클래스 속성(Attribute)
    - 클래스 전체가 공유하는 속성 값
    - 모든 객체(Instance)가 같은 값을 참조
    - 남용하면 스파게티 코드의 원인이 됨
    - 클래스.속성 또는 객체.속성 형태로 접근
* 클래스 함수(Method)
    - 각 객체에 적용이 가능한 함수
    - 현재 수정하고자 하는 객체를 'self'로 지칭(관습)
    - 파이썬은 'self'를 첫번째 파라미터로 명시적으로 받음
    - 클래스.메소드(객체,파라미터,..) 또는 **객체.메소드(파라미터..)**
* 객체 속성(Attribute)
    - 각 객체가 개인적으로 가지는 값
    - 객체.속성의 형태로 접근
    - 클래스 형태로 선언되어 나온 객체는 언제 어디서든 속성 수정 가능(권장x)
        + ex)
        ```python
        courier1 = Courier('김기사','경기도 성남시 정자동')
        courier1.value = 10 # value는 클래스 속성에 정의되지 않았지만 값 부여 가능
        print(courier1.value) # 10 출력
        ```
* Magic Method : 생성자(Initializer)
    - 객체를 생성할 때 호출됨
    - 일반적으로 객체의 속성을 초기화(혹은 초기값 설정)하는 데 사용
    - 객체 = 클래스(arg...)의 형태로 호출하여 객체 생성
    - Argument format이 x
* Magic Method : 소멸자(Destroyer)
```python
class Courier(object) :
    def __del__(self) : # 소멸자
        self.parcels.clear()
```
    - 객체를 소멸할 때 호출됨
    - 파이썬은 쓰레기 수거(Garbage Collection)로 메모리 관리
        + 객체가 어디에서도 참조되지 않을 때 소멸
        + 잘 사용되지 x
    - del 명령어 : 참조 삭제 o 객체 삭제 x

### 상속(Ingeritance)
* 자식 class가 부모 class의 기능을 이용 가능
* 파이썬에서는 다중 상속 지원
    - 참조할 때 메소드 탐색 순서(mro)를 따름
    - super 내장함수를 이용해 상위 클래스 접근 가능

### 다형성(Polymorphism)
* 같은 이름의 메소드를 다르게 작성
    - 부모 메소드로 접근 시 자식 메소드 실행
    - 외부에서는 똑같은 API로 접근하여 코드 수정이 X

* 상속&다형성 예시
```python
# 부모클래스
class Courier : 
    def __init__(self, name:str) :
        self.name = name
        self.parcels = []

    def assign(self, parcel:str) -> None :
        self.parcels.append(parcel)
    
    def deliver(self) -> None : 
        for parcel in self.parcels :
            print(parcel, '배달중', self.address)

# 자식클래스
class JejuCourier(Courier) :
    def __init__(self, name:str, ticket:int) :
        super().__init__(name)  # 부모클래스 생성자 접근(정해진 호출 타이밍 無)
        self.ticket = ticket
    
    def deliver(self) -> None :
        print(self.ticket, '티켓으로 제주도 이동')
        super().deliver()

courier = JejuCourier('김기사', 15)
courier.assign('편지')
courier.deliver()
super(JejuCourier,courier).deliver() # super로 언제나 원하는 상위 클래스로 변환 및 접근 가능 / 클래스 밖에서 호출할때는 (클래스, 객체)로 호출

"""출력
15 티켓으로 제주도 이동
편지 배달중
편지 배달중 (super문으로 출력됨)""" 
```
* 파이썬에는 2가지 정적 함수 존재
    - 일반적으로 클래스.메소드 형태로 사용
    - Static Method
        + staticmethod 꾸밈자 사용
        + 특별한 arg 받지 x
        + 일반적으로 class 내 유틸함수로 사용
        + Class를 일종의 Namespace로 사용
    - Class Method
        + Classmethod 꾸밈자 사용
        + 호출된 class인 cls를 받음(self와 비슷)
        + factory 패턴에서 사용
    - 유사하나 상속하면 차이가 발생

### 가시성(Visibility), 캡슐화
* 다른 클래스에게 객체의 내부를 감추기
    - 캡슐화, 정보 은닉
    - 클래스 간 간섭 최소화
    - 최소한의 정보만을 지정된 API로 공개
    - C나 Java에서는 private & protected로 구현하나 Python에서는 명시적으로는 모두 public
    - private 변수/함수 이름 앞에 __를 붙임
    - protected 변수/함수 이름 앞에 _를 붙임
    - public과 기능적 차이는 없으나 가독성을 위해 작성
* Property
    - Getter, Setter를 명시적으로 설정 가능
    - Encapsulation 등에 활용
    - 가독성을 위해 적재적소에 활용

### Magic Methods
* Indexing : &#95;&#95;getitem&#95;&#95;, &#95;&#95;setitem&#95;&#95;
    - [] 인덱싱을 재정의
* Length : &#95;&#95;len&#95;&#95;
* Typing : &#95;&#95;str&#95;&#95;, &#95;&#95;int&#95;&#95;, &#95;&#95;float&#95;&#95;, &#95;&#95;bool&#95;&#95;
    - 객체를 다른 타입으로 형 변환할때 호출
* Comparison Operator : &#95;&#95;lt&#95;&#95;, &#95;&#95;le&#95;&#95;, &#95;&#95;gt&#95;&#95;, &#95;&#95;ge&#95;&#95;, &#95;&#95;eq__, &#95;&#95;ne__
    - &#95;&#95;lt__ : A < B를 호출 → A.&#95;&#95;lt__(B)를 호출
* Arithmetetic Operator : &#95;&#95;add__, &#95;&#95;sub__, &#95;&#95;mul__
    - in-place 버전인 __iadd__가 존재 : 이 경우 self를 직접 수정 필요
* Callable : &#95;&#95;call__
    - 생성된 객체를 호출 가능하게 만듦
    - instance(args...)가 instance.&#95;&#95;call__(args...)를 호출
* Iterable
    - iter 내장함수 : 해당 객체의 순환자 반환, &#95;&#95;iter__ 호출
    - next 내장함수 : 해당 순환자를 진행, &#95;&#95;next__ 호출
    - 끝에서 Stopiteration Exception
    - Generator는 자동으로 &#95;&#95;iter__와 &#95;&#95;next__가 구현
* Context Manager : &#95;&#95;enter__, &#95;&#95;exit__
    - 소멸자 대용으로 특정 Block 입장/종료 시 자동으로 호출
    - File description 등을 자동으로 닫고자 할 때 사용

## 모듈 & 패키지
