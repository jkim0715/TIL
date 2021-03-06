연습문제 

- 연도별 직업별 SAL평균 

  1981년도에 입사한 사람중 부서 10,20 중에서 SAL 평균 1500 이상인 사람의 평균SAL을 출력하세요

- ``` SQL
  SELECT TO_CHAR(HIREDATE,'YYYY') AS YEAR,JOB, ROUND(AVG(SAL),1) FROM EMP GROUP BY TO_CHAR(HIREDATE,'YYYY'),JOB HAVING TO_CHAR(HIREDATE,'YYYY') IN ('1981') AND AVG(SAL) >1500 ORDER BY JOB
  ```



- 입사한 달로 사원들을 그룹짓고

  DEPTNO가 20,30 이고 4, 5, 12월에 입사한 사원들의 평균임금을 출력한다.

  MONTH 오름차순으로 출력한다.

  

- ``` SQL 
  SELECT TO_CHAR(HIREDATE,'MM') AS MONTH, AVG(SAL) FROM EMP GROUP BY TO_CHAR(HIREDATE,'MM') HAVING TO_CHAR(HIREDATE,'MM') IN('04','05','12') ORDER BY MONTH
  ```





- 직업별 입사 월별 월급의 최대값을 구하시오.

  단 이름에 S가 들어간 사람을 대상으로 하고

  입사 월이 12월인 사람을 대상으로 하시오.

  - ``` SQL
    SELECT JOB, TO_CHAR(HIREDATE,'MM') AS MONTH , MAX(SAL) FROM EMP WHERE ENAME LIKE '%S%' GROUP BY JOB ,TO_CHAR(HIREDATE,'MM') HAVING TO_CHAR(HIREDATE,'MM') IN('12') 
    ```

- 고용 월별, 직업별로 SAL+COMM의 평균을 출력하고

  SAL+COMM의 평균이 2000이상이며

  ENAME에 A가 있는 경우를 고용 월별을 기준으로 

  내림차순으로 정렬하시오
  - ``` SQL 
    SELECT JOB, TO_CHAR(HIREDATE,'MM') AS MONTH, AVG(SAL + NVL(COMM,0)) FROM EMP WHERE ENAME LIKE '%A%' GROUP BY JOB, TO_CHAR(HIREDATE,'MM') HAVING AVG(SAL + NVL(COMM,0))> 2000 ORDER BY MONTH DESC;
    ```

- 
  EMP 테이블에서 JOB별, MGR별 ENAME을 구하시오. 

  단, HIREDATE가 9월, 12월이며, MGR이 7698이다.

  그리고 JOB 오름차순으로 정렬하시오. 

  - ``` SQL 
    SELECT JOB, MGR, ENAME FROM EMP WHERE TO_CHAR(HIREDATE,'MM') IN('09','12') GROUP BY JOB, MGR, ENAME HAVING MGR IN ('7698') ORDER BY JOB 
    ```

- JOB 별 SALARY의 평균을 구하고 평균이 2000이상인 그룹중에서 

  가장 큰 평균을 갖은 그룹과 가장 작은 평균을 갖은 그룹의 액수를 각각 출력하시오.

  - ``` SQL
    SELECT MAX(A), MIN(A) FROM (SELECT JOB, AVG(SAL) AS A FROM EMP GROUP BY JOB HAVING AVG(SAL) >2000 )
    ```



- 부서별 월급의 평균을 조회하는 VIEW를 작성하시오 

  - ``` SQL
    CREATE VIEW AVGSALVIEW(DEPTNO, AVGSAL) AS SELECT DEPTNO, AVG(SAL) FROM EMP GROUP BY DEPTNO
    ```

- DALLAS의 있는 사람의 이름을 조회하시오

  - ```SQL
    SELECT DEPTNO FROM DEPT WHERE LOC = 'DALLAS'
    
    SELECT ENAME FROM EMP WHERE DEPTNO = 20
    ```

- FOREIGN KEY... 

