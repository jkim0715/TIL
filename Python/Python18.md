### 독립환경 구축  

- Python Virtual ENV
  - GLOBAL 환경과 어느것도 연관되지 않고 독립적으로 존재.



### 가상환경 (모든 파이썬 프로젝트에 적용됨)

### venv 폴더

- 터미널을 가상환경을 만듬
  - python venv venv
- 터미널이 가상환경을 보도록 만듬 
  - source venv/Scripts/activate
- F1 -> Select Interpreter -> .`\venv\ 선택
- pip freeze
  - install된 내역 버전까지 상세보기 



### requirements.txt(국룰)

- Pip freeze한 내역 기록하는 부분
  - 복사 붙여넣기 해도 되는데 extension을 이용하도록 하자
  - pip freeze > requirements.txt



### .gitignore

- venv/
  - venv 파일에 설치되는 내역은 requirements에 다 나와있으므로 굳이 git에 올릴 필요 없음.
- .vscode/
  - vscode설정파일인데 



### Django Extension

- django 자동완성 지원
- Extension Django 0.19.0
  - ctrl + ,
    - association
      - Edit in settings .json



### Dummy Data

- **Faker**

  - pip install faker

  - from faker import Faker

    f = Faker()

  - ```python
    
    ```

  - 



### Interactice Shell

- python manage.py shell
  - 직접 Import해야함
- python manage.py shell_plus
  - pip install django_extensions 
  - pip 



### NOTE

- pip : Print Out

- ```linux
  > : 왼쪽에 있는 것을 오른쪽에 있는 파일에 씌우겠다.
  ```

#### git 관리에서 뺴는 법

1. .gitignore에 등록 

- git rm  --cached manage.py  (파일)
- git rm -r --cached board/ (폴더 )



#### vsCode 단축키

- ctrl + g : 원하는 코드 줄로 이동.



#### Linux 단축키

- cd - 
  - 뒤로가기
- 







lectured by 유태영 강사님