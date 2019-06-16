## SQL

- data를 조작하고 어떻게 연동하는가..?  에 대해 공부
- ANSI 표준, Oracle 표준, 



- 다양한 App과의 연동을 위해 배웠음..



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

  - 테이블은 심플하게 생성. 제약조건 설정은 ALTER이용.

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

  - 제약조건 주기

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



- #### INSERT(Create)

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
  - 모든 row의 데이터를 한번씩 적용시켜주는것

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





### 집약 함수

- 집합함수의 결과는 하나다.

- COUNT

  - ``` SQL
    SELECT COUNT(*) FROM EMP;			-- 카운트 (NULL 값을 포함함)
    SELECT COUNT(ENAME) AS CNT FROM EMP;
    SELECT COUNT(COMM) AS CNT FROM EMP;  --NULL을 제외하고 계산 하게됨.
    SELECT COUNT(NVL(COMM,0)) AS CNT FROM EMP; -- NULL값을 포함하고자 한다면 NVL이용
    ```

    

- SUM

  - ``` SQL
    SELECT SUM(SAL) AS CNT FROM EMP;
    SELECT SUM(SAL), SUM(DISTINCT SAL) FROM EMP; -- DISTINCT 는 중복 배제.
    ```

  - 

- AVG

  - ``` SQL
    SELECT ROUND(AVG(NVL(COMM,0)),2) AS CNT FROM EMP;
    ```

  - 

- MAX

  - MAX/MIN 은  날짜에 사용 가능하다.

- MIN

  - ``` SQL
    SELECT MIN(HIREDATE) FROM EMP; 	-- 날짜의 비교는 가능.
    SELECT SUM(HIREDATE) FROM EMP;  -- 날짜의 계산은 불가능
    ```

  - 

``` SQL
SELECT MIN(SAL), MAX(SAL), SUM(SAL), ROUND(AVG(SAL),2) FROM EMP;  
SELECT ENAME, SUM(SAL) AS CNT FROM EMP;  -- 이건 안됨!! 
```

- GROUP BY

  - 그룹함수는, 집합함수랑 같이 사용한다.

  - GROUPING 이 먼저되고 그 그룹내에서 집합함수 사용( SUM, AVG, MIN,MAX)하여 하나의 값을 도출

  - 무엇을 기준으로  GROUPING을 할지가 중요할 듯.

  - ``` SQL
    SELECT JOB FROM EMP GROUP BY JOB;			--가능
    SELECT JOB ,SAL FROM EMP GROUP BY JOB;		--불가능
    SELECT JOB, SUM(SAL) FROM EMP GROUP BY JOB;	--가능.
    
    SELECT DEPTNO, JOB, FROM EMP GROUP BY DEPTNO,JOB ORDER BY DEPTNO; --GROUPING을 여러번 할 수 있다.
    
    SELECT DEPTNO, JOB, SUM(SAL) FROM EMP GROUP BY DEPTNO,JOB HAVING DEPTNO IN(10,20) AND JOB LIKE '%E%' ORDER BY DEPTNO;  -- WHERE 대신 HAVING 을 쓰고,, AND도 가능.
    SELECT DEPTNO, JOB, SUM(SAL) FROM EMP GROUP BY DEPTNO,JOB HAVING DEPTNO IN(10,20) AND JOB IN ('MANAGER', 'CLERK') ORDER BY DEPTNO;  -- 라던지.
    ```

- HAVING

``` SQL
 SELECT JOB, AVG(SAL) FROM EMP WHERE DEPTNO IN (10,30) GROUP BY JOB ;  --가능
 SELECT JOB, AVG(SAL) FROM EMP GROUP BY JOB HAVING DEPTNO IN (10,30);	--불가능
SELECT JOB, AVG(SAL) FROM EMP GROUP BY JOB HAVING JOB IN ('MANAGER', 'CLERK'); --가능
```