- ```SQL
  CREATE TABLE ITEM( ID VARCHAR2(10), NAME VARCHAR2(20), CATE NUMBER(10))
  CREATE TABLE CATEGORY( NO MUMBER(20), NAME VARCHAR2(20))
  
  ALTER TABLE ITEM ADD CONSTRAINT PRIMARY KEY(ID)
  ALTER TABLE CATEGORY ADD CONSTRAINT PRIMARY KEY(ID)
  ```

- ``` SQL
  CREATE TABLE ITEM( ID VARCHAR2(10), NAME VARCHAR2(20), CATE NUMBER(10))
  CREATE TABLE CATEGORY( NO NUMBER(20), NAME VARCHAR2(20))
  
  
  ALTER TABLE ITEM ADD PRIMARY KEY(ID)
  ALTER TABLE CATEGORY ADD PRIMARY KEY(NO)
  
  INSERT INTO CATEGORY VALUES(100,'의류')
  INSERT INTO CATEGORY VALUES(200,'잡화')
  INSERT INTO CATEGORY VALUES(300,'소품')
  
  DELETE FROM ITEM WHERE ID = 'IT01'
  
  ALTER TABLE ITEM ADD FOREIGN KEY(CATE) REFERENCES CATEGORY(NO)
  
  ```

- ``` SQL
  SELECT ENAME, SAL, AVG(SAL) FROM EMP  -- 불가능
  SELECT ENAME, SAL , (SELECT AVG(SAL) FROM EMP ) FROM EMP ; --모든 ROW에 평균표시.
  ```



- JOB 별 평균 월급보다 많이 받는 사람 을 조회하시오 

  - ``` SQL
    SELECT JOB, ENAME, SAL FROM EMP e1 WHERE SAL >(
    SELECT AVG(SAL) FROM EMP e2 WHERE e1.JOB = e2.JOB GROUP BY JOB ) 
    ```

- 부서별 월급이 가장 많은사람의 DEPTNO, ENAME,SAL을 조회하시오

  - ```SQL
    SELECT DEPTNO,ENAME,SAL FROM EMP E1 WHERE SAL >= (SELECT MAX(SAL) FROM EMP E2 WHERE E2.DEPTNO = E1.DEPTNO GROUP BY DEPTNO)
    ```

- 'CHICAGO ' 지역의 평균 월급보다 높은 사람들의 JOB 별 SAL 를  (JOB,ENAME,YYYY,SAL) 로 나타내시오

  - ```SQL
    SELECT JOB, ENAME , TO_CHAR(HIREDATE,'YYYY') AS YEAR,SAL FROM EMP WHERE SAL > (SELECT AVG(SAL) FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND D.LOC IN ('CHICAGO') GROUP BY D.LOC) ORDER BY SAL DESC 
    ```



- 지역별 ... (강진이 문제 )

  - ``` SQL 
    1. 지역별 평균
    SELECT AVG(SAL), LOC AS A FROM EMP E, DEPT D  WHERE E.DEPTNO = D.DEPTNO GROUP BY LOC
    
    2.지역별 평균중 MAX 지역
    SELECT MAX(A) FROM (SELECT AVG(SAL), LOC AS A FROM EMP E, DEPT D  WHERE E.DEPTNO = D.DEPTNO GROUP BY LOC)
    
    SELECT MIN(SAL)AS D FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND D.LOC = (SELECT MAX(A) FROM (SELECT AVG(SAL), LOC AS A FROM EMP E, DEPT D  WHERE E.DEPTNO = D.DEPTNO GROUP BY LOC))
    
    3. 지역별 평균중 MIN지역 
    SELECT MIN(A) FROM (SELECT AVG(SAL), LOC AS A FROM EMP E, DEPT D  WHERE E.DEPTNO = D.DEPTNO GROUP BY LOC)
    
    SELECT MAX(SAL) AS C FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND D.LOC=(SELECT MIN(A) FROM (SELECT AVG(SAL), LOC AS A FROM EMP E, DEPT D  WHERE E.DEPTNO = D.DEPTNO GROUP BY LOC))
    
    
    SELECT MAX(C) FROM (
    SELECT MAX(SAL) AS C FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND D.LOC=(SELECT MIN(A) FROM (SELECT AVG(SAL), LOC AS A FROM EMP E, DEPT D  WHERE E.DEPTNO = D.DEPTNO GROUP BY LOC))
    UNION
    SELECT MIN(SAL)AS D FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND D.LOC = (SELECT MAX(A) FROM (SELECT AVG(SAL), LOC AS A FROM EMP E, DEPT D  WHERE E.DEPTNO = D.DEPTNO GROUP BY LOC)))
    
    
    ```

