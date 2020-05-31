# Spring IoC

`Inversion of Control` 제어의 역행. 

- IoC는 객체지향 언어에서 객체 간의 연결 관계를 런타임에 결정하게 하는 방법
- 객체 간의 관계가 **느슨하게** 연결됨 
  - 확장성증가 유지보수의 유용성.
- IoC의 구현 방법 중 하나가 **DI**(Dependency Injection)
  - `IoC`는 개념이고, 구현은 `DI`를 통해서 한다.

## XML

스프링프레임 워크는 Bean 컨테이너다 (빈 생성, 소멸, 관리)

XML의 태그명은 데이터에 대한 서술, 설명

```xml
<!-- 스프링프레임 워크는 Bean 컨테이너다 (빈 생성, 소멸, 관리) -->
<!-- XML의 태그명은 데이터에 대한 서술, 설명-->

<!-- 등록할 Bean을 정의 -->
<!-- 주의) 추상 클래스나 인터페이스는 등록불가 -->
<bean class="com.ssafy.step3.MessageBeanKO" id="msg"></bean>
<!-- MessageBeanKo msg = new MessageBeanKo() -->
```





## Annotation



namespaces context 추가 



@ 사용법

```java
@Component("id")
@Service("id")
@Repository("id") 
```

객체 성질에따라 달라짐 

우리는 Biz는 Service,  Dao 는 Repository 라고 정하고 쓴다.



component-scan이  container에서  객체를 쭉 스캔하고 저장해놓는다.

그후 id를 불러와서 해당 객체를 불러와 사용하면 됨.



**xml**

```xml
<context:component-scan base-package="springtv"></context:component-scan>
```

**java** 

```java
@Component("id")  or @Service("id") or @Repository("id")  비즈니스 로직에 따라 다름

@Autowired 해당 타입의 객체가 한개일때만 불러올 수 있다.    
@Qualifier("id") 이걸 아래다가 붙이면 해당 아이디의 객체를 불러옴

다 필요없고 
@Resource(name="id") 이렇게 쓰면 된다.
    
  
```

##### Annotation 단독으로 사용하면 범용성 있는 코드를 짜기 힘드므로 

##### XML + Annotation을 짬뽕 하여 쓴다.

**java**

```java
@Autowired  만 써놓고  xml에 어떤 타입의 객체를 사용할건지 명시 

```

**xml**

```xml
<context:component-scan base-package="springtv"></context:component-scan>

<bean id="ms" class="springtv.HarmanSpeaker"/>
```



어떤 방식을 사용하건 프로젝트에따라 더 좋아보이는걸 쓰면 된다.





