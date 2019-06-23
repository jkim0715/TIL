## Inheritance

- Polymorphism - 의미는 같지만 형태는 다르다.;;
  - 사용하는 이유 : 사용자는 하나의 parent 클래스(표준) 만 알면 그 밑의 자손클래스들을 이름만 알아도 자유롭게 사용가능

### StarUML

Gerneralization - 상위에 잇는걸 상속받는다

- generalize 하다보니 추상 클래스가 나올 수 밖에 없었다.

isAbstract -- 추상 구현

- Dependency  -- parents 하나만 보고 작성





### Java

``` java
	extends Employee

	public Manager(String id, String name, double salary, String dept, double incentive) {
		super(id, name, salary, dept);		// Constructor는 상속이 안되기 때문에 선언
		this.incentive = incentive;
	}

//Heterogeneous Collection
		Shape s[] = new Shape[3];
		s[0] = new Circle (new Point(1,1),5);
		s[1] = new Rectangle (new Point(2,2),5,6);
		s[2] = new Triangle (new Point(3,3),5,6);
		

// Polymorphism 다형성
		for(Shape sh :s) {
			sh.move(5,5);
			if(sh instanceof Circle) {
				Circle c = (Circle)sh;	// shape sh를 Circle로 type Casting
				c.fillColor("red");
			}
			System.out.println(sh.toString());
			//System.out.println(sh.getArea());
			//System.out.println(sh.getCircum());
		}

```

``` java
if(sh instanceof Circle){		// 만약 sh가 Circle 이라면 
    
}
```

 #### 상속관계 (is a..)

``` java
class Circle{
    Point c = new Point();
}

class Circle extends Point{
    int r;
}
```



#### 포함관계 (has a)

``` java
class Circle{
    int x;
    int y;
    int r;
}

class Circle{
    Point c = new Pount();
    int r;
}
```

#### 오버로딩 vs 오버라이딩

- 오버로딩 (overloading) : 기존에 없는 새로운 메서드를 정의하는 것 (new)
- 오버라이딩 (overriding) : 상속받은 메서드의 내용을 변경한느 것 (change, modify)



#### Super

- 자손 클래스에서 조상 클래스로부터 상속받은 멤버를 참조하는데 사용되는 참조 변수.

``` java
class SuperTest{
    public static void main(String arg[]){
        Child c = new Child();
        c.method();
    }
}

class Parent{
    int x = 10;
}

class Child extends Parent{
    int x =20;
    void method(){
        sysout(x);			// x = 20
        sysout(this.x);		// x = 20
        sysout(super.x);	// x = 10
    }
}
```

- 변수뿐만 아니라 method 역시 호출 가능.

``` java
class Point {
    int x;
    int y;
    String getLocation(){
        return "x:"+x+", y:"+y;
    }
}

class Point3D extends Point{
    int z;
    String getLocation(){
        return super.getLocation()
    }
}
```

### 객체지향 

아래 코딩이 되는 이유는 OOP2

- user 를 object로  받을 수 있다.  왜냐면 object > user 개념이기 때문에.

``` java
public Object select(Object obj){
    User user = null;
    
    return user;
}
```



#### Generics

- 클래스 내부에서 사용할 데이터 타입을 외부에서 지정.





#### Collection API

- Set -  중복 불가,  순서 없음

``` java
HashSet<Object> set0 = new HashSet<>();		//전체
		HashSet<Integer> set = new HashSet<>();
	
		
		Random r= new Random();
		while(true) {
			set.add(r.nextInt(45)+1);
			if(set.size() == 6) {
				break;
			}
		}
System.out.println(set.toString());// 보면 중복 허용안함...순서마구잡이
```



- List  - 순서 있음, 속도 느림

```java
import java.util.Arraylist;

public static main (String[] args){
//ArrayList 선언
    ArrayList al = new ArrayList();
// 순서대로 들어간다, 넣을떈 .add();
// add() 안에 인자는 object 로 저장됨.    
    al.add("one");
    al.add("two");
    al.add("three");
// 출력시 .get();    
    for(int i=0; i<al.size(); i++){
        System.out.println(al.get(i));
//Object 타입을 String 타입인 변수에 넣으려고 하면 에러남        
        String value = al.get(i);
// 따라서 형변환이 필요함
        String value = (String)al.get(i);
    };
}
```



``` java
ArrayList<Integer> list = new ArrayList<>();
		
		Random r= new Random();
		while(true) {
			list.add(r.nextInt(45)+1);
			if(list.size() == 10) {				//10개를 넣겟다 
				break;
			}
		}
		System.out.println(list.toString());	
```



- HashMap < Key, Value >  
  - 1번 박 2 번 최 3번 이 ... 저장
    - 1번 호출하면 박이나옴

Set,List,Hash - 이런애들은 사실 Shape 같이 최상위 클래스임.. 그밑에 실제로 구현을 위한 클래스들이 있음.