- 지역별 입사일이 가장 늦은 사원의 정보를 출력 하시오 LOC,ENAME,HIREDATE 

  - ``` SQL
    SELECT D.LOC,E.ENAME, E.HIREDATE FROM EMP E, DEPT D WHERE E.DEPTNO= D.DEPTNO 
    AND HIREDATE IN (SELECT MAX(HIREDATE) FROM EMP E1, DEPT D1
    WHERE D1.DEPTNO = E1.DEPTNO 
    AND D.LOC = D1.LOC
    GROUP BY D.LOC) ORDER BY D.LOC
    ```

- 내가 속한 각 부서별 월급 평균 이상으로 받는 직원들을 조회하시오.

  - ``` SQL
    SELECT ENAME, SAL FROM EMP E1 WHERE SAL > (SELECT AVG(SAL) FROM EMP E2 WHERE E1.DEPTNO = E2.DEPTNO GROUP BY DEPTNO)
    ```

- 내가 속한 각 부서별 월급을 가장 많이 받는 직원들을 조회하시오.

  - ``` SQL
    SELECT DEPTNO,ENAME, SAL FROM EMP E1 WHERE SAL >= (SELECT MAX(SAL) FROM EMP E2 WHERE E1.DEPTNO = E2.DEPTNO GROUP BY DEPTNO)
    ```

- 내가 속한 각 부서별 월급을 가장 많이 받는 직원들을 조회하시오. 단 부서명과 지역을 출력하시오 

  - ```SQL
    SELECT E.DEPTNO,E.ENAME,E.SAL,D.DNAME,D.LOC FROM EMP E, DEPT D 
    WHERE E.DEPTNO=D.DEPTNO AND SAL >= (SELECT MAX(SAL) FROM EMP E2 
    WHERE E.DEPTNO = E2.DEPTNO GROUP BY DEPTNO)
    ```

- SCOTT 이 소속된 부서의 직원 정보를 조회하시오

  -  ```SQL
    SELECT E.DEPTNO,E.ENAME,E.SAL,D.DNAME,D.LOC FROM EMP E, DEPT D 
    WHERE E.DEPTNO=D.DEPTNO AND E.DEPTNO IN(SELECT DEPTNO FROM EMP WHERE ENAME = 'SCOTT')
    ```

- DALLAS에 있는 직원의 정보를 조회 하시오 

  - ```SQL
    SELECT E.DEPTNO, E.ENAME, E.SAL, D.DNAME, D.LOC FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND D.DEPTNO IN (SELECT DEPTNO FROM DEPT WHERE LOC = 'DALLAS')
    ```

  ##### EXIST 사용 버전

  - ```SQL
    SELECT E.DEPTNO, E.ENAME, E.SAL, D.DNAME, D.LOC FROM EMP E, DEPT D WHERE E.DEPTNO = D.DEPTNO AND EXISTS (SELECT D2.DEPTNO FROM DEPT D2, EMP E2 WHERE D2.DEPTNO = E2.DEPTNO AND LOC = 'DALLAS' AND E.DEPTNO = E2.DEPTNO)
    ```





- MANAGER인 직원을 조회 하시오 

  - ```SQL
    SELECT ENAME FROM EMP WHERE JOB = 'MANAGER'
    ```

- JONES가 속한 JOB 의 직원을 조회하시오 

  - ``` SQL
    SELECT ENAME FROM EMP WHERE JOB IN (SELECT JOB FROM EMP WHERE ENAME ='JONES')
    ```

- EXISTS () 란 ?   ()가 항상 트루인 것에 대한 결과 물 이랄까.. 

  - ``` SQL
    SELECT ENAME FROM EMP E1 WHERE EXISTS (SELECT JOB FROM EMP E2 WHERE ENAME ='JONES' AND E1.JOB = E2.JOB)
    ```

