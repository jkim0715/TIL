# R 데이터 분석

## 왜 R 인가?

R은 데이터 분석을 위한 통계 및 그래픽스를 지원하는 자유 소프트웨어 환경, 오픈소스.

1. 통계 분석 언어인 S에 기반을 두고 있음.

2. Data Mining, 같은 필드가 인기가 높을 때 인기가 많아지기 시작.

3. R은 컴퓨터 언어이자 다양한 패키지의 집합.

    다양한 라이브러리가 하루에도 수백개씩 생기곤 함.

4. 데이터 분석을 해낼 수 있음 ( 통계, 기계학습, 금융, 생물정보학, 그래픽스 등)

5. 통계를 기반으로 한 데이터 분석 

6. CRAN(http://cran.r-project.org/web/views/) 에서 다양 한 패키지들을 다운로드 받을 수 있음

7. R은 자바연동, 빅데이터 연동이 쉽다. (RHIVE를 이용하여 하이브 환경에서 R사용)

8. 원래 파이썬이 통계 기능쪽에서 R보다 딸렸는데 요즘은 여러가지 통계 라이브러리가 추가되었음

I. R설치하기

- http://www.r-project.org/
- Windows 용 다운로드 
- default값으로 설치



II. Rstudio

- IDE 툴 (Integrated  Development Environment)

- 이클립스 같은게 IDE 툴 임.
- rstudio.com 에서 다운로드
- free version download - Rstudio 1.2.1335 -Windows 7+(64bit)
- R이랑 연동해서 돌아감 



III. 활용

file - new project - new Directory - new project - (폴더 이름이랑 경로 설정하고 create)r

왼쪽 상단 + 눌러서 R Script 누르면 코드 입력 창 같은게 나오는데 이게 자바 같은거

1. run은 라인별 실행
2. source는 전체 실행 
3. console창은 리눅스 터미널과 명렁어 가 비슷하다

패키지 활용하기

패키지 다운로드

install.packages("randomForest")

패키지 저장 경로 :  C:\Program Files\R\R-3.6.1\library 밑에 저장됨



패키지 사용하기 

```R
library(randomForest)
```

마치 자바에서 외부라이브러리를 Import 해서 사용하는 것 과 같이 RScript 맨 윗부분에 작성





데이터 타입

I. 변수

변수이름 규칙

- 변수명 : 알파벳, 숫자, _(언더스코어),.(마침표)로 구성.  -(하이폰)은 사용 할 수 없다.
- . 으로 시작한다면 뒤에 숫자가 올 수 없다.

변수 값 할당

 = 대신 <- (화살표)를 씀

=은 명령 최상위 수준에서만 사용



함수 호출 시 인자 지정

R의 함수인자는 위치 또는 이름으로 지정 가능.

```
foo(a, b, c=1, d=2)

foo(1, 2, 3, 4)
foo(3, 4)
```

함수선언시 값을 넣어주면 default 값으로 들어가서 따로 c와 d를 인자로 전달하지않으면 각각 1 , 2로 지정되어 호출함.



--본격적인 R에서의 변수 타입--

R에서 데이터 타입의 기본은 벡터(Vector)



 스칼라 Scalar

- 숫자

- NA (Not Available)

  연산시 배제해야 함이 맞음.

   is.na 를 활용하여 ( NA가 저장되어 있으면 TRUE 아니면 FALSE를 리턴함)

- NULL

  변수가 초기화 되지 않았을 때 사용 NA와 구분하여 사용.

  대문자 NULL로 써야 함.

- 문자열

- 진리값

  

팩터 (Factor) 

- 범주형 데이터 자료를 표현하기 위한 데이터 타입.

- ```
  sex <- factor("m",c("m","f"))
  
  sex
  [1] m
  
  Levels: m f
  ```

  



벡터

다른언어에서 배열 개념

Example)

```javascript
#배열 선언  score
score <- c(100,90,80);  

#배열 컬럼지정
names(score) <-c("lee","kim","han");

#score 출력
print(score);

#배열의 첫번째 출력 (컬럼이랑 같이 출력 됨)
print(score[1]);

#배열 안 합산값 출력
print(sum(score));

#컬럼 "lee"의 값 출력
print(score["lee"]);

#1~10까지 배열 v1으로 선언
v1 <- c(1:10);

#배열 첫번째 값 출력
print(v1[1]);

#배열 v1에서 열번째 값 뺴고 출력
print(v1[-10])

#배열 인자값 카운트
print(NROW(v1))
print(length(v1))

#5~8번쨰 인자값 출력
print(v1[5:8]);

```



두개 이상일 떄는 무조건 c (vector)를 이용해야 한다.



벡터 연산





리스트 

R에서의 리스트는 Key Value를 의미함



행렬

대부분의 데이터는 정방행렬 형태일 것.

