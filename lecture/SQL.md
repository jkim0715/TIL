## SQL

- data를 조작하고 어떻게 연동하는가..?  에 대해 공부



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



## SQL 

#### 종류

## DDL(Data Definition Language) :데이터 정의언어

- #### CREATE

``` SQL
CREATE TABLE T_USER(
	ID VARCHAR2(10),    //(10)10자리까지 가능
    PWD VARCHAR2(10),	//VARCHAR2 는 버전..
    NAME VARCHAR2(20)
);

DESC T_USER; 	// 만든 테이블 정보 확인 

------------------------------------------------------------------

CREATE TABLE T_PRODUCT(
	ID VARCHAR2(10) PRIMARY KEY,  // 중복방지
    NAME VARCHAR2(20) NOT NULL,		//상품 이름없음 데이터 못드가게 에러띄움
    PRICE NUMBER(10,1) NOT NULL, // 오라클에서 숫자표현 방법. 숫자10자리, 소수 1째자리
    REGDATE DATE	NOT NULL	// 날짜형

);
```

- #### DROP

``` sQL
DROP TABLE T_USER; 	//테이블 뿐만 아니라 데이터까지 싹다날림.. 잘못하면 소송감임 
```



- #### ALTER

``` SQL
ALTER TABLE T_PRODUCT ADD (REGDATE DATE);// 제약조건 변경, 컬럼 추가
ALTER TABLE T_PRODUCT DROP (REGDATE);// 빼기
ALTER TABLE T_PRODUCT ADD PRIMARY KEY (ID); // ID에 PRIMARY KEY 추가
ALTER TABLE T_PRODUCT MODIFY(NAME CHAR(10)); //타입 바꾸기 VARCHAR -> CHAR
ALTER TABLE T_PRODUCT MODIFY(NAME NULL);  // 제약조건 바꿀 수 있다,
ALTER TABLE T_PRODUCT RENAME COLUMN NAME TO UNAME; // 이름을 NAME -> UNAME 으로 바꾸기
ALTER TABLE T_PRODUCT RENAME TO PRODUCT; //테이블 이름 바꾸기.
ALTER TABLE T_USER MODIFY (NAME UNIQUE);  유니크만들기(PRIMARY KEY 말고)같은이름 불가
```





## DML(Data Manipulation Language):데이터 조작언어

- #### SELECT

``` SQL
SELECT * FROM T_PRODUCT;
```



- #### INSERT

``` SQL
INSERT INTO T_USER(ID,PWD,NAME) VALUES('','','');
INSERT INTO T_USER VALUES('ID01','PWD01','이말숙'); //VALUES 앞에다 컬럼명 안써도 됨

INSERT INTO T_PRODUCT VALUES ('P02','PANTS2','20000',SYSDATE);
//중간에 돈 20000 뺴고 넣기
INSERT INTO T_PRODUCT (ID, NAME, REGDATE) VALUES ('P02','PANTS2',SYSDATE); 
// 이렇게 하면 나중에 분석 연산할때 매우 위험 !
ALTER TABLE T_PRODUCT MODIFY (PRICE DEFAULT 1000); // 디폴트값 줘서 빈값 10000 수렴.

```

- #### UPDATE

``` SQL
UPDATE T_USER SET PWD = '111';  ///싹다 111 로 바꿈
UPDATE T_USER SET PWD = '111', NAME= '공말숙'; // 여러개
UPDATE T_USER SET PWD = '111',NAME= '공말숙' WHERE ID = 'ID03';
```

- #### DELETE

``` SQL
DELETE FROM T_USER					// 싹다 삭제
DELETE FROM T_USER WHERE ID = 'ID05'  // WHERE 로 조건 설정
TRUNCATE <테이블명>;  테이블의 모든 데이터를 삭제.
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

  



#### DDL 



### JAVA

#### JDBC (java data base connectivity)