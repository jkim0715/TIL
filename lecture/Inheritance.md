## Inheritance



### StarUML

Gerneralization - 상위에 잇는걸 상속받는다

- generalize 하다보니 추상 클래스가 나올 수 밖에 없었다.

isAbstract -- 추상 구현





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

