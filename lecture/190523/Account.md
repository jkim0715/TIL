### Bank

#### Acccount



``` java
package bank;

public class Account {
	private String owner;
	private String accNum;
	private double balance;
	
	public static int cnt = 0;  /// static -- 클래스 변수 메모리 method에 cnt들어감
	
	
	
	//사실 계좌 만들라면 정보 필요해서 default 값을 쓸필요가 없지만 걍 만듬
	public Account() {
	}

	public Account(String owner, String accNum, double balance) throws Exception {
		if(accNum.length() != 5 ) {
			throw new Exception("E1000");  // constructor에도 Exception 쓸수 있음. 
		}
		this.owner = owner;
		this.accNum = accNum+cnt;
		this.balance = balance;
		cnt++;
	}


	public String getOwner() {
		return owner;
	}

	public String getAccNum() {
		return accNum;
	}

	public double getBalance() {
		return balance;
	}

	@Override
	public String toString() {
		return "Account [owner=" + owner + ", accNum=" + accNum + ", balance=" + balance + "]";
	}
	
	public void withdraw(double money) throws Exception {
		if(money <= 0) {
			throw new Exception("E0001"); // exp(메시지 보낼수도있음);
		}
		
		if(this.balance < money) {
			throw new Exception("E0002");  
		}
		this.balance -= money;
	}
	
	public void deposit(double money) throws Exception {
		if(money <= 0) {
			throw new Exception("E0001"); 
		}
		this.balance += money;
	}
}

```



##### AccountTest

``` java
package bank;

public class AccountTest {

	public static void main(String[] args) {
		Account acc1 = null, acc2 = null;	// ref 의 초기값은 null이다~
		
		try {
			acc1 = new Account("Kim", "12345", 10000);
			System.out.println(acc1);
			System.out.println(Account.cnt);  //클래스.이름 클래스변수의 접근법(direct로 접근가능하다)
			acc2 = new Account("Lee", "12346", 10000);
			System.out.println(acc2);
			System.out.println(Account.cnt); 
			
		
		} catch (Exception e) {
			System.out.println(e.getMessage());
			
		}
	}

}

```

![Account](C:\Users\student\Desktop\Account.png)