- JONES가 속한 JOB 의 직원을 조회하시오. 단, 직원의 부서명과 지역을 출력하시오

  - ```SQL
    SELECT E1.ENAME,D.DNAME,D.LOC FROM EMP E1,DEPT D WHERE E1.DEPTNO = D.DEPTNO AND EXISTS (SELECT JOB FROM EMP E2 WHERE ENAME ='JONES' AND E1.JOB = E2.JOB)
    ```



#### VIEW 사용 해서 결합 

- ``` SQL 
  CREATE VIEW T_EMP(ENO, ENM,SAL,DNO)  AS ( SELECT EMPNO, ENAME, SAL, DEPTNO FROM EMP  )
  
  CREATE VIEW T_DEPT(DNO,DNM,LOC)  AS ( SELECT DEPTNO,DNAME,LOC FROM DEPT )
  
  CREATE VIEW T_SAL(ENO, ASAL) AS SELECT EMPNO, SAL*12+(NVL(COMM,0)*12) FROM EMP 
  
  ```

- 위 테이블을 사용하여 직원 정보를 출력하시오 ENO,ENM,SAL,ASAL,DNM,LOC

  - ``` SQL
    (여러개 결합..) ORACLE 용
    SELECT A.ENO,A.ENM,A.SAL,C.ASAL,B.DNM,B.LOC FROM T_EMP A,T_DEPT B,T_SAL C
    WHERE A.DNO = B.DNO AND A.ENO = C.ENO
    ```

  - ``` SQL 
    ANSI 표준 
    SELECT A.ENO,A.ENM,A.SAL,C.ASAL,B.DNM,B.LOC FROM T_EMP A INNER JOIN T_DEPT B ON (A.DNO = B.DNO) INNER JOIN T_SAL C ON (A.ENO = C.ENO)
    ```

  - ```SQL
    JONES 가 속한 부서원만 조회하시오
    SELECT A.ENO,A.ENM,A.SAL,C.ASAL,B.DNM,B.LOC FROM T_EMP A,T_DEPT B,T_SAL C
    WHERE A.DNO = B.DNO AND A.ENO = C.ENO AND A.DNO IN (SELECT DNO FROM T_EMP WHERE ENM = 'JONES')
    ```

  - ```SQL
    부서별 연봉의 평균보다 많이 받는 직원을 조회 
    SELECT E.ENO,E.ENM,E.SAL,A.ASAL,D.DNM,D.LOC FROM T_EMP E, T_SAL A, T_DEPT D WHERE E.DNO = D.DNO AND E.ENO = A.ENO AND  A.ASAL > (SELECT AVG(S1.ASAL) FROM T_EMP E1, T_SAL S1 WHERE E1.ENO = S1.ENO AND E.DNO =E1.DNO GROUP BY (E1.DNO)) 
     
    ```



``` SQL
직원의 정보를 출력하시오
EMPNO, ENAME, MNAME 을 출력하시오 
SELECT E1.EMPNO AS EMPNO,E1.ENAME AS ENAME, E2.ENAME AS MNAME
FROM EMP E1, EMP E2 WHERE E1.MGR = E2.EMPNO
```



```SQL


INSERT INTO EMP VALUES 
(8888,'KSK','SALESMAN',7839,TO_DATE('2019/06/05','YYYY/MM//DD'),4000,100,NULL)
```



## 윈도우 함수 

- ``` SQL
  SELECT ENAME, SAL, RANK () OVER (ORDER BY SAL ) AS RAKING FROM EMP ORDER BY SAL 
  ```

-  ``` SQL
  SELECT ENAME, SAL, RANK () OVER (ORDER BY SAL ) AS RAKING, DENSE_RANK() OVER(ORDER BY SAL DESC) AS D_RANKING FROM EMP ORDER BY SAL  
  ```

