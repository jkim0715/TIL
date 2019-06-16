### UserDao

```java

public void insert(User v, Connection con) throws Exception { //앞에서 준 커넥션으로 한거임
			PreparedStatement pstmt = null;
			pstmt = con.prepareStatement(Sql.insertUser);
			pstmt.setString(1, v.getId());
			pstmt.setString(2, v.getName());
			pstmt.setString(3, v.getPwd());
			pstmt.executeUpdate();
			close(pstmt);
		
	}
이렇게 하면 close 안될수도이음
```

#### solution

```java
public void insert(User v, Connection con) throws Exception { //앞에서 준 커넥션으로 한거임
			PreparedStatement pstmt = null;
			try {
			pstmt = con.prepareStatement(Sql.insertUser);
			pstmt.setString(1, v.getId());
			pstmt.setString(2, v.getName());
			pstmt.setString(3, v.getPwd());
			pstmt.executeUpdate();
			}catch(Exception e) {
				throw e;
			}finally {
			close(pstmt);
			}
	}
```





