### User

- 로그인 상태 확인

  - ```python
    request.user.is_authenticated:
    ```

- 현재 로그인 유저 정보가져오기

  - ```python
    request.user.id
    ```

- User Authentication Error : 401 

  - ```python
    context ={
    'status':401,
    'message' : '로그인이 필요합니다.'
     }
    return HttpResponse(json.dumps(context), status =401, content_type = "application/json")
    ```

### 권한

- HTML에서 안보인다고 삭제 권한이 없는건 아니므로 Back에서도 막아줘야함.
- POST방식으로 처리되는 것들은 얼핏보면 안전한거 같지만  요즘 세상이 좋아져서 POST방식으로 날릴 수도 있으므로 방어.

### 좋아요

- ManyToMany()

  - ```python
    user_likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="article_likes")
    ```

- Related Name이랑 어디서 구현할지 명확하게 정의해 놓아야 함.







### NOTE

- 로그인이 되지 않은 상태에서 글을 작성할 수 없어야 함.
  - 글작성, 댓글작성, 좋아요(M:N)
  - 1:N은 다 끝남.
- Ajax vs Pusher 
  - Ajax 
    - 댓글이 달릴 때 페이지 리프레쉬 없이, 페이지를 다이나믹하게 하려고 사용.
    - 하지만 서로 다른 브라우저에서 동작되는 행위는 반영되지 않음
  - Pusher
    - 외부 API
    - 실시간 기능 

- 커스턴 user
  - settings 건들고
    - form을 건들여서 
  - OneToOne
    - 따로 1대1 대응되는 클래스를 엮어서 사용.
- Tooltip  사용 해보기
- Toaster : 메시지를 깔끔하게 보여주는 기능.



- 카카오지도 : 

  - Documentation이 잘 구성되어 있어서 가져오기 편함.

  - Stackoverflow처럼 자체 Q&A 게시판이 잘 되어있음.

  - 모두 JS로 이루어져 있어서 사용하기 편할 듯.

    