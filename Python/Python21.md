### 배포

#### heroku.com

- *$git push* 로 배포
- *$git commit* 기준으로 배포됨 

#### heroku 설치

- *$pip insall django_heroku*

- 안되면

  - *$brew install postgresql* 

  

#### Heroku Cli (command line interface)

- *$heroku login* 
  - Chrome으로 떠야 함

- *$herocu create* [서버이름]
  - 외부에 빈 서버가 하나 생길거임 
- *$git push heroku master*
  -  

### Heroku Dashboard

- dashboard에서 deploy되는 앱 관리 가능.

- [https://dashboard.heroku.com/apps](https://dashboard.heroku.com/apps)

#### DB 관리 

- Resouces 탭에서 관리
- Settings - Mores - run console
  - *$python manage.py migrate* 로 migrate해야함.(DB를 안올리기 때문)



### 보안

- setting.py 

``` python
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kmk-vn+7kg#l$tb=^1nidgey9vg%*5t2^df%w9gh5ys8lp(r19'	
```

- 같이 올리면 안되는 파일들 
  - .gitignore 에 등록





### NOTE

- 배포시 STATIC 파일들을 한곳에 몰아 넣는게 바람직 함.

  - 배포시 자동으로 STATIC collect 가 실행되고 

  - ``` python
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    ```

    - root에 static 폴더가 생길 예정

- Data dumping

  - $python manage.py dumpdata (보여주기만 함)
    - DB에 들어있는 데이터가 json형태로 보여줌 

  - master folder 말고 다른 app 폴더에 
    - fixtures 폴더 생성
      - 여기에 json 데이터 넣어두면
        - *$python manage.py dumpdata > board/fixtures/data.json*
      - *$python manage.py loaddata* *data*.json할때 알아서 fixtures폴더에서 찾아줌