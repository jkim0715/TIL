## SQL

- data를 조작하고 어떻게 연동하는가..?  에 대해 공부
- ANSI 표준, Oracle 표준, 



### 데이터 베이스란?

- 대량의 정보를 컴퓨터(software)가 효율적으로 접근할 수 있도록 가공 및 저장한 것.
- DBMS - 데이터베이스를 관리하기 위한 시스템
  - 다수의 사람이 대량의 데이터를 안전하고 쉽게 사용 가능.
  - 아무리 큰 회사라도 하나의 머신을 이용..여러개 있으면 헷갈린다.

- RDBMS - 관계형 데이터 베이스를 관리
  - Relational 한 데이터들... 
  - ex) 사원의 ID..  사원의 부서 ... 등등 
  - 여러가지 KEY 값을 통해 관리한다.
  - 점점 Web환경에서 처리할 수 있도록 바뀜..
    - 그에따라 보안이 중요해짐.
  - 모바일로 처리하도록 변하는 중.



#### DBMS가 필요한이유

- 다수의 사람이 데이터를 공유하기 어렵다.
- 대량의 데이터를 다루기 어려운 형태
- 읽/쓰 자동화 하려면 프로그래밍 기술 필요
- 만일의 사고에 대응하기 힘듬.

#### DBMS 의 종류

- 계층형 데이터 베이스 (Hierarchical Database)
- 관계형 데이터 베이스(Relational Database:RDB)
- 객체지향 데이터 베이스(Object Oriented Database:00DB)
- XML 데이터 베이스(XML Database:XMLDB)

- 키-밸류형 데이터스토어(Key -Value Store:KVS) *** 요즘 핫함..
  - 트위터.. 

- SQL 은 관계형 데이터 베이스를 제어하기 위한 언어이다.



## SQL 문장 

#### 종류

## DDL(Data Definition Language) :데이터 정의언어

- #### CREATE

``` SQL
CREATE TABLE T_USER(
	ID VARCHAR2(10),    --(10)10자리까지 가능
    PWD VARCHAR2(10),	--VARCHAR2 는 버전..
    NAME VARCHAR2(20)	--variable char
);

DESC T_USER; 	// 만든 테이블 정보 확인 

------------------------------------------------------------------

CREATE TABLE T_PRODUCT(
	ID VARCHAR2(10) PRIMARY KEY,  -- 중복방지
    NAME VARCHAR2(20) NOT NULL,		--상품 이름없음 데이터 못드가게 에러띄움
    PRICE NUMBER(10,1) NOT NULL, -- 오라클에서 숫자표현 방법. 숫자10자리, 소수 1째자리
    REGDATE DATE	NOT NULL	-- 날짜형

);
```

- #### DROP

``` sQL
DROP TABLE T_USER; 	//테이블 뿐만 아니라 데이터까지 싹다날림.. 잘못하면 소송감임 
```



- #### ALTER

``` SQL
ALTER TABLE T_PRODUCT ADD (REGDATE DATE);-- 제약조건 변경, 컬럼 추가
ALTER TABLE T_PRODUCT DROP (REGDATE);-- 빼기
ALTER TABLE T_PRODUCT ADD PRIMARY KEY (ID); -- ID에 PRIMARY KEY 추가
ALTER TABLE T_PRODUCT MODIFY(NAME CHAR(10)); --타입 바꾸기 VARCHAR -> CHAR
ALTER TABLE T_PRODUCT MODIFY(NAME NULL);  -- 제약조건 바꿀 수 있다,
ALTER TABLE T_PRODUCT RENAME COLUMN NAME TO UNAME; -- 이름을 NAME -> UNAME 으로 바꾸기
ALTER TABLE T_PRODUCT RENAME TO PRODUCT; --테이블 이름 바꾸기.
ALTER TABLE T_USER MODIFY (NAME UNIQUE); -- 유니크만들기(PRIMARY KEY 말고)같은이름 불가
```





## DML(Data Manipulation Language):데이터 조작언어

- #### SELECT(Read)

  - 검색용

