### JS, jQuery

- 요소를 찾아서 
  - 요소에 이벤트가 발생하는 것을 포착해서 (Event Listener)
  - 이벤트가 발생 했을 때 어떤 로직을 실행할 지 결정 (Event Handler)

- AJAX

  - 비동기 JS & XML

  - Call Back 

    - 실행은 다른 친구에게 맡겨두고 알람(Call Back)만 받는 구조.

  - 기본적인 문법

    - ```HTML
      <script>
      $(function(){
          $.ajax({
              url = '어느 주소로 요청을 보낼 지',
              method = '어느 request method로 보낼 지',
              data : {
              key : '어떤 형태로 보낼 지'
              },// JS에서는 객채 형태 => 객체를 보냄.
              success : function(data){
              '요청이 성공적으로 완료 됐을 때 Call Back'
              },
              error : function(data){
                  '오류 났을 때 '
              }
              
          })
      })
      </script>
      ```

      ​    \- </body> 바로위에 모두 선언
      
      ​    \- 이유는 속도
      
      ​    \- 위에서부터 읽어내려오기 때문에 마지막에 넣어두는게 좋음.
      
      ​    \- JS 객체는 딕셔너리 형태. but 사용하지 않을 예정.
      
      ​    \- Event Listener - Event Handler(function)
      
      ​    \- console.dir / console.log 로 트러블 슛



### 이벤트 발생

1. JS로 HTML요소를 추가한 다음 AJAX로 서버에 요청을 보내 실제 DB에 반영

2. AJAX로 서버에 요청을 보내 실제 DB에 반영되고 JS로 HTML요소 추가 





### 댓글 수정

- 수정버튼을 누른다 

- 원래의 댓글 내용이 입력창에 들어간다 

- 확인 버튼을 누르면 업데이트 된다.

  - 방법 1: 확인 버튼에 속성을 추가해서 제출 할 때 해당 속성의 유무를 파악해 서로 다른 로직을 탈 수 있도록 한다

  - 방법 2: 수정 할 때 ajax로 제출하는 url 부분을 변수(HTML 속성)로 만들어서 처리 





### Note

- axios
  - 찾아 보기

- 이름
  - % 모듈러
  - { } 퀄리브라켓

- 잘 짜인 코드

  - 가독성

  - 확장성

    