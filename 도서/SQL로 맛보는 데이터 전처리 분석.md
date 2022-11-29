> 도서 <SQL로 맛보는 데이터 전처리 분석> 노수영

## 데이터베이스와 SQL
### 데이터베이스
- 구조화된 데이터의 모임
- 종류
    - RDB(MySQL, MariaDB, Oracle 등) : 관계형 데이터베이스는 데이터가 구조화되어 있고, SQL을 통해 조회 가능
    - NoSQL(MongoDB, Hbase, Casandara 등) : 데이터가 구조화되지 않고, 행열의 개념보다 문서의 개념으로 접근하며, 분산 확장이 가능해 대용량 데이터 처리에 용이
    - 빅데이터에 NoSQL이 적합하나, 분석 업무에서는 RDB 형태로 변환해 분석하는 경우가 많다.
- 데이터베이스와 서버
    - 서버 : 특정 목적을 위해(특정 서비스를 제공하는) 컴퓨터
    - DB 서버에 기록된 데이터를 이용해 분석 업무 수행
### SQL
- 데이터베이스에 접근하고 데이터베이스를 조작하는 언어
- MySQL Workbench : MySQL(데이터베이스)의 SQL 작성을 용이하게 돕는 툴
### 서버, GUI
- 웹 서버 : 클라이언트(ex : 웹 브라우저)로부터 HTTP 요청을 받고 웹페이지를 반환하는 서버
    - 클라우드 서비스 : 사용자 환경 밖에서 서비스, 컴퓨터 자원을 사용하고 이에 대한 비용을 지불하는 서비스
        - 트래픽에 따라 유동적으로 메모리, CPU 등의 자원을 조절할 수 있고 초기에 막대한 인프라 구축 비용을 줄일 수 있다.
- 데이터베이스 서버 : 데이터베이스 서비스를 다른 컴퓨터나 프로그램에 제공하는 서버(유기적으로 동작)
- DB GUI Tools : 데이터베이스 탐색, 사용자 권한, 쿼리 작성 등을 쉽게 할 수 있는 기능 제공
### SQL 쿼리 작성법
1) 문법, 작성법 완벽하게 숙지
2) 절차 먼저 고민해 보기
    - SQL을 이용해 데이터를 조회할 때 가장 중요한 부분은 **정확성**과 **속도**
    - 먼저 어떤 데이터가 필요하고, 어떤 형식으로 데이터를 가공, 결합해 데이터를 추출할지 절차를 생각해 보는 것이 중요
3) 데이터 정합성, 정확성
    - 정합성 : 다양한 DB 내에 중복 등으로 인한 데이터의 불일치가 없는 상태
        - 부분 합과 전체 합 비교하기
        - 분석하기 편한 형태로 데이터 가공하기(최대한 새로운 쿼리 작성하지 않고 분석 - Human error 줄이기 위해)
        - Review하기

## SQL 문법
> 프로그래머스 > [코딩테스트](/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8.md)에 정리

## 데이터 추가, 삭제, 갱신, 데이터 정합성
### INSERT(행 추가하기)
```SQL
INSERT INTO 테이블명 (칼럼명1, 칼럼명2, 칼럼명3, ...) VALUES (값1, 값2, 값3, ...);
-- 여러 행을 추가하려면 VALUES에 ,로 구분해 여러 줄 입력
INSERT INTO 테이블명 (칼럼명 나열) VALUES (행1의 값 나열), (행2의 값 나열), ... ;
```

### DELETE(행 삭제하기)
```SQL
DELETE FROM 테이블명 WHERE 조건
```
* 데이터를 한번 삭제하면 복구하기가 까다로우므로, DELETE 전에 SELECT하여 확인 후 삭제

### UPDATE(데이터 갱신하기)
```SQL
UPDATE 테이블명 SET 컬럼명1 = 바꿀 값1, 컬럼명2 = 바꿀값2, ...
WHERE 조건;
```

### Procedure
* 매크로처럼 반복되는 내용을 하나의 단위로 생성
```SQL
DELIMITER //
CREATE PROCEDURE 프로시져명()
BEGIN
쿼리
-- 예시
UPDATE 테이블명
SET 컬럼명 = 바꿀 값 또는 식
WHERE 조건;
END //
DELIMITER;
```
* 생성된 프로시저는 `CALL 프로시저명`으로 실행 가능하며 스케줄을 통해 특정 상황에서 실행 가능

### View
* 테이블을 직접 생성하지 않고 SELECT문의 출력 결과를 보여 준다.
```SQL
CREATE VIEW DB.뷰명
AS SELECT -- 생성할 VIEW의 내용
```
* VIEW의 특징
    - 가상의 테이블, 사용자의 입장에서는 테이블과 동일하게 보이지만, 뷰는 실제 데이터를 가지고 있지 X
    - 실제 테이블에 링크된 개념
    - 엑세스 제한을 위해 주로 사용됨

### 데이터 정합성
* 데이터들의 값이 일치함
* MECE(Mutually Exclusive Collectively Exhaustive)
    - 서로 중복 x, 누락 x
    - 세그먼트로 나눠 분석할때, 각 세그먼트 간의 교집합이 발생하지 않도록 구분해서 분석
        - = 나눈 그룹의 합이 전체가 되도록 구성
        - = 각 항목들이 상호 배타적이면서 모였을 때는 완전하게 합쳐지는 것
* 번거롭더라도 항상 데이터 정합성 확인할 것!

## 자동차 매출 데이터를 이용한 리포트 작성
### 데이터 생성
- ERD를 통해 데이터 구조 파악
### 구매 지표 추출
* 매출액
    - 일별 매출액 조회
    ```SQL
    SELECT A.ORDERDATE, SUM(B.PRICEEACH * B.QUANTITYORDERED) AS SALES FROM classicmodels.ORDERS A LEFT JOIN classicmodels.ORDERDETAILS B ON A.ORDERNUMBER = B.ORDERNUMBER
    GROUP BY 1
    ORDER BY 1;
    ```
    - 월별 매출액 조회
        + SUBSTR(칼럼, 위치, 길이) : 문자열에서 원하는 부분만 가져오기
    ```SQL
    SELECT SUBSTR(A.ORDERDATE,1,7) AS MONTH, SUM(B.PRICEEACH * B.QUANTITYORDERED) AS SALES FROM classicmodels.ORDERS A LEFT JOIN classicmodels.ORDERDETAILS B ON A.ORDERNUMBER = B.ORDERNUMBER
    GROUP BY 1
    ORDER BY 1;
    ```
    - 연도별 매출액 조회
    ```SQL
    SELECT SUBSTR(A.ORDERDATE,1,4) AS YEAR, SUM(B.PRICEEACH * B.QUANTITYORDERED) AS SALES FROM classicmodels.ORDERS A LEFT JOIN classicmodels.ORDERDETAILS B ON A.ORDERNUMBER = B.ORDERNUMBER
    GROUP BY 1
    ORDER BY 1;
    ```
* 구매자 수, 구매 건수(일자별, 월별, 연도별)
* 인당 매출액(연도별)
* 건당 구매 금액(ATV, Average Transaction Value)(연도별)
### 그룹별 구매 지표 구하기
* 국가별, 도시별 매출액
* 북미(USA, Canada) vs 비북미 매출액 비교
### 재구매율
* 국가별 2004, 2005 Retention Rate(%)
### Best Seller
### Churn Rate(%)
* Churn Rate
* Churn 고객이 가장 많이 구매한 Productline