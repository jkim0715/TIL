# Spring AOP

### Aspect Oriented Programming 

- 관심분리 (Separation of Concerns)가 핵심!.



**횡단관심**(Crosscutting Concerns)

- Method 마다 **공통**으로 등장하는 로깅/예외/트랜잭션처리 

**핵심관심**(Core Concerns)

- 사용자의 요청에따라 실제로 수행되는 핵심 비즈니스 로직.



AOP는 횡단관심과 핵심관심을 완벽하게 분리하기 위한 것.



AOP 용어

1. Joinpoint

   - 클라이언트가 호출하는 모든 비즈니스 메소드 
   - 포인트컷 대상 또는 포인트컷 후보 (조인포인트 중에서 포인트컷 선택)

2. Pointcut

   - 필터링 된 조인포인트. 

   - 세밀하게 지정 가능

3. Advice

   - 무엇을 적용할 것 인지 결정

4. Aspect/Advisor

   - 포인트 컷과 어드바이스의 결합으로서 어떤 포인트컷 메소드에 대해서 어떤 메소드를 실행할지 결정



### AOP elment

#### aop:config 엘리먼트

xml

```xml
<aop:config></aop:config>
```

- 루트 엘리먼트 

#### aop:pointcut

xml

```xml
<aop:pointcut expression="execution(* com..Biz+.select(..))" id="id01"/>
```

- 포인트컷을 지정하기 위하여 사용
- 유일한 아이디를 할당하여 애스팩트를 설정할 때 포인트컷을 참조하는 용도로 사용.

#### aop:aspect

xml

```xml
<aop:aspect ref="log"></aop:aspect>
```



#### aop:advisor

1. Before
2. After
   1. After Returning
   2. After Throwing
3. Around

xml

```xml
<aop:after-returning pointcut-ref= "id01" method="printLog"/>
<aop:after-throwing pointcut-ref= "id01" method="exLog"/> 
<aop:around pointcut-ref= "id01" method="aroundLog"/> 
```



### AOP based on Annotation

#### aop:aspectj-autoproxy

```xml
<aop:aspectj-autoproxy></aop:aspectj-autoproxy>
```

Advice  클래스에 AOP관련 Annotation들을 설정.

```java
package com.frame;

import java.util.Date;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.AfterReturning;
import org.aspectj.lang.annotation.AfterThrowing;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Service;
import org.springframework.util.StopWatch;

@Service
@Aspect
public class LogAdvice {
	public void printLog() {
		Date d= new Date();
		System.out.println( d+"[공통로그]비즈니스 로직 수행");
	}
	@Before("execution(* com..Biz+.register(..))")
	public void beforeLog(JoinPoint jp) {
		// 실행되는 method 이름 불러오기
		String method = jp.getSignature().getName();
		// method 안에 arguments 불러오기
		Object [] args = jp.getArgs();

		System.out.println(method+":"+args[0]);		
		System.out.println("[before]비지니스 로직");
	}
	@AfterReturning(pointcut="execution(* com..Biz+.select(..))",returning="returnObj")
	public void afterLog(JoinPoint jp, Object returnObj) {
		
		System.out.println("[after]비지니스 로직");
		System.out.println("Result :"+returnObj);
	}
	@AfterThrowing(pointcut="execution(* com..Biz+.select(..)", throwing ="ex")
	public void exLog(JoinPoint jp, Exception ex) {
		Date d= new Date();
		System.out.println( d+"[EX로그]Exception");
		System.out.println(ex.getMessage());
	}
	
	@Around("execution(* com..Biz+.select(..))")
	public Object aroundLog(ProceedingJoinPoint pjp) throws Throwable {
		
		StopWatch stopwatch = new StopWatch();
		
		stopwatch.start();
		System.out.println("Before Action");
		Object obj = pjp.proceed(); /* <- where our method working */
		System.out.println("After Action");
		stopwatch.stop();
		
		System.out.println("processing Time:"+stopwatch.getTotalTimeSeconds());
		return obj;
	}
}

```







## LOG

1. web.xml 
   
   - <Listener 부분 추가 >
   
   - 모든 request 가 들어올 때마다 Listener가 인지. ( log를 찍기 위함)
   
   - ```xml
     	<listener>
       	<listener-lass>
             org.springframework.web.util.Log4jConfigListener
         </listener-class>
      	 </listener>
       <context-param>
       	<param-name>log4jConfigLocation</param-name>
       	<param-value>/WEB-INF/config/log4j.properties</param-value>
       </context-param>
     ```
   
   - WEB-INF - config 밑에 log4j.properties 복사해서 붙여넣기 (제공된 smvc3 폴더 이용)
   
     - ```properties
       log4j.logger.user = DEBUG, console, user
       log4j.logger.work = DEBUG, console, work
       log4j.logger.data = DEBUG, console, data
       ```
   
       - user, work, data는 임의로 저장.
       - 디버그를 할거고 콘솔에 찍어볼거임 
       - 마지막으로 로그을 파일로 저장할 거임 (user , work , data)
   
     - ```properties
       # user
       log4j.appender.user.Threadhold=DEBUG
       log4j.appender.user = org.apache.log4j.DailyRollingFileAppender 
       log4j.appender.user.DatePattern = '.'yyyy-MM-dd
       log4j.appender.user.layout = org.apache.log4j.PatternLayout 
       log4j.appender.user.layout.ConversionPattern = %-5p %L [%d] - %m%n
       log4j.appender.user.File = c:/logs/user.log   
       ```
   
       - 년월일 찍어볼거고 패턴준거고 저 경로에 파일 저장할거임
       - Linux에서는 경로가 달라져야 함.
   
   - Loggers.java
   
     - ```java
       public class Loggers {
       	private Logger work_log = 
       			Logger.getLogger("work"); 
       	private Logger user_log = 
       			Logger.getLogger("user"); 
       	private Logger data_log = 
       			Logger.getLogger("data"); 
       ```
   
       - 어떤 로그를 쓸건지 결정





EXCEPTION 처리 

Spring MVC 에서 에러가 나면 에러처리 화면으로 보낼 거임.

1. web.xml

   - ```xml
       <listener>
       	<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
       </listener>
       
       <context-param>
       	<param-name>contextConfigLocation</param-name>
       	<param-value>/WEB-INF/config/springex.xml</param-value>
       </context-param>
     ```

     -  요청이 들어올 때 springex.xml 이라는 환경설정 파일을 메모리에 올릴 거다

2. WEB-INF>config 에 springx.xml 추가 

   - ```xml
     <bean id="exeptionResolver" 
      	class="org.springframework.web.servlet.handler.SimpleMappingExceptionResolver">
      		<property name="exceptionMappings">
      			<props>
      				<prop key="java.lang.ArithmeticException">
      					error
      				</prop>
      			</props>
      		</property>
      	</bean>
     ```

     - 일부로 ArithmeticException을 만들어 놨음 ( int a = a/0; )

3. 





문제가 있을때 maven folder 삭제하고 다시 설치 

- C:\Users\student\.m2 에 repository 폴더 삭제 후 project 를 다시 Maven update
- porm.xml 에서 logging 쪽에 runtime 제거 하기 ( Import가 잘 안돼는 경우)



LOG Summary

--Log4j (Log for java)

1.  web.xml

2.  log4j.properties

3.  Logger.java

   -AOP



--Exception

1. web.xml
2. spring.xml
3. error.jsp