``` SQL
SELECT * FROM EMP;

SELECT ENAME,SAL FROM EMP;

SELECT ENAME,SAL,DEPTNO AS DNO FROM EMP;  --컬럼 명칭 바꿔버리기
SELECT ENAME,SAL,SAL*12 AS ASAL,DEPTNO AS DNO FROM EMP; -- 연봉계산하고 이름 쉽게 바뀌기
SELECT ENAME,SAL,SAL*12 AS "ANN SAL",DEPTNO AS DNO FROM EMP; -- 중간에 한칸 띄우기 "" 쓰면댐

SELECT ENAME || JOB FROM EMP;  -- merge 같은 기능.. 노쓸모일듯..
SELECT ENAME,SAL + COMM,SAL FROM EMP; --컬럼 더해서 표에 표시
SELECT SAL, COMM, (SAL*12*.87) + (NVL(COMM,0)*12*.88) AS ANNSAL FROM EMP;
/*  NVL (XXX,0)  XXX에서 NULL값을 0으로 계산 */
SELECT SAL, COMM, (SAL*12*.87) + (NVL(COMM,0)*12*.88) AS ANNSAL FROM EMP WHERE (SAL*12*.87) + (NVL(COMM,0)*12*.88) > 30000;  -- 30000 이상 고르기.. WHERE 절에 그냥 WHERE ANNSAL > 30000 안되고 식을 싹다 써야함... 



SELECT ENAME || ''|| SAL AS ENAMEANDJOB FROM EMP;  
SELECT DISTINCT(JOB) FROM EMP;		-- 컬럼 종류 중복 걸러내기

SELECT * FROM EMP WHERE JOB = 'SALESMAN' -- SALESMANS만 찾기
SELECT * FROM EMP WHERE JOB = 'SALESMAN' AND SAL > 1000;  -- 조건 여러개도 가능.
SELECT * FROM EMP WHERE JOB = 'MANAGER' AND SAL >1000 AND HIREDATE > '02/20/1981';

SELECT ENAME,SAL FROM EMP WHERE SAL BETWEEN 2000 AND 3000 -- 양 끝단의 값을 포함하기 때문에 주의 ! 


/*
중간에 들어간 글자 찾기
*/
SELECT * FROM EMP WHERE ENAME LIKE '%C%'; -- 중간에 c
SELECT * FROM EMP WHERE ENAME LIKE '%C';	-- C로 끝남
SELECT * FROM EMP WHERE ENAME LIKE 'C%';	-- C로 시작
SELECT * FROM EMP WHERE  ENAME NOT LIKE '%F%' ; -- F 안드가는거.

SELECT * FROM EMP WHERE COMM IS NULL ; -- NULL 값 조회는 비교연산자 = 를 사용하지 못한다. IS NULL  / IS NOT NULL
SELECT * FROM EMP WHERE NOT (SAL >= 2000)  ; --이런것도 가능..
SELECT * FROM EMP WHERE  SAL < 2000 AND DEPTNO = 30 OR ENAME LIKE '%F%' ; -- AND OR 연산은 앞에서부터 순서대로 진행

-- 정렬
SELECT ENAME,SAL FROM EMP ORDER BY SAL			--기본 오름차순 ASC
SELECT ENAME,SAL FROM EMP ORDER BY SAL DESC;	-- DESC 내림차순
SELECT ENAME,SAL FROM EMP WHERE SAL >1000 AND DEPTNO =20 ORDER BY 2;  -- 2번 = SAL 이므로 같은 값,, 1이면 ENAME 이므로 앞파벳 순으로 정렬
SELECT ENAME,SAL, SAL*12 AS ANN_SAL FROM EMP WHERE SAL >1000 AND DEPTNO =20 ORDER BY ANN_SAL;  -- 컬럼명으로 비교는 안됐지만 정렬은 가능 !

SELECT * FROM EMP WHERE MGR IS NOT NULL ORDER BY MGR,ENAME; -- 여러개 정렬 가능. 
SELECT * FROM EMP WHERE COMM IS NOT NULL ORDER BY COMM DESC -- NULL값 빼고정렬
```



- #### INSERT(C)

``` SQL
INSERT INTO T_USER(ID,PWD,NAME) VALUES('','','');
--- 한글값 넣을때는 한글자당 3BYTE씩 먹으므로 VARCHAR(20) 이거 잘 설정하기 바람.
INSERT INTO T_USER VALUES('ID01','PWD01','이말숙'); --VALUES 앞에다 컬럼명 안써도 됨

INSERT INTO T_PRODUCT VALUES ('P02','PANTS2','20000',SYSDATE);

--중간에 돈 20000 뺴고 넣기
INSERT INTO T_PRODUCT (ID, NAME, REGDATE) VALUES ('P02','PANTS2',SYSDATE); 

-- 이렇게 하면 나중에 분석 연산할때 매우 위험 !
ALTER TABLE T_PRODUCT MODIFY (PRICE DEFAULT 1000); -- 디폴트값 줘서 빈값 10000 수렴.



```

- #### UPDATE

``` SQL
UPDATE T_USER SET PWD = '111';  --싹다 111 로 바꿈
UPDATE T_USER SET PWD = '111', NAME= '공말숙'; -- 여러개
UPDATE T_USER SET PWD = '111',NAME= '공말숙' WHERE ID = 'ID03';
```

- #### DELETE

