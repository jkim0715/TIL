# 객체지향언어

## I.역사

- 현실 세계의 어떤 내용을 집어넣기 위해 탄생.
- 최초의 객체지향언어 (Simula)
  - 언어라기 보다는 개념에 가까웠음

- COBOL - 아직까지 증권, 은행에서 사용됨
- 현실세계의 요구사항들을 절차적 언어로는 극복하기 어렵다는 문제발생
  - 객체지향언어를 이용한 개발방법론 등장	

-  1995년 말에 java가 발표되고 1990년대 말에 인터넷이 유행하면서 객체지향언어가 프로그램의 주류로 자리잡음.

> ​	OOAD (Object Oriented Analisys and Design) 
>
> - UML
>
> > 1995-2000  
> >
> > OOP (Object Oriented Programming)  
> >
> > - java or c++
> >
> >   



## II.객체지향언어

- 코드의 재사용성의 높다
- 코드의 관리가 용이하다
- 신뢰성이 높은 프로그래밍을 가능하게 한다



객체지향개념을 학습할 때 재사용성과 유지보수 그리고 중복된 코드의 제거, 이 세가지 관점에서 봐라.

일단 프로그램을 기능적으로 완성한 다음 어떻게 하면 보다 객체지향적으로 코드를 개선할지 고민.



# 클래스와 객체

## I. 클래스와 객체의 정의와 용도

#### 클래스

- 클래스의 정의 : 클래스란 객체를 정의해 놓은 것이다.
- 클래스의 용도 : 클래스는 개체를 생성하는데 사용된다.



#### 객체

- 객체의 정의 : 실제로 존재하는 것. 사물 또는 개념
- 객체의 용도 : 객체가 가지고 있는 기능과 속성에 따라 다름.
- 유형의 객체 : 책상,의자,자동차,TV와 같은 사물
- 무형의 객체 : 수학공식, 프로그램 에러와 같은 논리나 개념



## II.객체와 인스턴스



클래스 ----->(인스턴스화)---> 인스턴스(객체)



## III 객체의 구성요소

- 속성 (property): 멤버변수 (member variable), 특성(attribute), 필드(field), 상태(status)
- 기능(function) :메서드 (method), 함수 (function), 행위(behavior)



## IV 인스턴스의 생성과 사용

``` java
클래스명 변수명;			// 클래스의 객체를 참조하기 위한 참조변수를 선언
변수명 = new 클래스명();	// 클래스의 객체를 생성 후, 객체의 주소를 참조변수에 저장

TV t;					// Tv클래스 타입의 참조변수 t를 선언
t = new Tv();			// Tv인스턴스를 생성한 후, 생성된 Tv 인스턴스의 주소를 t에저장
```

- 여러개의 객체를 생성 할 땐 객체배열을 통하여 생선한다.

  - ```java
    Tv[] tvArr = new Tv[3];
    
    for(i = 0; i < 3; i++){
        tvArr[i] = new TV();
    }
    ```

  - 



##### oop



- OOAD -UML
- oop - Java or C++
- Class and Object
- attribute, constructor, function

##### oop2

- Encapsulation

  - modifier

    - private  & public  

    - ``` java
      private String color;
      private boolean power;  
      public int channel;
      ```

  - Getter & Setter 

    - ``` java
      public String getColor() { //게터  string 값이 리턴
      		return color;  // this.  이 생략
      	}
      	public void setColor(String color) { // 세터 없애면 encap 을 더 강력하게 함
      		// 숫자 못들어오게 한다 
      		// 컬러는 몇개로 정해서 동작한다.
      		if(color.equals("")|| color == null) {
      			return; //함수 끝내기 
      		}
      		this.color = color;
      	}
      ```

- Inheritance

- Polymorphism

  

- Abstration
- Override
- Overload





### StarUML

- 현실 - RFP - OOAD - OOP



