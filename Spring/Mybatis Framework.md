# Mybatis Framework.

Spring JDBC 연동은 꾸짐.. 그래서 Mybatis framework를 연동해서 사용



ORM

object를 relate 시키는거..



SQL 문장을 XML에서 관리할거임.



DB랑 연동할려면 젤먼저 트렌잭션 을 떠올려야 함 



xml 안에서 SQL문을 쓸때 주의 할 것 특수문자 안먹음

```xml
LIKE '%L%' 이거 안먹음	
```





 객체의 이름과 컬럼명이 다를때 사용 (resultMap)

```xml

	<resultMap type="user" id="um">
		<result property="identification" column="id"/>
		<result property="password" column="pwd"/>
		<result property="username" column="name"/>
	</resultMap> 
```



XML문서의 SQL문에 부등호를 써야 할 때

```xml
<![CDATA[Select * from T_user where NAME > 10]]>
```







