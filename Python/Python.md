MVC vs MVVM ?

Front-end Framework - Django

Flask (get - return)





개발자도구 (F12)

- Network를 보면 해당 페이지 동작의 70%정도는 알  수있다.

wappalyzer

- 웹 서비스가 어떤걸로 이루어 져 있는지 분석하는 프로그램.



I. 브라우저의 랜더링 과정 ?

1. https://d2.naver.com/helloworld/59361
2. 





SEO (Search Engine Optimizer)

- og tag : 검색엔진에 최적화 시켜서 노출 될 정보 등록.

``` 
  <meta property="og:title" content="네이버 웹툰" >
  <meta property="og:image" content="https://ssl.pstatic.net/static/comic/images/og_tag_v2.png" >
  <meta property="og:description" content="매일매일 새로운 재미, 네이버 웹툰.">
```



graphql

- 데이터를 담고 있는 파일.. JSON 이나 XML



틀과 데이터를 제공하는 코드가 나뉘는 추세임

- 이런 추세인 이유

  1. Click 했을때 이벤트가 발생한다는 개념.
     1. 일단 화면 바꾸고 
     2. 데이터는 나중에 채워 ~
     3. 아이폰이 이런 형식을 제일 잘 반영.

  2.  예전에는 페이지 전체가 로딩중이였지만 (답답)... 지금은 틀은 먼저 볼 수 있기때문에 대략적으로 어떻게 돌아가는지 알 수 있음.



파이썬 설치

I. Python 3.7.4 다운로드 (https://www.python.org/downloads/release/python-374/)

II.  [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe) 설치 

III. Add Python 3.7 To Path



실행 

1. Window Key + R
2. 실행 창에 powershell 
3. python req.py 로 파이썬파일 실행 



응답코드

1. 200번대 : 정상
2. 300 : 리디렉션 (다른 페이지로 redirect시켜줌)
3. 400 : 클라이언트 오류 
   1. 404 : 해당 URL을 찾을 수 없음.
   2. 403 : Forbidden 숨겨짐.

4. 500 : 서버 오류 (개발자 잘못),
   - 코드오류, 데이터 파싱오류 (타입이라던지..) 등등 개발과정에서 오류.