- ```SQL
  SELECT ENAME, SAL, RANK () OVER (ORDER BY SAL ) AS RAKING, DENSE_RANK() OVER(ORDER BY SAL DESC) AS D_RANKING, ROW_NUMBER() OVER(ORDER BY SAL DESC) AS ROW_NUM FROM EMP ORDER BY SAL 
  ```

- ``` SQL
  탑 5를 고르시오
  SELECT ENAME, SAL, ROW_NUM FROM (SELECT ENAME, SAL, ROW_NUMBER() OVER (ORDER BY SAL DESC) AS ROW_NUM FROM EMP ) WHERE ROW_NUM <= 5
  ```

- ``` SQL
  TOTAL 도 구하시오 
  SELECT ENAME, SAL, ROW_NUM,(SELECT COUNT(*) FROM EMP ) FROM (SELECT ENAME, SAL, RANK() OVER (ORDER BY SAL DESC )AS RANK FROM EMP ) WHERE RANK <= 5
  ```

- ```SQL
  월급 평균 까지 구하시오 
  SELECT ENAME, SAL, RANK,(SELECT COUNT(*) FROM EMP ) AS TOTAL,(SELECT AVG(SAL) FROM EMP) AS ASAL FROM (SELECT ENAME, SAL, RANK() OVER (ORDER BY SAL DESC )AS RANK FROM EMP ) 
  ```





```sql
SELECT e.ENO, e.ENM, e.SAL,s.ASAL,d.DNM,d.LOC FROM T_EMP e, T_DEPT d, T_SAL s
WHERE e.DNO = d.DNO AND e.ENO = s.ENO AND s.ASAL
```









``` SQL
3조) 직원들의 정보와 해당 직원의 상사 정보를 같이 출력하시오.

왼쪽이 부하직원들의 정보, 오른쪽은 상사의 정보. MGR은 상사의 EMPNO를 나타낸다고 가정한다
SELECT E1.EMPNO, E1.ENAME, E1.JOB, E1.MGR,E2.EMPNO, E2.ENAME, E2.JOB, E2.MGR FROM EMP E1 ,EMP E2 WHERE E1.MGR = E2.EMPNO
```





``` SQL
부서별 연봉의 평균 보다 많이 받는 직원을 구하고 연봉 순위를 매기시오.

T_EMP, T_SAL, T_DEPT를 이용하시오.
SELECT E.ENO, E.ENM, S.ASAL, D.DNM, D.LOC, RANK()OVER (ORDER BY ASAL DESC) AS RANKING FROM T_EMP E, T_DEPT D, T_SAL S
WHERE E.DNO = D.DNO AND E.ENO = S.ENO AND S.ASAL > ( SELECT AVG(S1.ASAL) FROM T_SAL S1, T_EMP E1 WHERE S1.ENO = E1.ENO  AND E.DNO = E1.DNO GROUP BY E1.DNO )
```



VIEW를 사용하여 SQL문을 작성한다.(T_EMP, T_DEPT)

RESEARCH부서 사람들의 월급 ROW_NUM을 출력하시오(내림차순으로



```SQL
4조) VIEW를 사용하여 SQL문을 작성한다.(T_EMP, T_DEPT)

RESEARCH부서 사람들의 월급 ROW_NUM을 출력하시오(내림차순으로
                                  
SELECT ROW_NUMBER() OVER(ORDER BY E.SAL DESC) AS ROW_NUM , E.ENO, E.ENM, E.SAL, D.DNM FROM T_EMP E, T_DEPT D WHERE E.DNO = D.DNO AND D.DNM ='RESEARCH'
                                  
표준 SQL 양식을 사용하여 작성하시오 각 부서의 평균 연봉 보다 많이 받는 사람의 지역별 총합과 지역별 총합의 총합을 출력하시오 
SELECT SUM(S.ASAL) AS ASALSUM, D.LOC FROM T_SAL S INNER JOIN T_EMP E ON (E.ENO= S.ENO) INNER JOIN T_DEPT D ON (E.DNO=D.DNO) WHERE S.ASAL>(SELECT AVG(S1.ASAL) FROM T_EMP E1 INNER JOIN T_SAL S1 ON(E1.ENO = S1.ENO) WHERE E1.DNO =E.DNO  )GROUP BY ROLLUP(D.LOC)
                                  
                                  
                                  
                                  
                                  

```





1조 ) 전체 연봉의 평균보다 많게 받는 직원의 ENO, ENM, SAL, ASA

