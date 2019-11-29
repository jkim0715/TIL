### I. Ajax, jQuery 활용하여 CRUD 구현 

- 한글 코딩으로 시나리오 짜는 것도 한 방법.

- jQuery에서 CSS Selector, Tree Traversal 등을 이용하여 원하는 위치의 HTML문서에서 값을 자유롭게 다룸.

- Create/ Edit 만들 떄 비슷한 Ajax 코드 반복하기 번거로우니 ajax data 넘길때 Method : edit 등을 지정하여 View.py에서 처리해서 넘겨주는 방식을 사용 해 보기로 함.

  



#### jQuery Selector

- [jQuery CSS Selector](https://www.w3schools.com/jquery/jquery_ref_selectors.asp)

- this : Event가 발생한 위치

  ```python
  $(this).find('input')
  ```

  find : $(this)에서 찾은 위치의 자식들 중 'input' 이라는 element가 가르키는 친구를 찾아줌.

  - jQuery [Tree Traversal](https://api.jquery.com/category/traversing/tree-traversal/)

  

  ```python
  $(this).find('input')[1]
  ```

  1번째 자식.

  

  ```python
  $(this).find('input.commentInput').val()
  ```

  input이라는 태그를 찾고 그 안에 .commentForm 이란 클래스를 가진 애들을 찾고 값을 뽑는다.



#### CSS Function

- [바로가기](https://www.w3schools.com/cssref/css_functions.asp) 





### II. Custom Data Attributes

- ```html
  <button data-id="3">버튼</button>
  ```

  속성값을 뽑을 때  **$(this).data("id")**

  **$(this).data();** 는 Dictionary 형식 혹은 Json 형식으로 저장 되어있음

  data-id / data-value 등 원하는대로 사용 가능






### III. jQuery .serialize();

##### console.log($(this).serialize());

- form안에 들어있는 모든 태그 안의 모든 파라미터들을 만들어줌.

  ```html
  article_id=5&contents=%EC%9D%B4%EC%97%B4 이런식으로 나옴
  ```

- 사용 방법 :

  ```html
  var 변수 = console.log($(this).serialize())
  변수.article_id;
  변수.contents;
  ```







### IV. Auth

- 기본적으로 구현되어있는 모델이 있기 때문에 따로 모델링 불필요.
  - /accounts/login
  - /accounts/logout
  - /accounts/signup
- 유저를 관리할 App을 따로 만들어서 관리.
  - python manage.py startapp accounts

- Django 가 Form을 이용해 유저의 정보랑 매칭 하는 기능 제공. (views.py)

  ```python
  from django.contrib.auth.models import User
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
  from django.contrib.auth import login as auth_login
  from django.contrib.auth import logout as auth_logout
  ```

  

### Cookie  vs Session

- 필요성.

  - HTTP req / res 무상태성 (State less)
  - 무상태성 이란?
    - 요청/응답 한번 하면 연결이 끊기는 것.
    - 내가 요청을 하기 전 까지내가 뭐하고 있는지 서버는 모름

- 정보 저장의 주체.

  - Cookie : 내 브라우져  (크롬, 익스플로러 다 다르게 저장됨)
    - 아무나 다 볼 수 있는 내용.(보안 취약, 개인정보 저장 하면 안됨)
    - 별로 좋은 저장 방식이 아니였음.
  - Session : 서버 컴퓨터 (정보를 서버 컴퓨터의 메모리에 저장해놓고 내 컴퓨터에는 정보의 위치만 저장)
    - 로그인이 됀 상태인건 브라우저 가 알기보단 서버가 알고있는거고 브라우저는 그 정보가 담긴 주소값만 가지고 있음.
  - Session Storage랑 Session이랑 헷갈리지 말기

- 라이프 사이클.

  - Cookie : 브라우져가 종료되도 남아있음
    - 만료기간을 정해줄 수 있음
  - Session : 브라우저가 종료되면 날아감 (하지만 저장해 놓을 수 있는 방법이 있음)
    - remember me 같은거

  









#### NOTE

- 변수에 문자열로 HTML Tag를  갖다 박을 수 있음.

- Ajax Success function안에서 변수 지정 및 function(data)에서 data 활용 방법

  ${data.contents}

   ``` html
  var content = 
  '
  <li class="list-group-item" id='comment-{{comment.id}}'>
  <span class="fas fa-comment-dots commentItem">${data.contents}</span>
  <span class="float-right">
  <button class="btn btn-warning editComment" data-id="{{comment.id}}" data-value="{{article.id}}"><i class="far fa-edit" ></i>수정</button>
  <button class="btn btn-danger deleteComment" data-id="{{comment.id}}" data-value="{{article.id}}"><i class="far fa-trash-alt" ></i>삭제</button>
  </span>
  </li>
  '
   ```
  
  **파이썬 문법이랑 JS문법 쓸때 안쓸때 확실히 구분해야 함**.
  
  - Ajax Callback 부분에서는 JS밖에 못쓰므로, 파이썬 문법을 다 JS로 바꿔줘야 함.
  
    **(Python)** {{data.contents}} = ${data.contents} **(JS)**





