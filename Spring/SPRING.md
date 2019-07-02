# SPRING

based on java...

## FRAMEWORK

잘 만들어진 프레임워크를 사용하면 앱에대한 **분석,설계,구현 모두에서 재사용성 증가.**

- 빠른구현시간
- 쉬운 관리
- 개발자들의 역량 획일화
- 검증된 아키텍쳐의 재사용과 일관성 유지



### 자바기반의 프레임워크

Presentation

- webclient

Business

- Spring

Persistence

- Mybatis



## SPRING FRAMEWORK 

장점! 쓰는 이유!

IOC랑 AOP라고 말하면 된다 !.





POJO

- 기존 자바 클래스

1. LightWeight 가볍다

2. IOC (inversion of Control)
   - new로 역여있는 클래스 를 풀어준다?
3. AOP()
   - 공통으로 사용하는 기능들을 외부의 독립된 클래스로 분리.



객체는 Spring에서 관리

STV에관한 설정은 XML에서 관리.



##### Spring Project 개발 환경설정.

1. Make Project
2. Spring Nature
3. Maven(Add Spring Library)
   - pom.xml (List up Library)
   - Download Library (eclipse 가 미국 어딘가의 서버로 가서 jars 다운받아서 저장시켜줌)
     - .m2 folder
   - maven update



Spring IoC

I. xml

- <beans> 루트 엘리먼트
- <import> 엘리먼트
- <bean> 엘리먼



의존성 주입 

*lose coupling 상태에서 size같은 값은 주입하기는 어려움.

