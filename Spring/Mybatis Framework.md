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



JVM 위에 Spring MVC, Spring Container, Mybatis가 같이 구동한다.



Mybatis는 XML 파일에 저장된 SQL 명령어를 대신 실행하고 실행 결과를 VO같은 자바 객체에 자동으로 매핑까지 해준다!!

Mybatis도 xml로 설정한다.

```
<tx:annotation-driven transaction-manager="txManager"/>
<typeAlias type="com.vo.Cust" alias="cust"/>
```

alias : type의 이름을 alias-value로 재정의 한다.

Mybatis는 pom.xml에 적어주면 spring이 알아서 관리한다.

### XML에서 설정하는 방법

all xml code

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:aop="http://www.springframework.org/schema/aop"
	xmlns:context="http://www.springframework.org/schema/context"
	xmlns:p="http://www.springframework.org/schema/p"
	xmlns:tx="http://www.springframework.org/schema/tx"
	xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.2.xsd
		http://www.springframework.org/schema/aop http://www.springframework.org/schema/aop/spring-aop-4.2.xsd
		http://www.springframework.org/schema/tx http://www.springframework.org/schema/tx/spring-tx-4.2.xsd">
	
	<context:component-scan base-package="com.*"></context:component-scan>
	<tx:annotation-driven transaction-manager="txManager"/>
	
	<!-- 1. Database Setting -->
 	<bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
 		<property name="driverClassName" value="oracle.jdbc.driver.OracleDriver"/>
 		<property name="url" value="jdbc:oracle:thin:@70.12.114.68:1521:xe"/>
 		<property name="username" value="db"/>
 		<property name="password" value="db"/>
 	</bean>
	
	<!-- 2. Transaction Setting -->
 	<bean id="txManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
 		<property name="dataSource" ref="dataSource"/>
 	</bean>
 	
 	<!-- 3. MyBatis Setting -->
 	<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
 		<property name="dataSource" ref="dataSource"/>
 		<property name="configLocation" value="classpath:com/mybatis/mybatis.xml"/>
 	</bean>
	
	<!-- 4. Spring Mybatis Connect -->
 	<bean id="sqlSessionTemplate" class="org.mybatis.spring.SqlSessionTemplate">
 		<constructor-arg ref="sqlSessionFactory"/>
 	</bean>
 	
 	<!-- 5. Mapper Setting -->
 	<bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
 		<property name="basePackage" value="com.mapper"/>
 	</bean>
	
	
</beans>
```

#### 1. database setting

```
<!-- 1. Database Setting -->
 <bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
 	<property name="driverClassName" value="oracle.jdbc.driver.OracleDriver"/>
 	<property name="url" value="jdbc:oracle:thin:@70.12.114.68:1521:xe"/>
 	<property name="username" value="db"/>
 	<property name="password" value="db"/>
 </bean>
```

DB에 접근하기 위한 ID등을 넣어준다. (DB의 정보)

#### 2. Transaction Setting

```
<!-- 2. Transaction Setting -->
 	<bean id="txManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
 		<property name="dataSource" ref="dataSource"/>
 	</bean>
```

사용하고자 하는 클래스의 매서드 위에 @Transactional를 써 줘야 함 인터페이스의 매서드 위에 써 주면 상속받는 모든 매서드에 @Transactional처리가 됨

#### 3. MyBatis setting

```
<!-- 3. MyBatis Setting -->
 	<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
 		<property name="dataSource" ref="dataSource"/>
 		<property name="configLocation" value="classpath:com/mybatis/mybatis.xml"/>
 	</bean>
```

configLocation의 value에는 mybatis의 설정이 있는 xml 이름을 적어준다.

##### 3-1. MyBatis.xml

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
PUBLIC "-//mybatis.org/DTD Config 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
	<typeAliases>
		<typeAlias type="com.vo.User" alias="user"/>
	    <typeAlias type="com.vo.Product" alias="product"/>
	</typeAliases>
	
	<mappers>
		<mapper resource="com/mybatis/usermapper.xml"/>
		<mapper resource="com/mybatis/productmapper.xml"/>
	</mappers>
</configuration>
```

typeAliases : db의 테이블의 구조를 클래스화한 다음, 링크를 걸고(type) 쓰기 쉽게 줄여준다.(alias)

mapper : resource에 사용할 쿼리문이 적힌 xml파일을 넣어준다.

###### **3-1-1. com.vo.User class**

```
package com.vo;

public class User {
	String id;
	String password;
	String name;
	
	public User() {
	}

	public User(String id, String password, String name) {
		super();
		this.id = id;
		this.password = password;
		this.name = name;
	}
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
}
```

※ getter가 다 있어야 하며, default constructor도 있어야 한다.

###### **3-1-2. usermapper.xml**

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper
PUBLIC "-//mybatis.org/DTD Mapper 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.mapper.userMapper">

	
	<select id="select" parameterType="String" 
	resultType="user">
		SELECT * FROM T_USER WHERE ID=#{id}
	</select>
	
	<select id="selectall" 
	resultType="user">
		SELECT * FROM T_USER ORDER BY 1
	</select>
	<insert id="insert" parameterType="user">
		INSERT INTO T_USER VALUES (#{id},#{password},#{name})
	</insert>
	<update id="update" parameterType="user">
		UPDATE TB_CUST SET PWD=#{password},NAME=#{name} WHERE ID=#{id}
	</update>
	<delete id="delete" parameterType="String">
		DELETE FROM TB_USER WHERE ID=#{id}
	</delete>
	
</mapper>
```

id : 매핑 된 클래스 에서 매서드의 이름 parameterType : 인풋 인자의 형식 resultType : 아웃풋 인자의 형식 ※ #{value}안의 값은 resultType형식 안의 데이터를 넣어 주어야 한다.

3-

#### 4. Spring Mybatis Connect

```
<!-- 4. Spring Mybatis Connect -->
 	<bean id="sqlSessionTemplate" class="org.mybatis.spring.SqlSessionTemplate">
 		<constructor-arg ref="sqlSessionFactory"/>
 	</bean>
```

#### 5. Mapper Setting

```
<!-- 5. Mapper Setting -->
 	<bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
 		<property name="basePackage" value="com.mapper"/>
 	</bean>
```

value에 mapper가 들어가 있는 패키지를 적어준다.

## Spring MVC

```
package com.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class MainController {
	
	@RequestMapping("/main.mc")
	public ModelAndView main() {
		ModelAndView mv = new ModelAndView(); 
		mv.addObject("",)
		mv.setViewName("main");
		return mv;
	}
}
```

@RequestMapping 매서드의 이름을 지정함, pulic ~ 로 이어지는 매서드 명은 쓰지 않는다.

ModelAndView mv = new ModelAndView(); 값을 넣고, 보내는 객체

mv.addObject("object","target") 넣을 때 사용함 target 에는 목적지에서 쓸 오브젝트의 이름이고, object에는 목적지에서 target의 이름에 해당하는 값이다.

mv.setViewName("target") : target에는 requetMapping에 쓰인 이름으로 이동한다.



