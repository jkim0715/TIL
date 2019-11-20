### I. 환경 설정

1. Korean Language Pack 설치
2. Python  (extension) 설치
3. pip install pylint
4. pip install pylint django
5. 내컴퓨터 - 속성 -설정변경 -고급- 환경변수 -PATH(user)- 편집 - 변수 값 복사(python 포함된거 두개 )
   - ctrl+p - '>settings' - 기본설정:사용자설정열기 - python path -  ';변수 값 붙여넣기'





### II.  Articles ( CRUD 연습 )

- URL 나누기

- Base.html

  - css  (/head) 바로 위

  - JS (/body) 바로 위

- Views.py 

  - View를 가지는 친구들과 아닌 친구들 구분해서 코딩하기

- Models.py

  - (models.Model)

### III. URL NameSpace

- 각각의 URL에 별명을 지어줘서 html파일에서 사용하는 링크를 추가적으로 바꾸지 않고, 'urls.py'에서만 수정하면 HTML 파일에서도 링크 수정이 반영되게끔 함.

- ***app_name 설정하고 띄어쓰기 조심해야 됨*** 

- urls.py

  - ```python
     app_name='articles'
    path('new/', views.new, name = "new"),
    ```

- html

  - ```HTML
    {% url 'articles:show' article.id %}
    ```

  - ```html
    {% url 'articles:new' %}
    ```

- views.py

  - ```python
    redirect('articles:show', article.id)
    ```

  - ```python
    redirect('delete')
    ```



### IV.RESTful API

- 예시 articles
- Request Method에 따라서 같은 Endpoint더라도 다른 Function을 동작시킴.

| 역할   | Request-Method | End-Point              | Views(Functions) |
| ------ | -------------- | ---------------------- | ---------------- |
| Create | GET            | /articles/new/         | new              |
| Create | POST           | /articles/             | new(create)      |
| Read   | GET            | /articles/<id>/        | show             |
| Read   | GET            | /articles/             | index            |
| Update | GET            | /articles/<id>/edit/   | edit             |
| Update | POST           | /articles/<id>/        | edit(update)     |
| Delete | POST           | /articles/<id>/delete/ | delete           |

- Request Method에 따라서 같은 Method를 가지고 있음 Function을 합칠 것 임.

- HTML POST 방식으로 보낼 때

  - ```HTML
    <form action="{% url 'boards:new' %}" method="POST">
    ```

    method를 POST로 지정해 줘야 함.

- DB에 접근하는 애들은 POST로 통일... 

  - HTML에서 <a> Tag 는 요청을 GET 방식으로 밖에 못보냄... URL를 바꾸는 거기 때문에.. POST는 불가능..
  - POST로 보낼 수 있는건 사실 '<form>' 밖에 없음...



### IV. Note

- div.container

  - ```jsp
    <div class="container"></div>
    ```

    

- RESTful API 
  - GET : 조회
  - POST : DB에 반영

- Makemigration 

  - ```powershell
    You are trying to add the field 'created_date' with 'auto_now_add=True' to article without a default; the database needs something to populate existing rows.
    
     1) Provide a one-off default now (will be set on all existing rows)
     2) Quit, and let me add a default in models.py
    ```

    - ```python
      created_date = models.DateTimeField(auto_now_add=True, null =True)
      ```

    - 2번 선택 후 

    - null = True를 추가해주면 해결.

- DB Browser 

- auto_now_add=True
  
  - DB를 바꿔서 날짜를 추가해도 이전에 만들어놨던 객체들에 날짜가 임의로 들어감.
- python strftime (str format time)
  
- [링크](https://datascienceschool.net/view-notebook/465066ac92ef4da3b0aba32f76d9750a/)
  
- Instance Method 

  - models.py

    ```python
    class Article(models.Model):
        title = models.CharField(max_length=16)
        contents= models.TextField()
        creator = models.CharField(max_length=8)
        created_date = models.DateTimeField(auto_now_add=True, null =True)
        updated_date = models.DateTimeField(auto_now=True, null = True)
    
        def datetime_to_string(self):
            return self.created_date.strftime("%Y-%m-%d")
    
    
        def created_by(self):
            return "Created By:" + self.creator
    ```

    ***객체 안에 함수 선언***

- Django-Admin

  - localhost:8000/admin

  1. User 만들기

     - ```powershell
       PS C:\Users\82104\Desktop\multicampus\Python\Day9\crudtest> python manage.py createsuperuser
       사용자 이름 (leave blank to use '82104'): master
       이메일 주소: master@naver.com
       Password:
       Password (again):
       비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
       비밀번호가 너무 일상적인 단어입니다.
       비밀번호가 전부 숫자로 되어 있습니다.
       Bypass password validation and create user anyway? [y/N]: y
       Superuser created successfully.
       ```

  2. Admin 만들기

     1. admin.py

        추가

        ```python
        admin.site.register(Article)
        ```

     2. 끗...