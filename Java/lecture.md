

``` java
		
		trnasactionStart();
		dao.insert(v);
		transactionEnd();
```

``` java
		
		transactionStart();
		try {
			dao.insert(v);
		}catch(Exception e) {
			throw e;
		}finally {
			transactionEnd();
		}
```



#### Interface

- 일종의 추상 클래스
- 기능만 정의



###### ex) shop

``` java
package inter;

public interface Shop {
	public abstract void register();  //  abstract 생략 가능.
	public void login();
	public void logout();
	public void order();	

}
```

- 인터페이스를 쓰는 이유 
  - 레고 블럭마냥 끼웟다 뺏다 할 수 있음.
  - 여러가지의 속성을 주입할 수 있다. (다중상속 가능)
  - 독립적인 작업가능.

