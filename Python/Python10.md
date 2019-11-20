

### I. RESTful API

- Resquest Method에 따라 같은 url 요청이라도 다른 함수실행.
  - Browser에서 공식 지원되는 2가지
    - GET
    - POST : DB에 접근
      - CSRF 토큰을 확인하게되고, 만약 토큰이 다르다면 
- 사용 이유 :  

### II. CSRF 

- 다른 사이트에서 우리 사이트로 보내는 요청을 걸러주는 기초적인 보안 장치

- POST 요청을 안정적으로 보낼 수 있게 만들어주는 녀석들임.

  - ```html
    <input type = "text" name = csrfmiddlewaretoken value = "{{csrf_token}}">
    ```



### NOTE

- NoReverseMatch
  - HTML : 에 뭔가 딴게 들어갔을때 
- App-templates - html 파일들은 Python embedded 된 html 파일임
  - views.py 에서 html들을 불러오기 떄문에 먼저 python문법으로 읽고 html를 리턴해주는 방식임.