- 결론 : HAVING절에는 GROUPING 된것만 들어갈 스ㅜ 있다.

  - WHERE 절에는 그룹함수가 못들어간다.

  - JOB 별 중에서 E 가 들어간 JOB만 조회 하시오.

  - ``` SQL
    SELECT JOB, AVG(SAL) FROM EMP GROUP BY JOB HAVING JOB LIKE '%E%';
    ```

  - JOB별 월금의 평균을 구하시오. 단, DEPTNO가 10,20인 직우너들을 대상으로 하시오

  - ``` SQL 
    SELECT JOB, AVG(SAL) FROM EMP  WHERE DEPTNO IN (10,20) GROUP BY JOB 
    ```

- EXAMPLES

  - ``` SQL 
    -- 년도별 입사자의 평균을 구하시오
    SELECT TO_CHAR(HIREDATE,'YYYY') AS YEAR, AVG(SAL) FROM EMP GROUP BY TO_CHAR(HIREDATE,'YYYY')
    
    --년도별 입사 매니저의 평균을 구하시오
    SELECT TO_CHAR(HIREDATE,'YYYY') AS YEAR, ROUND(AVG(SAL),2) FROM EMP WHERE JOB IN('MANAGER') GROUP BY TO_CHAR(HIREDATE,'YYYY')
    ```

    

### VIEW

물리적으로 테이블을 만드는게 아니고 그냥 임시로 만드는 것임.

- 뷰 작성 방법

  - ```SQL
    CREATE VIEW EMPSALVIEW(ENAME, ANNSAL) AS SELECT ENAME, (SAL*12)+(NVL(COMM,0)*12) FROM EMP   
    ```

- 뷰는 SELECT 문을 저장한다. 



- 뷰 삭제방법

  - ```SQL
    DROP VIEW;
    ```



#### SUBQUAEY

-  절대적으로 TABLE과 TABLE 간에 RELATIONSHIP 이 존재해야함.

- ##### SCALAR SUBQUERY 

  - 반환값이 단일값일때.

  - WHERE 절에 쓸때.

  - ``` SQL
    SELECT DEPTNO FROM DEPT WHERE LOC = 'DALLAS'
    
    SELECT ENAME FROM EMP WHERE DEPTNO = 20
    ```

    - ``` SQL
      SELECT ENAME FROM EMP WHERE DEPTNO = (SELECT DEPTNO FROM DEPT WHERE LOC='DALLAS')
      ```

  - SAL 의 평균보다 많이 받는 사람들의 이름과 SAL을 출력하시오

  - ``` SQL
    SELECT ENAME, SAL FROM EMP WHERE SAL > (SELECT AVG(SAL) FROM EMP )
    
    ```

  -  위 문제에서 DALLAS와 CHICAGO에 근무하는 애들을 고르시오

  - ```SQL
    SELECT ENAME, SAL FROM EMP WHERE SAL > (SELECT AVG(SAL) FROM EMP ) AND (DEPTNO IN ( SELECT DEPTNO FROM DEPT WHERE LOC IN('DALLAS','CHICAGO')))
    
    ```

    SUBQUARY   응용.. 

  - ``` SQL 
    SELECT ENAME, SAL, AVG(SAL) FROM EMP  -- 불가능
    SELECT ENAME, SAL , (SELECT AVG(SAL) FROM EMP ) FROM EMP ; --모든 ROW에 평균표시.
    ```

- #### 상관 SUBQUERY

- 부서별 월급의 평균을 구하고자 한다. 이 중 전체 평균 보다 높은 부서만 출력한다. 단, NEW YORK 부서는 제외한다.

  - ``` SQL
    SELECT DEPTNO,AVG(SAL) FROM EMP GROUP BY DEPTNO HAVING AVG(SAL) >(SELECT AVG(SAL) FROM EMP) AND DEPTNO NOT IN (SELECT DEPTNO FROM DEPT WHERE LOC = 'NEW YORK')
    
    
    ```

  - 여기서 ACCOUNTING 만 뺀다

  - ```SQL 
    SELECT DEPTNO,ENAME,SAL FROM EMP E1 WHERE SAL >= (SELECT MAX(SAL) FROM EMP E2 WHERE E2.DEPTNO = E1.DEPTNO  AND E2.DEPTNO NOT IN (SELECT DEPTNO FROM DEPT WHERE DNAME = 'ACCOUNTING' )GROUP BY DEPTNO)
    ```

