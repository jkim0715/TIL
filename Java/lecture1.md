변수와 메서드 

#### 선언위치에 따른 변수의 종류

- 클래스 변수 

  ``` java
  public static int cnt = 0;		//모든 인스턴스가 공통된 변수를 공유.
  Account.cnt  					//클래스명.변수로 direct로 변수를 불러올 수 있음.
  // static 함수 안에서 사용되는 변수는 static 변수 (클래스 변수) 여야한다.
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

  



### 메서드 (Method)

#### 메서드를 사용하는 이유

- 높은 재사용성 (reusability)
- 중복된 코드의 제거
- 프로그램의 구조화



#### 메서드의 선언과 구현

- 메서드 선언부
- 매개변수 선언 
- 매서드의 이름
- 반환타입
- 메서드의 구현부
- return문
- 지역변수
  - 초기화 필요

### V. 메서드의 호출

### VI. return문

- void 는 return 생략 가능. 
  - 모든 함수는 return 이 있어야 끝이 난다. void 는 사실 return 이 있는거임
  - if 문 안에서도 return가능

### JVM의 메모리 구조

- 메서드 영역
- 힙
- 호출스택

### 재귀호출(resursive call)

- ex) factorial 계산 **n!** 계산

  ``` java
  private static int factorial(int n) {
  		int result =0;
  		if(n ==1) {
  			return 1;
  		}else {
  			result = n*factorial(n-1);	
  		}
  		return result;
  	}
  ```

- ex) power

  ``` java
  private static int cub(int x, int n) {
  		int result =0;
  		if(n==1) {
  			return x;
  		}else {
  			result = x * cub(x,n-1);
  		}
  		return result;
  	}
  ```

### 클래스 메서드 와 인스턴스 메서드

- 인스턴스 메서드 : 인스턴스 변수와 관련된 작업을 하는, 즉 메서드의 작업을 수행하는데 인스턴스 변수를 필요로 하는 메서드이다.
- 클래스 메서드 : 인스턴스와 관계없는 (인스턴스 변수나 인스턴스 메서드를 사용하지 않는) 메서드
  - 클래스를 설계할때 멤버변수 중 모든 인스턴스에 공통으로 사용하는 것에 static을 붙인다.
  - 클래스 변수는 인스턴스를 생성하지 않아도 사용가능
  - 클래스 메서드는 인스턴스 변수를 사용불가
  - 메서드 내에서 인스턴스 변수를 사용하지 않는다면, static을 붙이는 것을 고려한다

### 오버로딩

- 함수이름이 같지만 argument는 달라야함 . return type은 무관하다.

  ``` java
  	public Calc() {					
  	}
  
  	public Calc(int[] data) {		//함수 이름은 같지만 매개변수의 개수 또는 타입이다름
  		this.data = data;
  	}
  ```

   

## 생성자

- 인스턴스 변수를 초기화 한다.

```java
Card c = new Card();
```





## 변수의 초기화 



### 초기화 블럭

``` java
//attribute
		private int defaultSize =100;
		private static int serial =1;
//initialization block -- 
		{
			cfSize = defaultSize *2;		// new Car만들어질때마다 실행
			cfSize++;
		}
		static {
			serial *= 1000;      			// 한번만 실행
		}
//constructor
		public Car(){
           
        }
```







