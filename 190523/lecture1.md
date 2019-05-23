## 변수와 메서드 

#### 선언위치에 따른 변수의 종류

- 클래스 변수 

  ``` java
  public static int cnt = 0;		//모든 인스턴스가 공통된 변수를 공유.
  Account.cnt  					//클래스명.변수로 direct로 변수를 불러올 수 있음.
  ```

- 인스턴스 변수

  ``` java
  private int balance;
  ```

- 지역 변수 

  ```java
  (){
      int i =0;		// 매서드 내에 선언되어 매서드 안에서만 사용가능
  }
  ```

  