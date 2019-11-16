### I. 기본 게시판 만들기 

1. ##### App마다 URL 분리

   - boards 폴더 ( APP) 안에 urls.py 만들기

     - ```python
       from . import views as boards_views
       ```

     - 여기는 Alias 사용 할 필요는 없음.

     - path 선언할 때 앞에 /board 부분 생략 가능.

   - crudtest 폴더 (Project) 안에 urls.py에는 

     - ```python
       from django.urls import path, include
       urlpatterns = [
           path('admin/', admin.site.urls),
           path('boards/', include('boards.urls'))
       ]
       ```

     - import 에include 추가해주고, path는 boards/ 로 통일



2. ##### 공용으로 사용할 수 있는 (공유할 수 있는 ) HTML 파일 만들기.

   - 반복되는 HTML 구조를 계속해서 새로 만들지 말고, 공통되는 부분은 하나의 파일로 묶어서 반복해서 사용함

   - [예제](https://github.com/jkim0715/Python/blob/master/Day8/crudtest/boards/templates/base.html): base.html
   
     - ```python
           <div class="container">
               {% block content %}
               {% endblock %}
       
           </div>
       ```
   
       
   
   - 다른 HTML파일에는 밑에 나온 형식ㅇ로
   
     - ```python
       {% extends 'base.html' %}
       {% block content %}
       	<내용>
       {%endblock %}
       ```
   
       
   
   



### boards (게시판)

- urls.py 

  - 게시판의 메인페이지, 전체리스트 페이지
  - 게시판의 새 글을 작성하는 페이지
  - 게시판의 글 상세보기

- models.py

  - 객체 생성

  - `class Boards(models.Model)`

    - 게시글 제목, 내용, 작성자 가 필요함 ( Attributes)
    - objects = models.Manager() 를 붙혀주면 "Boards has no 'object' " 에러 사라짐.
    - 혹은 그냥 Extension 설치 하면 됨.
    - ID는 자동으로 생성, auto increment
    - Charfield는 반드시 max_length가 필요함

    

  - Django Shell (ORM 사용 목적)

    - *python manage.py makemigrations* : DB환경을 만들 수 있는 파일을 만드는 것 
    - *python manage.py migrate* : Commit 

  - ```python
    def __str__():
    ```

    - 이게 Java의 toString() 같은 느낌임.

- views.py

  - 파라미터로 넘어오는 값은 모두 str, 하지만 table에 id는 int형이기 때문에 형변환 필요.

    - ```python
        board = Boards.objects.get(id=int(id))
      ```

  -  혹은 urls.py에서 id값을 받을 때 형을 지정 해줄 수 있음

    - ```python
        path('<int:id>/',boards_views.show)
      ```

      

  

- 반복되는 html 파일 묶기
  - templates/base.html
  - 센터 바꾸는 개념임.

#### 화면

- 메인 

  ![](https://user-images.githubusercontent.com/50862254/68990569-1cd51800-0898-11ea-9a8f-f4d27c95153c.PNG)

- 새글 (Create)

  ![board_new](https://user-images.githubusercontent.com/50862254/68990594-6c1b4880-0898-11ea-9b66-94dae6499181.PNG)

- 수정(Update) / 삭제 (Delete)

  ![board_detail](https://user-images.githubusercontent.com/50862254/68990624-b00e4d80-0898-11ea-8a24-0413d20c6d06.PNG)

  

### Bootstrap

- [사이트 접속](https://getbootstrap.com/)

- getstarted

- css 복사 <head> 끝나기 전에 복붙.

- JS는 Body에 복붙

[예제](https://github.com/jkim0715/Python/blob/master/Day8/crudtest/boards/templates/base.html) : base.html



### Note 

- URL 나누는 이유
  - C  : New , Create
  - R : Index. Show
  - U : Edit, Update
  - D : Destroy
    - urls.py 에다가 우리가 접속할 모든 주소를 명시했는데, CRUD를 하다보면 만들어야 할 페이지가 점점 많아져 구부낳기가 어려워지기 떄문에 각 역할을 하는 App마다 urls.py파일을 생성할 예정.



- Beautify 
  - auto indent 
    - ctrl + p
      - " > beatify file"



- notion

  주소 : [바로가기](https://www.notion.so/) 

- Trello

- 슬랙
- 장고의 철학
  - 튼튼한 결집
  - 느슨한 결합.

