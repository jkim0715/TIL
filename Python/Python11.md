### I. Fake Instagram

- 기능

  - 댓글 (comment) : model, url 

    - Database Relation(1:N)

  - 이미지 업로드

  - 좋아요 , 해시태그

    - Database Relation(M:N)

    

### II. Article (Post)

- reverse() 정렬

  - ```python
     articles = Article.objects.all().order_by("created_date").reverse()
    ```

  - ```python
     articles = Article.objects.all().order_by("-created_date")
    ```




### III. Comment 달기

#### 1 : N 관계

- models.py

  - Class 관계 설정

    - *article = models.ForeignKey(참조할 테이블, on_delete=models.CASCADE)*   추가 

    ```python
    class Comment(models.Model):
        contents = models.TextField()
        created_date = models.DateTimeField(auto_now_add= True)
        updated_date = models.DateTimeField(auto_now= True)
        article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ```

    **article 이라고 선언하면 DB에는 '_id'가 붙어서 저장됨** : *article_id*

  

- _set

  - Foreign Key 역참조 

    - 원래 참조 당하는 애는 누가 자기를 참조하고 있는지 모름.

    - 해당 Article을 참조하는 모든 Comment 들을 불러옴. 

    - ```html
      {% for comment in article.comment_set.all %}
      ```

    - 특정 Article에 대하여 달린 댓글들 (article_id 가 같은 모든 Comment(객체) 들을 불러옴)

    

### NOTE

- Relation
  - Primary Key와 Foreign Key 의 비율. 
    - 1:1
    - 1:N
    - N:M

- Render 와 Redirect
- Render
  - render를 요청하면 동일한 수준에 있는 Directory내에서 templates 폴더를 찾고 그안에 html파일를 읽음
  - html 파일을 읽으면서 Python 문법를 찾음 
    - {%%} 로직을 찾는 문법
      - 로직을 탄다고 생각하면 됨.
    - {{}} 실제 출력. ( 실제 사용자가 볼 수 있는 화면)
- Redirect 
  
- url를 한번 더 타는 것.
  
- CallBack

  - 동작이 완료됐다고 알려주는 것

- migrations

  -  ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),

  