- SCOTT이 소속된 부서의 매니저들의 EMPNO, ENAME, DEPTNO 를 조회하시오

  - ```SQL
    SELECT EMPNO, ENAME, DEPTNO FROM EMP WHERE MGR IN (SELECT MGR FROM EMP WHERE JOB =(SELECT JOB FROM EMP WHERE ENAME = 'SCOTT'))
    
    SELECT MGR FROM EMP WHERE JOB =(SELECT JOB FROM EMP WHERE ENAME = 'SCOTT')
    ```

  - ``` SQL 
    SELECT EMPNO, ENAME, DEPTNO FROM EMP E1 WHERE EMPTNO IN (SELECT MGR FROM EMP E2 WHERE DEPTNO = (SELECT DEPTNO FROM EMP WHERE ENAME ='SCOTT')AND E1.EMPNO = E2.MGR)
    ```

  - ``` SQL
    SELECT EMPNO, ENAME, DEPTNO FROM EMP WHERE EMPTNO IN (SELECT MGR FROM EMP WHERE DEPTNO = (SELECT DEPTNO FROM EMP WHERE ENAME ='SCOTT'))
    ```

- #### JOIN

- 두개의 테이블을 합친다.

- EMP 를 조회한다.  EMPNO, ENAME, DNAME, LOC 다나오게.

  - ``` SQL 
    SELECT E.EMPNO, E.ENAME, D.DNAME,D.LOC FROM EMP E, DEPT D
    ```

  - FOREIGN KEY / PRIMARY KEY 를 조건으로 걸어야 함.

  - ``` SQL
    SELECT E.EMPNO, E.ENAME, D.DNAME,D.LOC FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO
    ```

- 지역별 월급의 평균을 구하시오

  - ```SQL 
    SELECT D.LOC, AVG(E.SAL) FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO GROUP BY D.LOC
    ```

  - 

- 지역별 월급의 평균보다 많이 받는 사람의 LOC ENAME,SAL을 조회하시오 DALLAS느 제외하시오 

  - ```SQL
    SELECT D.LOC, E.ENAME, E.SAL FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND D.LOC NOT IN ('DALLAS') AND E.SAL >(SELECT AVG(SAL) FROM EMP E2, DEPT D2 WHERE E2.DEPTNO = D2.DEPTNO AND D.LOC = D2.LOC GROUP BY D.LOC)
    
    SELECT AVG(SAL) FROM E.EMP E2, DEPT D2 WHERE E2.DEPTNO = D2.DEPTNO AND D.LOC = D2.LOC GROUP BY D.LOC
    ```



- ``` sql
  SELECT D.LOC,E.ENAME, E.HIREDATE FROM EMP E, DEPT D WHERE E.DEPTNO= D.DEPTNO 
  AND HIREDATE IN (SELECT MAX(HIREDATE) FROM EMP E1, DEPT D1 WHERE D1.DEPTNO = E1.DEPTNO AND D.LOC = D1.LOC GROUP BY D.LOC) ORDER BY D.LOC
  ```
  
- ##### EXISTS () 

  - ()안에 문장이 TRUE인 값만 가져옴.

- #####  테이블 덧셈 UNION (공통 부분 제외)

  - ```SQL
    MANAGER와 SALESMAN 의 이름과 JOB을 조회하시오 
    SELECT ENAME, JOB FROM EMP WHERE JOB = 'MANAGER' UNION SELECT ENAME, JOB FROM EMP WHERE JOB = 'SALESMAN' ORDER BY JOB
    ```

- ##### UNION ALL ( 공통부분 포함  중복표시)

- ##### 테이블 뺄셈 EXCEPT

- ##### 테이블 간 공통부분 선택 INTERSECT

##### 

#### 결합

