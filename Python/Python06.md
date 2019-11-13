## I. 카카오 API 활용하기

1. 주소 검색하기 (GPS_X, GPS_Y 좌표 받기 위해서)

   [카카오 Developer](https://developers.kakao.com/docs/restapi/local#주소-검색)참고

2. 키워드로 장소 검색하기 

   특정 좌표 주위 검색.



- API 적용하기
  1.  url  = Host + GET +{format}
     - ex) url =  dapi.kakao.com/v2/local/search/address.**json**

- 결과 json 나온거 보고 키값 계속 찾아 들어가기
- **request 보낼 때 반드시 요구조건을 만족해서 보내기**
  - ![request](https://user-images.githubusercontent.com/50862254/68755426-d25f5b80-064b-11ea-9024-0efc3bfbf977.PNG)
  - 카카오 API에서는 *params* 와 *headers*를  요구함.
  - params 는 필수 속성이 있고, 선택 속성이 있는데 상황에 맞게 선택
  - headers는 Authorization Key를 넣어야 해서 필수



### II. APItest

- [apitest](https://github.com/jkim0715/Python/tree/master/Day6/apitest)

- format을 json으로 했는데도 결과 값이 str로 날라오면 json 형태로 바꿔서 뿌리기 

  - json.loads()

- 결과 값의 Keyvalue를 파악해서 원하는 데이터만 파싱해서 dictionary에 넣고 html로 한번에 뿌렸음.

  



### III. 실행 화면

- 검색어 수유 

- ![searchadd](https://user-images.githubusercontent.com/50862254/68754631-68928200-064a-11ea-818e-39e77ce8e93d.PNG)

- 키워드 :  코인

- ![Mapsearch](https://user-images.githubusercontent.com/50862254/68754526-3719b680-064a-11ea-9121-220411cd4193.PNG) 











## NOTE

- API Key 같은 중요한 개인정보는 Github에 공개하지 않아야 한다.
  - AWS Credential Key가 털릴 경우 폭탄 맞을 수 있음.
- 공식 API 문서를 볼 때 주의할 점
  - 요청 방식과 요청을 보내야 할 주소 (End-point)가 어떻게 되는지
  - 필수적인 파라미터가 있는지 
  - 인증키를 어떠한 방식으로 보내야 하는지
- *면접 Tip* :프로젝트 하면서 Map API  써야되는데 카카오가 잘 되있어서 쓰려고 하는데 문서화 한게 시렞 사용할 때랑 다른데 좀 고쳐줬음 좋겠다.
  - document -> documents