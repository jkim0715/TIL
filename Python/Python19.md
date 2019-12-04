### Templates Dir

- os.path.join(BASE_DIR, 'templates')
  - OS마다 역슬레쉬 정슬레쉬 구분해주는 친구라





### DB 확실하게 날리는 법

```shell
rm db.sqlite3
rm board/migrations/0*
```





### 사용자 데이터 검증이 안되있음.

- Models.py 에서 검증할 수 잇는걸 import 할 수 있지만 model에는 데이터의 대한 스키마 정보만 담고 있는게 이상적.







### pip install django-bootstrap4







### 유효성 검사

- HTML (1단계)

  - required, min_length 등

  - 브라우저가 막아줌
  - 근데 이번 수능 점수마냥 쉽게 뚫림

- Django Form (2단계)

  - is_valid()
    - 거의 여기서 걸러짐
  - blank = True 로 패스가능
  - CharField / TextField 는 blank =True 로 DB까지 패스가능
    - 빈값으로 놔두면 DB에 null이 들어가는게 아니고  빈 문자열이 들어가게 됨

- DB (3단계)

  - null = True 로 패스 가능.
  - Django 기본 값으로 null = false 로 되어있음.

