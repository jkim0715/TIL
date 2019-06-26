### HTML5 웹 스토리지, 웹 소켓, Drag & Drop

#### Web storage (HTML5 제공)

- local storage
  - 브라우져를 닫아도 안없어짐.  but 해당 브라우저에서만 저장.
- session storage
  - 브라우져를  닫으면 없어짐 

``` html
<!-- F12 application, storage 에서 key value값 확인가능.-->
<script>
$(document).ready(function(){
	$('button').eq(0).click(function(){
		sessionStorage.m='sid01';		//m은 임의의 키 값, 'side01'은 임의의 value값.
		});
	$('button').eq(1).click(function(){
		localStorage.m='lid01';	// 넣을때 꺼낼때 동일하게 
		});
});
</script>
```





#### Web socket (서버와 양방향 소통 가능.)

- 보통 web browser에서 데이터를 서버에 요청해야 데이터를 받지만  Web socket을 이용하면 요청없이도 서버에서 데이터를 browser로 보낼 수 있음. 
- work flow :

1. ```
   1. open
   2. onmessage(대기)
   3. send 데이터 전송
   4. onmessage invoke
   5. 서버가 데이터 전송
   6. onmessage invoke
   ```



#### Drag & Drop

- 이미지 같은것들을 Drag & Drop으로 각 div에 옮길 수 있도록 만듬

- 사용되는 attributes:

  - ``` html
    <div ondrop="mydrop(event)" ondragover="allowdrop(event)">	
    	<img src ="b1.jpg" id="m1" draggable="true" ondragstart="mydrag(event)">
    </div>	
    ```

- 사용되는 함수 

  - ```html
    <script>
    function mydrop(e){
    	e.preventDefault();
    	var src = e.dataTransfer.getData('m');	// mydrag에서 세팅한 m
    	e.target.appendChild(document.getElementById(src));
    	// 	$(e.target).append($('#'+src));   //jQuery
    };
    function allowdrop(e){
    	e.preventDefault();
    };
    function mydrag(e){
    	e.dataTransfer.effrectAllowed = 'move';
    	e.dataTransfer.setData('m',e.target.id);  //m이라는 이름으로 저 장
    };
    </script>
    ```

- HTML body

  - ```html
    <body>
    <h3>Item</h3>    
        <div ondrop="mydrop(event)" ondragover="allowdrop(event)">	
    		<img src ="b1.jpg" id="m1" draggable="true" ondragstart="mydrag(event)">
    		<img src ="d1.jpg" id="m2" draggable="true" ondragstart="mydrag(event)">
    		<img src ="d2.jpg" id="m3" draggable="true" ondragstart="mydrag(event)">
    		<img src ="g1.jpg" id="m4" draggable="true" ondragstart="mydrag(event)">
    		<img src ="k1.jpg" id="m5" draggable="true" ondragstart="mydrag(event)">
    	</div>
    <h3>Cart</h3>
    	<div ondrop="mydrop(event)" ondragover="allowdrop(event)"> 
            					<!--ondragover는 필수다 라는걻 발견함 ㅇㅇ -->
    </body>
    
    ```



#### Google Maps 를 이용한 프로젝트

