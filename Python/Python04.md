## I. Flask

- WAS (Web Application Server)
- 경량화 Framework





## II. Django

- 중규모 서비스 처리에 적합.
- *pip install django*

- 역할별로 파트별로 분리



**프로젝트 생성**

- *django-admin startproject 프로젝트이름*

  



**실행 (Working directory를 생성한 프로젝트안으로 이동 후 )**

- *python manage.py runserver*

  



**프로젝트 구성** 

- settings.py
  - INSTALLED_APPS
    - Application이라고 해서 헷갈리는데, Controller 같은 느낌임.
  - DataBases
    - SQLite 등.
  - LANGUAGE_CODE = 'ko'
    - 한글로 변환
  - TIME_ZONE = 'Asia/Seoul'
- urls.py
  - 모든 Routing 개념을 여기서 규정.



**어플리케이션 생성**

- *python manage.py startapp webtoon*
  - "webtoon" 이라는 앱을 만듬.



**앱 구성**

- migrations.

-  admin.py

- apps.py

- models.py

- test.py

- views.py

  



**Trouble Shooting**

- *python manage.py migrate*







## III. REST API

- url을 구성하는 패턴 중 하나.



**REST API 디자인 가이드**

- URI는 정보의 자원을 표현해야 한다.
- 자원에 대한 행위는 HTTP Method(GET, POST, PUT, PATCH,DELETE)로 표현한다.
  - Create -**POST** 
    - */webtoons* 같은거라도 생성
  - Read - **GET** 
    - */webtoons*/webtoon/<nickname> 조회
  - Update - **PUT, PATCH**
    - webtoon/<nickname> 업뎃
  - Destroy - **DELETE**
    - webtoon/<nickname> 삭제
- request method에 따라서 조회하거나, 업데이트 하거나, 삭제하는 것임.





### 참고

- *https://meetup.toast.com/posts/92*





## Workshop

1. Fake 검색창 (query string)
   - 검색창 + 검색결과
2. Fake Login
   - 로그인창 → 로그인 로직 → 메인창
   - Form 에서 method = "post"
     - Method Not Allowed뜸.
     - Flask 에서 *@app.route('/login/submit' , methods=['POST']* 처럼 방식을 지정해줘야 함.
   - 주소창에다가 주소를 치는것은 Methods중 GET방식만 가능 따라서 POST로 요청을 보내는 아이는 자기 자신의 View를 가지면 안됨. 무조건 Redirect를 시키는 것을 추천.
3. 기본 CRUD 로직 ( 아이디어 톤 이후)





## Note

- *https://tutorial.djangogirls.org/ko/*
  - 장고 튜토리얼

- Enterprise 급 기준?
  - 하루 접속자 천만이상 (ex 네이버)
  - 하루 query 요청 억단위

- 기술면접
  - *핵심단어* 어필.
  - 마인드 맵 형식으로 중심의 핵심단어 설명하고 가지치기 형식으로 설명해 나가기.

- API store
  - www.apistore.co.kr
- 개발이랑 운영이랑은 많이 다름.
- SI (System Integration)
  - 인력사무소 
  - 사수를 잘만나면 좋지만 자기가 개발한 서비스를 운영해볼 기회가 없음.
  - 50명이라도 주변에서 사용해줄 사람 찾고 실제로 서비스 운영해보기 
- Flutter
  - **Flutter** is an [open-source](https://en.wikipedia.org/wiki/Open-source_software) [UI](https://en.wikipedia.org/wiki/User_interface) [software development kit](https://en.wikipedia.org/wiki/Software_development_kit) created by [Google](https://en.wikipedia.org/wiki/Google). 
  - App 뒷단은 Flask 나 Django로만들고 Flutter를 이용해서 서비스.
  - https://flutter.dev/
- **MVC 패턴 역할**
  - Model 역할
  - Controller 역할
    - 파라미터값 가져와서 뷰 에 전달.
    - 뷰선택
  - View 역할

- **MVVM** 대세니까 알아두기.
  - 안드로이드도 이쪽임.
- 내가 "www.naver.com" 에 접속했을 때 발생하는 모든 과정을 아는대로 설명하시오
  1. Client에서 url  을 날리겠죠
  2. DNS서버에서 URL을 IP주소로 치환.
  3. request
  4. route (누가 처리할건지 Mapping)
  5. Controller
  6. Model
  7. Controller
  8. View
  9. Response
  10. Browser
  11. HTML문서를 읽고
      1. "<HEAD>"
      2. DOM TREE 그려서
      3. CSS 붙이고 
      4. Render