- INNER JOIN (두가지 모두 기억하기)

  - ```SQL
    오라클 전용
    SELECT E1.ENAME,D1.LOC FROM  EMP E1, DEPT D1 WHERE E1.DEPTNO = D1.DEPTNO
    ```

  - ```SQL
    ANSI표준
    SELECT E1.ENAME,D1.LOC FROM  EMP E1 INNER JOIN DEPT D1 ON E1.DEPTNO = D1.DEPTNO
    
    ANSI표준 (USING)
    SELECT E1.ENAME,D1.LOC FROM  EMP E1 INNER JOIN DEPT D1 USING (DEPTNO)
    ```

  - ```SQL
    조건 추가 
    SELECT E1.ENAME,D1.LOC FROM  EMP E1 INNER JOIN DEPT D1 ON (E1.DEPTNO = D1.DEPTNO) WHERE E1.JOB = 'MANAGER' AND D1.LOC ='CHICAGO'
    ```

  - ``` SQL
    3개 결합 (T_EMP, T_DEPT, T_SAL) -- PRACTICE 참고 
    SELECT A.ENO,A.ENM,A.SAL,C.ASAL,B.DNM,B.LOC FROM T_EMP A INNER JOIN T_DEPT B ON (A.DNO = B.DNO) INNER JOIN T_SAL C ON (A.ENO = C.ENO)
    ```

- OUTTER JOIN (현업에서 많이 해봄)

  - ``` SQL
    INSERT INTO EMP VALUES (8888,'KSK','SALESMAN',7839,TO_DATE('2019/06/05','YYYY/MM//DD'),4000,100,NULL)
    
    (+)반대 쪽에 없는것도 표시
    SELECT E.ENAME, E.JOB, D.DNAME, D.LOC FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO (+)
    
    SELECT E.ENAME, E.JOB, D.DNAME, D.LOC FROM EMP E, DEPT D WHERE E.DEPTNO(+) = D.DEPTNO (+)
    ```

  - ```SQL
    ANSI 표준
    (LEFT EMP 기준)
    SELECT E.ENAME, E.JOB , D.DNAME, D.LOC FROM EMP E LEFT OUTER JOIN DEPT D USING (DEPTNO)
    
    (RIGHT DEPT 기준)
    SELECT E.ENAME, E.JOB , D.DNAME, D.LOC FROM EMP E RIGHT OUTER JOIN DEPT D USING (DEPTNO)
    
    (양쪽 기준 )
    SELECT E.ENAME, E.JOB , D.DNAME, D.LOC FROM EMP E FULL OUTER JOIN DEPT D USING (DEPTNO)
    ```





### 윈도우 함수 

- RANK 

  - ```SQL
    정렬
    SELECT ENAME, SAL, RANK () OVER (ORDER BY SAL DESC) AS RAKING FROM EMP ORDER BY SAL DESC 
    
    ```

- DENSE_RANK 

  - ``` SQL
    SELECT ENAME, SAL, RANK () OVER (ORDER BY SAL ) AS RAKING, DENSE_RANK() OVER(ORDER BY SAL DESC) AS D_RANKING FROM EMP ORDER BY SAL 
    ```

    

- ROW_NUMBER

  - ```SQL
    SELECT ENAME, SAL, RANK () OVER (ORDER BY SAL ) AS RAKING, DENSE_RANK() OVER(ORDER BY SAL DESC) AS D_RANKING, ROW_NUMBER() OVER(ORDER BY SAL DESC) AS ROW_NUM FROM EMP ORDER BY SAL 
    ```

- ```SQL
  탑 5만 고르시오 
  SELECT ENAME, SAL, ROW_NUM FROM (SELECT ENAME, SAL, ROW_NUMBER() OVER (ORDER BY SAL DESC) AS ROW_NUM FROM EMP ) WHERE ROW_NUM <= 5
  ```

- ```SQL
  토탈 () 중에 탑 5를 표시하시오
  SELECT ENAME, SAL, RANK,(SELECT COUNT(*) FROM EMP ) AS TOTAL FROM (SELECT ENAME, SAL, RANK() OVER (ORDER BY SAL DESC )AS RANK FROM EMP ) 
  ```



- #### ROLLUP

  - 출력된 결과들의 집계를 표현.

  - ```SQL
    SELECT JOB, SUM(SAL) FROM EMP GROUP BY ROLLUP(JOB) 
    ```

  - ```SQL
    SELECT JOB,AVG(SAL), SUM(SAL) FROM EMP GROUP BY ROLLUP(JOB) 
    ```

  - 

#### DDL 



### JAVA

#### JDBC (java data base connectivity)









