#### Array

``` java
int a = {3,4,5};
String s[] = new String [3];

String str = "Multi_Campus"
    
    char c = str.toCharArray();

system.out.println(Arrays.toString(c));


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

