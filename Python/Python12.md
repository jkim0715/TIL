- Static Field 

  - 개발환경 vs 배포환경

- 이미지 업로드

  - 모델 하나에 직접 입력
  - 이미지 리사이징
  - 이미지 썸네일

- Multiple 이미지 업로드

  - 하나의 Article에 여러 이미지 업로드하기 

- JS 기본

  - 하나의 페이지를 동적으로 만든다.

  - jQuery : JS프레임워크 (x), JS라이브러리(o)

    



### I. Static Field

- 개발환경
  - Static file 을 알아서 관리
  - 정확한 경로를 볼 수 있음 

- 배포환경 
  - Static file 이 한 폴더에 몰려있는거 처럼 보여지게 됨.
  - 실제위치랑 다르게 보이므로 정확한 경로를 숨김.

- Static file : 미리 준비한 파일들 ( css, js 라이브러리 포함)



### II. 이미지 파일

#### 이미지 저장

- App폴더>static폴더>App이름폴더>images폴더 생성 후 images 폴더에 이미지 저장할거임.

- Input form 이 필요함.

  - Image는 GET방식으로 못보내고 POST로만 보낼 수 있음.
  - form 속성에 반드시 **enctype="multipart/form-data"** 추가.

- views.py

  -  *request.FIELS["image"]* 로 form에서 업로드 된 이미지를 가져 올 수 있음.

- models.py에서 ImageField를 추가해서 DB에 저장

  - ```python
    image = models.ImageField(blank = True)
    ```

- pip install Pillow

  - ImageField를 사용하기 위해서는 Pillow라는 녀석을 설치 해야함.

- setting.py 에 경로 추가 

  - ```python
    #우리가 실제로 저장할 위치
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
    #사용자에게 보여지는 위치
    ## 보안목적
    MEDIA_URL = '/media/'
    ```

  - BASE_DIR  = 현재 프로젝트 폴더.



#### 저장된 이미지 뿌리기

- {% load static %}

  - 삽입 위치는 {% extends 'base.html' %} 있으면 바로 밑에

- img src="{% static '/article/images/bono.jpg' %}" 이런식으로 TEST

- ```python
  <img src="{{article.image.url}}" class="card-img-top" alt="{{article.image}}">
  ```

- Project 쪽 urls.py

  - ```python
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns =[
    
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

    - url 파일에 추가.





#### 이미지 Resize

- ProcessedImageField

- ResizetoFill
  - 설정한 사이즈에 딱 맞춰서 이미지 크기 수정, 가로가 긴 경우, 좌,우 영역삭제
- ResizetoFit
  - 비율을 유지한 채로 설정한 사이즈에 맞춤. 여백이 생길 수 있음.





#### 이미지 썸네일

- ImageSpecField

  - Thumbnail

- ```python
      image_thumbnail =ImageSpecField(
          source='image',
          processors=[Thumbnail(200,200)],
          format='JPEG',
          options={'quality':90}
  
  
      )
  ```





### 이미지 여러개 올리기

- carousel







### DB 날리는 법

- migration폴더 > init 빼고 삭제
- db.sqlite3 삭제 



### [WinError 87] 매개변수 

원인 : Python 3.7.4버전에서 종종 있다는  에러임 

해결방법 : Python 버전을 3.7.3으로 바꾼다 



### Note

- 요금 : Response에 담기는 용량 만큼 과금.
  - 이미지 리사이징, 썸네일을 이용해 용량 최소화.
- 프레임워크 vs 라이브러리 차이점 찾아보기
  - IOC
  - A library is just a collection of class definitions
  - In framework, all the control flow is already there, and there's a bunch of predefined white spots that you should fill out with your code. 
  - 
- Bootstrap 쓰는 이유  : Grid system (12분할)



- Django에서는 기본적으로 NULL 값을 허용하지 않음

  - 허용하기 위해서는 null = True를 붙여줘야 함.

  - 따라서 중간에 컬럼을 추가했을 경우, 전에 생성된 rows들은 colomn이 비어있기 때문에 에러가 남.

  