L, RANK를 연봉이 높은순서로 정렬하여 조회하시오.

```sql
SELECT E.ENO,E.ENM,E.SAL,S.ASAL, DENSE_RANK() OVER (ORDER BY S.ASAL DESC) AS RANKING,DNM FROM T_EMP E, T_DEPT D, T_SAL S WHERE E.ENO =S.ENO AND E.DNO = D.DNO AND S.ASAL > (SELECT AVG(ASAL) FROM T_SAL)

-- KSK 안넣어서.. 답지랑 결과가 살짝 다르게 나옴 
```



ENO, EN, ASAL, DNM ,LO , RANK, TOTAL 을 출력하시오 부서별 월급의 평균 보다 많이 받는 직원을 출력하고, 순위를 2위까지만 출력한다. 단, DALLAS 지역 제외

```SQL
SELECT ENO, NE, DNM, LO, RANK FROM (SELECT E.ENO, E.ENM AS NE, D.DNM , D.LOC AS LO , RANK() OVER(ORDER BY S.ASAL DESC) AS RANK FROM T_EMP E, T_SAL S, T_DEPT D WHERE E.DNO=D.DNO AND E.ENO =S.ENO AND D.LOC NOT IN( 'DALLAS')  AND S.ASAL > (SELECT AVG(S1.ASAL) FROM T_SAL S1, T_EMP E1 WHERE S1.ENO = E1.ENO GROUP BY E.DNO)) WHERE RANK <= 2
```





6조문제

```sql

1번
SELECT RANK() OVER (ORDER BY S.ASAL DESC) AS RANKING , E.ENM AS EN, S.ASAL FROM T_EMP E INNER JOIN T_SAL S ON(E.ENO = S.ENO) WHERE ASAL >( SELECT AVG(S1.ASAL) FROM T_SAL S1)




2번

SELECT * FROM EMP WHERE EMPNO  = (SELECT MGR FROM EMP  GROUP BY MGR HAVING AVG(SAL) IN (SELECT MAX(AVSAL) FROM (SELECT E2.MGR,AVG(E2.SAL) AS AVSAL FROM EMP E, EMP E2 WHERE E.EMPNO = E2.MGR AND E.JOB IN ('MANAGER') GROUP BY E2.MGR) ) ) 



```





```SQL
5조

1번
UPDATE EMP SET DEPTNO = '40' WHERE ENAME ='KSK'

SELECT ENAME,ASAL,ROW_NUM,LOC,MGR FROM 
(SELECT E.ENAME, S.ASAL, ROW_NUMBER() OVER (ORDER BY S.ASAL DESC) AS ROW_NUM, D.LOC, E.MGR, E.EMPNO FROM EMP E, T_DEPT D, T_SAL S WHERE E.EMPNO = S.ENO AND E.DEPTNO = D.DNO AND E.MGR = (SELECT E1.EMPNO FROM EMP E1 WHERE E1.JOB IN ('PRESIDENT') ) AND D.LOC NOT IN(SELECT D2.LOC FROM EMP E2, T_DEPT D2 WHERE E2.DEPTNO = D2.DNO AND E2.JOB IN('PRESIDENT')) ) WHERE ROW_NUM =1


2번
SELECT ENAME, HIREDATE, ASAL, DNO, LOC, ROW_NUM, 
CASE WHEN ROW_NUM <=5 THEN '퇴직자' 
WHEN ROW_NUM >5 AND ROW_NUM <= 14 THEN '현직자' ELSE '신입사원' END AS STATE FROM (
    
SELECT E.ENAME, E.HIREDATE, S.ASAL, D.DNO, D.LOC, ROW_NUMBER() OVER (ORDER BY E.HIREDATE) AS ROW_NUM
 FROM EMP E, T_DEPT D,T_SAL S WHERE E.EMPNO = S.ENO AND E.DEPTNO = D.DNO 
    
    )






```















