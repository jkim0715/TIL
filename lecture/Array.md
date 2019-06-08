#### Array

- 배열은  같은 타입의 여러 변수를 하나의 묶음으로 다루는 것.
- 인덱스(Index) 의 범위는 0부터 배열 길이 -1까지.
- 배열의 길이는 변경 불가능.. 지우고 새로 만들어야 한다.

``` java

int a = {3,4,5};
String s[] = new String [3];

String str = "Multi_Campus"
    
    char c = str.toCharArray();

system.out.println(Arrays.toString(c));
// 예외적으로 배열 타입이 Char인 경우  Arrays.toString 없이 sysout(c) 해도 정상적으로 출력 됨.


int a [] = new int [100];		// 100명의 투표 
		//1~4 까지의 숫자를 랜덤하게 배열에 입력
		Random r= new Random();
		int sum = 0;
		double avr = 0;
		for (int in =0; in <a.length; in++) {
			a[in]= r.nextInt(4)+1; // 투표번호 1~4
			sum += a[in];
			avr = (double)sum / a.length;
	}
```



- 복사는 for문을 돌리는 것 보다 

  - ```java
    System.arraycopy(); 를 사용하는 것이 효율적이다.
    ```

- ```java
  char charAt(int index)    // 문자열에서 해당 위치(index)에 있는 문자를 반환한다.
      int length()			//문자열의 길이를 반환한다.
      String substring(int from ,int to)  	// 해당범위 from ~ to 에 있는 문자열 반환
      boolean equals(String str) //문자열의 내용이 같은지 확인한다. 같으면 결과는 ture 틀리면 false.
      char[] toCharArray() // 문자열을 char[] 로 변환해서 반환
  ```

- 