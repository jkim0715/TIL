## I. Django 

- MVC → MVT

  - Model, View, Controller
  - Model, View, Templates

- django에서 app의 단위는 하나의 모델에 대한 모든 내용이 담겨 있다.

  - 예를 들어 게시판을 만든다고 하면 post라는 app을 만들어 그안에서 모든 내용을 처리한다

  



## II. [WORKSHOP (Django Project)](https://github.com/jkim0715/Python/tree/master/Day5/day5)



### 1. 로또 번호 생성기

1. 메인 페이지 ( 번호를 몇개 뽑을지, 생성 버튼)
2. 결과 페이지
   - 랜덤으로 뽑힌 번호 
   - 뽑힌 번호와 가장 최근 뽑힌 번호랑 비교 몇개 맞았는지

### 시작

- python manage.py startapp lotto

- views.py, urls.py, settings.py 

1. [settings.py](https://github.com/jkim0715/Python/blob/master/Day5/day5/day5/settings.py)

   1. INSTALLED_APPS : 프로젝트에서 사용할 앱 등록
      -  'lotto' 추가

2. [urls.py](https://github.com/jkim0715/Python/blob/master/Day5/day5/day5/urls.py)

   - 사용자로 부터 request가 들어오면 urls.py 파일이 어느 views의 Method로 갈 것인지 설정을 해 준다.

   1. lotto로 부터 view를 Import 해야함.

      - ```python
        from lotto import views as lotto_views
        
        ```

      *사용 APP이 한개라면 As를 이용해서 구분 할 필요 없음.*

   2. path('request형태', '실행시킬 뷰')

      - ```python
          	path('admin/', admin.site.urls),
            path('lotto/', lotto_views.lotto),
            path('lotto/winning', lotto_views.winning)
        ```

3. [views.py](https://github.com/jkim0715/Python/blob/master/Day5/day5/lotto/views.py)

   함수 등록 

   ```python
   def winning(request):
   
       return render(request, 'winning.html')
   ```

   - Flask랑 다르게 매개변수로 "request" 필수.

   - 프론트로 변수 넘길 땐 기본적으로 Dictionary 형태로 넘김.

     {'result': result}

   - request랑 requests 구별

4. lotto 폴더 밑에 [templates](https://github.com/jkim0715/Python/tree/master/Day5/day5/lotto/templates) 폴더를 만들어서 html 파일 저장.

   - html:5   (자동완성 )

   - {{변수}}

   - {% for a in b%}

     {% endfor %}

   

### 화면

![lotto](https://user-images.githubusercontent.com/50862254/68641810-5bdd3380-054f-11ea-8a30-673472cd7d9c.PNG)



### 2. ASCII

- http://artii.herokuapp.com/make?text=hello&font=bubble__
- http://artii.herokuapp.com/fonts_list

[settings.py](https://github.com/jkim0715/Python/blob/master/Day5/day5/day5/settings.py)

[urls.py](https://github.com/jkim0715/Python/blob/master/Day5/day5/day5/urls.py)

[views.py](https://github.com/jkim0715/Python/blob/master/Day5/day5/ascii/views.py)

1. 원하는 텍스트와 폰트를 입력
   - 폰트는 fonts_list에서 받아온 폰트들을 select / option 으로 뿌렸음
2. Input 받은 데이터를 format string으로 url보내서 response결과 값을 리턴.
3. result.html 에 결과 뿌리기.



### 화면

![artii](https://user-images.githubusercontent.com/50862254/68645054-3ace1000-055a-11ea-94ad-79d99567e2ef.PNG)

### 3. OPgg

1. [settings.py](https://github.com/jkim0715/Python/blob/master/Day5/day5/day5/settings.py)
2. [urls.py](https://github.com/jkim0715/Python/blob/master/Day5/day5/day5/urls.py)
3. [views.py](https://github.com/jkim0715/Python/blob/master/Day5/day5/opgg/views.py)
   1. 아이디 입력 받기
   2. 해당 소환사의 전적을 BeaurifulSoup으로 select 해서 가져오기
   3. 전적을 결과 페이지에 뿌려서 보여주기.
4. [Templates](https://github.com/jkim0715/Python/tree/master/Day5/day5/opgg/templates)
   - opgg.html
   - ratio.html
     - 이름이 겹치면 다른 App의 html을 불러올 수 있으므로 조심.

### 화면

![fakeopgg](https://user-images.githubusercontent.com/50862254/68653766-c736fd80-056f-11ea-8814-ce5294f928a8.PNG)









## NOTE

- Flask 와 Django의 차이점 ?

  - | Flask | Django  |
    | ----- | ------- |
    | 경량  | 중 규모 |
    | MVC   | MVT     |

    

- range() 함수

  - The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

  - range*(start, stop, step*)

    | *start* | Optional. An integer number specifying at which position to start. Default is 0 |
    | ------- | ------------------------------------------------------------ |
    | *stop*  | Required. An integer number specifying at which position to end. |
    | *step*  | Optional. An integer number specifying the incrementation. Default is 1 |

- if a in b:
  
- 만약 a가 b안에 있을 경우 조건문.
  
- request로 받아온 text 배열로 저장하기

  - ```python
    url = 'http://artii.herokuapp.com/fonts_list'
    response = requests.get(url)
    fonts_list = response.text.split('\n')
    ```

  
  
  
- 문제

  1. Templates Issue

     - 랜더 한 html 파일 이름이 같아서 그런지 다른 App에 만들어 놓은 html을 불러옴.

     - opgg 에서 만든 result.html을 매핑했는데, ascii에서 만든 result.html을 불러오고 있었음 슬프게도..

  해결방법 : result.html이름을 바꿔버리기..  혹은 templates 안에 폴더를 새로 만들어서 경로를 다르게 해서 구분해주기

  2. 랭크가 없거나, 해당 유저 정보가 없을때

     - 조건문 으로 해결.

     ```python
     if html.select_one('span.WinLose .wins') is None :
     ```

     