``` SQL
DELETE FROM T_USER					-- 싹다 삭제
DELETE FROM T_USER WHERE ID = 'ID05'  -- WHERE 로 조건 설정
TRUNCATE <테이블명>; -- 테이블의 모든 데이터를 삭제.
```



## DCL(Data Control Language) :데이터 제어 언어

- #### COMMIT 

  - 확정.. Transaction에 사용..

    ```SQL
    COMMIT
    ```

    

- #### ROLLBACK

  - 롤백 .. Transcation에 사용..

    ``` SQL
    ROLLBACK
    ```

    

- #### GRANT

- #### REVOKE




#### FUNCTION 

- 단일 행 함수 ( ABS, MOD, ROUND )

``` SQL
SELECT ENAME, ABS(SAL) FROM EMP;  -- 컬럼안의 숫자를 컨트롤 하는 함수.
SELECT ENAME, MOD(SAL,3) FROM EMP; -- 나머지...
SELECT ENAME, SAL, ROUND(SAL/7,3) FROM EMP; -- 반올림 3자리까쥐
```

- 문자열 함수

```SQL
SELECT ENAME ||' '|| JOB AS EJOB FROM EMP;
SELECT LOWER(ENAME)FROM EMP; --소문자로 만들어버리기
SELECT ENAME, SUBSTR(ENAME,1,3) FROM EMP; -- 자리수만큼만 프린트 1번째 부터 3자리
SUBSTR(SAL,1,2) --첫번째부터 두자리 
SUBSTR(SAL,1,2)*10  --SUBSTR의 결과값이 숫자면 연산까지 가능하다.


SELECT ENAME, SUBSTR(ENAME,1,3), REPLACE(ENAME, SUBSTR(ENAME, 2, LENGTH(ENAME)), LOWER(SUBSTR(ENAME, 2, LENGTH(ENAME)))) FROM EMP; -- 뒺게 헷갈리네 
LENGTH --  영어 숫자 1개, 한글 1개로 침..

SELECT ENAME, SAL,DEPTNO FROM EMP WHERE DEPTNO =20 OR DEPTNO =30;  -- 20 OR 30 
SELECT ENAME, SAL,DEPTNO FROM EMP WHERE DEPTNO IN(20,30) --IN(20,30) 이렇게돗씀
SELECT ENAME, SAL,DEPTNO FROM EMP WHERE DEPTNO NOT IN(20,30) -- NOT IN.
```

- 날짜 함수

``` SQL
SELECT ENAME,CURRENT_TIMESTAMP, HIREDATE, SYSDATE FROM EMP; --보기 어려움.

SELECT ENAME,TO_CHAR(CURRENT_TIMESTAMP,'HH:MM:SS'), HIREDATE, SYSDATE FROM EMP;
SELECT ENAME,TO_CHAR(CURRENT_TIMESTAMP,'YYYY:MM:DD:HH:MM:SS'), HIREDATE, SYSDATE FROM EMP;  -- TO_CHAR(날짜컬럼,'')  원하는 모양으로 바꾸기

SELECT ENAME,CURRENT_TIMESTAMP, TO_CHAR(HIREDATE,'YYYY/MM/DD'), SYSDATE - HIREDATE FROM EMP; --- DATE 객체는 연산이 가능하구먼 허허 
TO_CHAR(HIREDATE,'YYYY/MM/DD') -TO_CHAR(SYSDATE,'YYYY/MM/DD') -- 이건 안댐 둘다 CHAR라서..
SELECT ENAME,HIREDATE, SYSDATE - HIREDATE, MONTHS_BETWEEN(SYSDATE,HIREDATE) FROM EMP; -- 두 날짜 사이의 일수, 개월수(MONTHS_BETWEEN) 계산

INSERT INTO T_PRODUCT VALUES ('ID43','PANTS3','30000',TO_DATE('1991:07:15', 'YYYY/MM/DD'));

```

- 변환 함수 

``` SQL
NVL(COMM,0)	-- NULL 값이 있으면 0으로 수렴.

```

#### 술어 

- LIKE
- BETWEEN
- IN(A,B)
- IS NULL



#### CASE

- 등급을 나눌때 주로 씀.

``` SQL
SELECT ENAME, CASE WHEN JOB = 'PRESIDENT'  THEN '왕' WHEN JOB ='MANAGER' THEN '관리자' ELSE '직원' END FROM EMP   -- WHEN THEN (ELSE) END.  다 있어야 해...


SELECT ENAME, SAL, CASE WHEN SAL >= 5000  THEN '왕' WHEN SAL >= 3000 AND SAL <5000 THEN '관리자' ELSE '직원' END AS GRADE FROM EMP  -- 범위로도 할수 있고 마지막에 AS GRADE로 깔끔하게 정리.  
```







#### DDL 



### JAVA

#### JDBC (java data base connectivity)





