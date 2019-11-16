### I. Naver API

- [네이버 Developer](https://developers.naver.com/)



### II. 검색어 트랜드

- Dictionary to JSON
  - json.dump(x)





- Get 방식으로 보낼 때 
  - get(url, headers, params)
- Post 방식으로 보낼 때
  - post(url, headers, data)





### III. Class

- 선언 
  - class Human :
- Method 
  - def walk(self)
  - def say_hello(self)
- 



### IV ORM  (Object Relationship Mapping)

- models.py
  - DB에 테이블을 만들 Class 생성
  - 속성 : 컬럼 명
  - 속성의 Field 타입이랑  조건 설정
    - ex) models.CharField(max_length=30)

- 뼈대를 만드는 것 
  - python manage.py makemigrations
- 뼈대 만든 것을 SQLite3에 반영하여 테이블 생성
  - python manage.py migrate

- 테이블 수정 (Column 추가)
  - 추가 할 때는 세세한 조건까지 추가 시켜줘야 함
    -  created_by = models.CharField(max_length=10, **null=True**)

- migration vs migrate
  - migration file :
    - python 파일로 DB구조를 만들 준비, 반영은 아직 x
  - migrate : 명령어
    - 실제 DB에 반영



### V. Django Shell

- 여기서 데이터를 마음대로 넣고 뺴고 할 수 있음

- *python manage.py shell* : shell scripter로 이동.
- Class Import  
  - from boards.models import Board
- 객체 생성 
  - b1 = Board()
  - b1.title = '제목'
  - b1.contents ='컨텐츠'
  - b1.created_by = '작성자'
- 객체 만든걸 테이블에 반영하기 
  - *b1.save()*
- 만들어 놓은 모든 객체 조회
  - Board.objects.all()
    - <QuerySet [<Board: Board object (1)>, <Board: Board object (2)>]> 이런식으로 배열로 나옴
  - Board.objects.all()[0] 이런식으로 하나씩 뽑을 수 있음
- filter
  - 특정 속성을 가진 Object 조회 :  Queryset으로 나옴 (배열 형태..)
  - Board.objects.filter(title = '제목')[0]  혹은 Board.objects.filter(title = '제목').first()
  - c1 = Board.objects.filter(title = '제목').first() 이런식으로 변수에 저장해서 선택한 객체를 이용할 수 있음
    - c1.title
    - c1.contents
- exit()

### Note

- orm (object relationship mapping)
  - 개발 코드를 SQL문으로 컨버트 해주는 느낌.
  - class를 만들면 Table을 만들어줌. 

- [SQLite 브라우져 뷰어](https://sqlitebrowser.org/)
- from django.db import models
  
- django.db의 models를 import해오는 것임.
  
- from A import B  VS import

  - It depends on how you want to access the import when you refer to it.

    ```py
    from urllib import request
    # access request directly.
    mine = request()
    
    import urllib.request
    # used as urllib.request
    mine = urllib.request()
    ```

    You can also alias things yourself when you import for simplicity or to avoid masking built ins:

    ```py
    from os import open as open_
    # lets you use os.open without destroying the 
    # built in open() which returns file handles.
    ```

- Django Shell
  
  - first() 가있고..  last()도 있음.. 



### Summary

- NAVER API 사용해보기

  - 외부 사이트에 Resquest를 보낼 때, Post 방식으로 요청하는 방법을 배움
  - Request Body에 단순히 파라미터명과 파라미터값으로 이루어진 쌍이 아니라 json 형식으로 파라미터를 보내는 방법

- ORM 기초

  - Create, Read를 Django Shell에서 실행시켜보기
  - ORM이 무엇인지? 왜 사용해야 하는지?
    - 객체랑 한 row랑 매칭, 테이블의 한 row를 파이썬에서 한개의 객체로 활용 가능.

  