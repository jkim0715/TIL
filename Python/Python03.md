## Contents

- Parameter
- Beautiful soup

## Parameter

- query string
- path parameter

*웹툰 데이터를 요일별로 다르게 url 세우기* 

*html 파일로 view 만들기(render template)*

## Beautiful soup

- 사이트 구조 분석하는 방법 (HTML은 어떻게 하는지)

- URL 구조(query string) 분석하는 방법

- 사람인 크롤링 (crawling) 해보기 

- 데이터가 xml 형태로 주고받는 사이트 제외 모두 크롤링 가능(로그인 안한 상태에서 볼 수 있는 것만)

- 설치 : pip install bs4

- Method

  - find
    - find
    - find_one

  - select
    - select : 하나만 선택되더라도 리턴은 list (배열)
    - select_one : 

- BeautifulSoup이 먼저 html 을 한번 읽는 과정을 거쳐야 함.

- 실습

  1. 개발자 탭 element에가서 select and element  in the page inspect of it 
  2.  마우스 우클릭 + copy + copy selector

  

## Parameter

url ? 파라미터명 = 값 & 

- 파라미터의 성질에 따라 요청 방법이 달라짐 (GET / POST) 방식.

- 앞쪽에서 넘긴 파라미터 받는 방법

  *request.args.get('파라미터명')*

request.args는 클라이언트로 부터 받은 파라미터를 저장하고 있는 친구

request.args.get('파라미터명')

request.args -> dict 타입(Immutable)). request.args[파라미터명]

### path parameter

/mon  /tue /thu  etc...

\# path parameter

\# python flask how to get multiple parameter from url 

@app.route('/<day>')

def toons(day):

​    return {'today is': day }



python으로 html 뿌리기

``` python
@app.route('/daum_webtoon')
def daum_toon_index():
    html = '''
        <a href="/daum_webtoon/mon">월요일</a><br>
        <a href="/daum_webtoon/tue">화요일</a><br>
        <a href="/daum_webtoon/wed">수요일</a><br>
        <a href="/daum_webtoon/thu">목요일</a><br>
        <a href="/daum_webtoon/fri">금요일</a><br>
        <a href="/daum_webtoon/sat">토요일</a><br>
        <a href="/daum_webtoon/fri">일요일</a><br>
    '''
    return html
```

''' ''' 3개 사이는 문자열로 만들기 





## render_template 

Html 파일을 찾아주고 연결시켜주는 친구 

- 규칙 1: app.py가 위치한 폴더내에 'template' 폴더 생성 ( 이름 무조건 template)

- html : 5

- 만든 HTML 파일 불러올땐 render_template('파일명')

- HTML에서 python에서 등록된 변수를 가져오거나 사용하기 

  - {%%}

  - {%for day in days%}

    {% endfor %}   // html에서는 indent로 for문을 구분할 수 없기 때문에 endfor를 명시하여 scope 명시

- HTML에서 파이썬 문법을 썼을 때 HTML 파일 불러오는 법

  render_template('파일명', **locals())

  - ** locals()  : 선언된 모든 지역변수를 html 로 보내버림 

  원하는 변수만 보낼 때 

  render_template('파일명', 변수명 =변수명, 변수명2=변수명2 )

  음 변수넘길때 dictionary에 다 저장해서 넘기는 방법도 활용 할 수 있을듯...