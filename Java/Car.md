#### 20190523



##### Car

``` java
package car;

public class Car {

	
		
		//Simulation 하는 Car라고 가정
		
		
		
		// attribute
		private String name;
		private String color;
		private int fSize;
		private int cfSize;
		private int speed;
		private int maxSpeed;
		
		
		// constructor
		// 사실 필요하면 다 만들어놔도 됨
		// init 할 때 필요한 값을 constructor로 만들면 됨
		// car 의 instance를 생성할때 동작하는 함수
		// 이름이 같고 return type이 없는게 특징 --overload 
		// source - generate using field.
		
		
	
		public Car() {  //default constructor;  카트라이더 기본 차 같은거..
			this.name = "K1";
			this.color = "red";
			this.fSize = 50;
			this.maxSpeed =50;
			// this.cfSize = 0;  --이건 이미 default 값이 0이라 안써도되는듯
		}


		public Car(String name, String color, int fSize) {
			this.name = name;
			this.color = color;
			this.fSize = fSize;
		}
		
		// 이 차가 나올때 default 값
		public Car(String name, String color, int fSize, int maxSpeed) {
			this.name = name;
			this.color = color;
			this.fSize = fSize;
			this.maxSpeed = maxSpeed;
		}


		// 만약을 위해 쓰던 안쓰던 argument다포함하여 다만들어 놔버리기 
		public Car(String name, String color, int fSize, int cfSize, int speed) {
			this.name = name;
			this.color = color;
			this.fSize = fSize;
			this.cfSize = cfSize;
			this.speed = speed;
		}


		
		
		
		// function
		// 목적에 따라 변화
		
		
		// to String
		@Override
		public String toString() {
			return "Car [name=" + name + ", color=" + color + ", fSize=" + fSize + ", cfSize=" + cfSize + ", speed="
					+ speed + "]";
		}

		// getter setter
		public String getName() {
			return name;
		}


		public void setName(String name) {
			this.name = name;
		}


		public String getColor() {
			return color;
		}


		public void setColor(String color) {
			this.color = color;
		}


		public int getfSize() {
			return fSize;
		}


		public void setfSize(int fSize) {
			this.fSize = fSize;
		}


		public int getCfSize() {
			return cfSize;
		}


		public void setCfSize(int cfSize) 
				throws Exception {  // encap의 장정은 오류값을 방지할수있음
			if((this.cfSize+cfSize) > this.fSize) {
				throw new Exception();  
// 자바의 강점 Exception! --> return이 필요없음 뭔가 잘못되면 밑으로 안내려감
//				return;  
			}	
			this.cfSize += cfSize;
		}


		public int getSpeed() {
			return speed;
		}


		public void setSpeed(int speed) {
			if(this.maxSpeed < speed) {
				this.speed = this.maxSpeed;
				return;
			}
			this.speed = speed;
		}	

		public void go(int level) {  // int level -> 함수의 argument
			// 요구사항에 따라 코딩(우리가 개발하고 생각해야할 부분임)
			// 이걸 잘 설계 하는 사람이 전문가임..
			// let level 1~5
			// speed up 1:10km
			// fuel down 1L 10km
			switch(level) {
			case 1: 
				this.setSpeed(20);  // this.speed = 20;  이렇게 넣으면 오류들어갈수있음
				this.cfSize -= 1; 
				break;
			case 2:
				this.setSpeed(40);
				this.cfSize -= 2; 
				break;
			case 3:
				this.setSpeed(60);
				this.cfSize -= 3; 
				break;
			case 4:
				this.setSpeed(80);
				this.cfSize -= 4; 
				break;
			case 5:
				this.setSpeed(100);
				this.cfSize -= 5; 
				break;
			default:
				break;
				
			}
						
		}
		public void stop() {
			this.speed = 0;
			
		}
		


}

```



##### CarTest

``` java
package car;

public class CarTest {

	public static void main(String[] args) {
		
		Car car1 = new Car();
		System.out.println(car1.toString());
		
		
		
		try {		// surround w/ try/catch
			car1.setCfSize(50);	// 맞을때 그대로 실행
		} catch (Exception e) { // 틀릴때만 실행
			System.out.println("Too Much..");
			e.printStackTrace();
		}
		System.out.println(car1);
		
		car1.go(4);
		
		System.out.println(car1);
		
	}

}
```

``` java
package car;

public class CarTest2 {

	public static void main(String[] args) {
		Car cars [] = new Car[3];
		cars[0] = new Car("k1", "Yellow", 60, 90);
		
		cars[1] = new Car("k2", "red",70, 100);
		cars[2] = new Car("k3", "blue", 80, 80);
		
		for(Car c : cars) {
			try {
				c.setCfSize(70);
			} catch (Exception e) {
				System.out.println(c.getName()+" "+"Too Much Fuel Size..");
			}
			System.out.println(c);
		}

	}

}

```