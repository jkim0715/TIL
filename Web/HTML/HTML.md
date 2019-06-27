# HTML 

- 전세계가 공통적으로 사용하는 Tag 언어 
- XHTML1.0
- ##### 2012 HTML5 등장
  
  - 웹에서 GPU를 건들일 수 있음.
  - 아직 모든브라우저가 지원하지는 않음.
    - 아직 대부분의 컴퓨터가 사양이 딸려서...





### <http://tomcat.apache.org/>

- 오픈소스 기반 소프트웨어를 커뮤니티 애들끼리 develop 시킴.
- tomcat 9 
  - 64bit windows.zip
  - c 밑에 넣으셈.
- new - Dynamic Web - next - next - day01 drag on to Tomcat9.0 
- web - new - HTML - Select HTML Templete





HTML TEST

```html
http://70.12.50.220:80/day01/a1.html
```

- 자동으로 80은 없어짐.. NAVER같은데서 기본으로 80포트를 쓰기때문.





### www.w3schools.com

- 여기보고 HTML 공부하시오..  이 책 만으로는 부족함.

- HTML , CSS,  JavaScript
- Try it yourself 활용해보기 





```html
<body>
<!-- 주석 만들기  -->    
	<h1><a href=""></a>HTML TEST</h1> 
	<img src = "img01.jpg">
	<img src = "img/img02.jpg">
<!--  에러메시지 안뜨니까 직접가서 확인해봐야함 -->
</body>
```

- ##### 단락주기

```html 

<p>" "  
</p>

<body>
<p>안녕하세요 </p>
<p>HTML입니다.</p>
<p>엔터               입니다.</p>
</body>

```

- ##### 화면 맞추기

```html
<br>
<body>
<p>안녕하세요안녕하세요안녕하세요안녕하세요 </p>
<p>안녕하세요안녕하세요안녕하세요안녕하세요 </p>
<p>안녕하세요<br>안녕하세요<br>안녕하세요<br>안녕하세요 </p>
</body>
```

- ##### 강제 띄우기 

```html
&nbsp;
<p>안녕하세요&nbsp;안녕하세요안녕하세요안녕하세요 </p>
```

- ##### 띄우기 인식 (그러나 해상도에 따라서 짤릴 수도 있음)

- ##### HTML  에서 줄바꿈도 안되고 스페이스도 한번밖에 안먹는데 입력한거 그대로 표시

```html
<pre>
줄을 바꿔도
스페이스를     무진장 띄워도
이대로 표시할 수 있습니다.
</pre>
```

- ##### 문서의 헤드라인 (폰트 사이즈 조정)

```HTMl
<h1>Header</h1>
<h2>Header</h2>
<h3>Header</h3>
<h6>Header</h6>
```





HTML에서 여러개를 묶을수 있는 기능이 한개인데 

### 리스트 

- 여러개를 한번에 관리함.. 한번에 색을주거나 폰트를 키우거나..

```HTML
<ul> 
<li>List1</li>
<li>List1</li>
<li>List1</li>
</ul>

<ol>
    <li>List1</li>
    <li>List1</li>
    <li>List1</li>
</ol>
```



### 링크



```html
WebApp : day02

<h1>
    Hyper Link
</h1>

<h3>
<a href = "http://www.naver.com">Click1</a>    
</h3>
<a href = "http://www.daum.net">Click2</a>


<h3><a href = "b1.html">Click1</a></h3>		같은 디렉토리일때는 바로 이동.
<a href = "b/b2.html">Click2</a>			폴더명/ 쓰고 이동


<h1>Page B2</h1>					
<a href ="../a.html">HOME</a>				상위폴더에 있을땐 [..] 활용
 

```



#### Target 

- script language에서 동일한 이름의 변수를 써도 에러가 안나서 찾는데 어려움

```html
<a href = "b1.html" target="_blank">Click1</a>	<!-- 윈도우에서 새로운 페이지를 연다 -->
<a href = "b/b2.html">Click2</a>
<a href = "#h_target">Click3</a>				<!-- id로 ㄱㄱ -->
<a href = "file/tomcat.zip">Click4</a>			<!-- file 다운로드 -->
<a href = "#" onclick = "send();">Click5</a>	<!-- 손가락 때문에 만듬 // send();는 위에 javascript 부분에서 정의한다. -->
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
<h1 id="h_target">Header1</h1>					id를 정해서 부여 
<h1>Header1</h1>
```



#### CSS/JavaScript 영역 (맛보기)

```html
<!--  css영역 -->
<style>
a{
	text-decoration: noe;
	color: red;
	font-size: 2em;	
}
</style>	
		
<!-- javascript 영역 -->
<script>
function send(){
	alert('Are you OK? ');    // 여기서는 single doulbe quotation 둘다 쓰는데 우리는 single만 쓰기로함
	location.href = 'b1.html';
};   // 여기서는 ;을 찍어서 문장 끝낸다.
</script>

<title>Insert title here</title>
</head>

<body>
<h1>
    Hyper Link
</h1>
<a href = "b1.html" target="_blank">Click1</a>
<a href = "b/b2.html">Click2</a>
<a href = "#h_target">Click3</a>
<a href = "file/tomcat.zip">Click4</a>
<a href = "#" onclick = "send();">Click5</a>	<!-- 손가락 때문에 만듬 -->
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
    
</body>
</html>
```



### 이미지



```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<style>
img{
	width: 100px; 		// width만 설정하면height는 자동설정됨
	height: 130px;		// height 크기를 따로 지정하고 싶음 써도 됨
	display: block;		// 태그의 속성을 css에서 조정 img 일렬로 세로로 세우기(원래는가로)
	
}
</style>
<title>Insert title here</title>
</head>
<body>
<h1>IMG TEST</h1>
<a href ="img/m1.jpg" target ="_blank"></a><img src = "img/m1.jpg">
<img src = "img/m2.jpg">
<img src = "img/m3.jpg">
<img src = "img/m4.jpg">
<img src = "img/m5.jpg">
</body>
</html>
```



### Table

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<style>
	table,td,tr,th{	
		border:2px solid bliack;
	}
	table{
		width: 300px;
		border-collapse: collapse;
	}
</style>
<title>Insert title here</title>
</head>
<body>
<h1>Table Test</h1>

<table border = "1">	<!-- 여기서 이렇게 쓰면 안댐..  css에서 컨트롤 하셈.. 지금은 테스트 용 -->
<caption>Employee List</caption>  <!-- 테이블 제목 -->
<thead> 				<!-- thead는 default 값으로 자동으로 생기지만 반드시 써주자 -->
<tr>
<th>ID</th><th>PWD</th><th>NAME</th>
</tr>
</thead>

<tbody>					<!-- tbody는 default 값으로 자동으로 생기지만 반드시 써주자 -->
<tr>
	<td>id01</td><td>pwd01</td><td>일말숙</td>
</tr>
<tr>
	<td>id02</td><td>pwd02</td><td>이말숙</td>
</tr>
<tr>
	<td>id03</td><td>pwd03</td><td>삼말숙</td>
</tr>
<tr>
	<td>id04</td><td>pwd04</td><td>삼말숙</td>
</tr>
<tr>
	<td>id05</td><td>pwd05</td><td>삼말숙</td>
</tr>
</tbody>				

</table>

</body>
</html>
```



#### Resume 만들기

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<style>
	
		table> tbody > tr{
		text-align: center;
	
	}

</style>


<title>Insert title here</title>
</head>
<body>
	<table border =1>
	<thead>
	</thead>
	<tbody>
	<tr><td rowspan="4"><img src = "img/m2.jpg"></td><td colspan ="4", id ="01">이력서</td></tr>
	<tr><td rowspan ="2">성명</td><td rowspan ="2">김재영</td><td colspan ="2">주민등록번호</td></tr>
	<tr><td colspan ="2">123456</td></tr>
	<tr><td colspan ="4">생년월일  1991년 7월 15일생 (만  세)</td></tr>
	<tr><td>주소</td><td colspan ="4">우리집</td></tr> 
	<tr><td rowspan ="2">연락처</td><td>집</td><td >070-000-0000</td><td rowspan ="2">전자우편</td><td rowspan="2">506@multicam.com</td></tr>
	<tr><td>핸드폰</td><td>010-0000-0000</td></tr>
	</tbody>
	</table>
</body>
</html>
```







##### layout

```HTML
<nav> - Defines a container for navigation links
<section> - Defines a section in a document
<article> - Defines an independent self-contained article
<aside> - Defines content aside from the content (like a sidebar)
<footer> - Defines a footer for a document or a section
<details> - Defines additional details  
<summary> - Defines a heading for the <details> element 
```



### 멀티 미디어



##### 오디오

```html
<audio src ="file/Kalimba.mp3" controls ="controls">
Not Support
</audio>

```

- 브라우저 마다 audio 태그의 모양이 다르다
  - explorer 는 버전마다 다름 



##### 비디오

```html
<video src ="http://media.w3c.org/2010/05/bunny/movie.ogv" 
controls = "controls"></video>

```

#### iframe

- 쓰면 안됨.. 바이러스의 온상



#### div와 span

- **div**
  
  - block이라 다 차지하지만 **사이즈를 결정할 수있다**.
  - div로 layout을 잡고 그 안에다 내가 치장하는 것임
  
- **span** 
  
  - div 안에서 한곳만 바꾸고 싶을때 span을 이용
  - span은 Inline임.
  
- div 와 span의 차이점.

  -  div 가로폭을 전부 차지함. span 태그안의 내용만 차지함

  -  필연적으로 줄 바꿈을 동반, span 줄 바꿈 없고 문장 중간에 들어갈 수 있음

  -  table 태그 대신 div와 span 태그로 더욱 간결한 html을 구성할 수 있다.

    

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<style>
div{
	background : blue;
	width:300px;
	height:50px;
	color:yellow;
}
span{
	color:red;
}
</style>
<title>Insert title here</title>
</head>
<body>
<h1> DIV Test</h1>

<div>Block <span>Area</span> Blue Zone..</div>
</body>
</html>
```



### 데이터 전송 방식 <form>

##### Get 방식 

-  URL 주소 뒤에 파라미터를 붙여서 데이터를 전달하는 방식.
  - 글자수 제한(2048글자)
  - 비밀보장 x (패스워드 같은걸  Get방식으로 보내면 큰일난다는 말임)
  - 북마크 가능 & 뒤로가기 보장 !

##### Post 방식 

- 사용자가 입력한 데이터를 HTTP Request  gpejdp 포함시켜서 전송하는 방식.

  - 길이에 제한이 없음
  - 보안유지 가능
  - POST 요청은 캐시되지 않으며 브라우저 히스토리에도 남아있지 않다.
  - 북마크 불가능, 뒤로가기 누를 시 데이터를 다시 보내야한다는 alert이 발생.

- ```html
  POST/ test/ input.jsp HTTP/1.1
  Host: www.naver.com
  name1=value1&name2=value2
  ...
  ```



## form 이란?

- 화면에 입력된 값을 서버로 전송하기 위해 사용. (다른 목적 없음)

```html
<body>
<h1>Form Test</h1>
<!-- a라는 서버 프로그램에 get방식으로 전달할거다 -->    
	<form action ="a" method = "GET"> 
ID <input type ="text" name = "nm"><br>
PWD <input type ="password" name = "pwd"><br>
<input type="reset" value ="RESET">
<input type="submit" value ="lOGIN">
</form>
</body>
```



- 다른방법

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<script>
function login(f){
	var c= confirm('Are You Login ..');
	
	if ( c == true){
		f.method = 'GET';
		f.action = 'a';
		f.submit();
	};
};
</script>

<title>Insert title here</title>
</head>
<body>
<h1>Form Test</h1>
<form>
ID <input type ="text" name = "nm"><br>
PWD <input type ="password" name = "pwd"><br>
<input type="reset" value ="RESET">
<input onclick ="login(this.form);" type="button" value ="lOGIN">
</form>
</body>

</html>

```

## Form List

- ##### 기억 할 것. 항상 name은 존재한다.

  - ##### 서버에서는 name속성을 변수 이름처럼 생각해 값을 참조한다.

```html
<body>
<h1>Form List</h1>
<form>
<!-- fieldset 은 입력 요소들을 grouping 하는데 사용됨. (테두리를 그려줌)-->
 	<fieldset>
<!-- 테두리 박스치기  -->
    <legend>Employee Register</legend>	
    
<!--  ID /PWD 입력창에 주로 씀 -->   
	TEXT	<input type ="text" name ="tx"><br>
	PASSWORD<input type ="password" name ="pwd"><br>
    
<!-- radio는  여러개중 한개 선택하게 함 단 name을 같게 하고 vlaue는 다르게. -->
    Male	<input type ="radio" name ="g" value = "m">  
	Female	<input type ="radio" name ="g" value = "f">
	Aje		<input type ="radio" name ="g" value = "a">

<!-- checkbox는 동시에 여러개 선택가능 단 name은 같고 value는 모두 달라야함 -->
<!--  이름이 f로 서버로 동시에 날라감 -->
	Apple <input type ="checkbox" name ="f" value = "a">	
	Grape <input type ="checkbox" name ="f" value = "g">
	Orange <input type ="checkbox" name ="f" value = "o">
	Melon <input type ="checkbox" name ="f" value = "m">
    
<!--선택버튼 -->
	<select name = "car">
		<option value ="h">Hyundai</option>
		<option value ="k">Comedy</option>
		<option value ="s">Romance</option>
	</select>
<!-- 파일 업로드 버튼. 
form 태그에 속성으로  enctype ="multi-part/form-data"  를 추가해주는게 좋음.  -->

	File <input type = "file" name = "ff">
    
<!--  이건 의미없는 버튼 -->
	<input type ="button" value ="Button">
    
<!--  요건 서버로 날리는 버튼 -->
	<input type ="submit" value ="SUBMIT"> 

</fieldset>
</form>
```



### Label

```html
<label for ="male">Male</label>
<input id="male" type ="radio" name ="g" value = "m">
```



#### Hidden

```html
<input type = "hidden" name ="geo" value ="fff">
```





### HTML5 Form

form 사이.

```html
<form>
Level<input value="level1" type="text" name="le" readonly="readonly">
DATE<input type="date" name="d"><br>
COLOR<input type="color" name="c"><br>
EMAIL<input type="email" name="e"><br>
TEL<input type="tel" name="f" required="required"><br>
NUMber<input type="number" name="num"><br>
Range<input type="range" min="1" max="10"
  name ="range"><br>
<input type="submit" value="register">
</form>
```

- readonly는 반드시 value 값 포함해야함
- required 는 반드시 채워야 하는 칸을 만듬





#### 정규식

- http://regexlib.com 참고
- 패턴주고 그거에 맞게 사용. ex) email add.

```html
TEL<input type="tel" 
pattern="[0-9]{3}-[0-9]{4}-[0-9]{4}"
title="###-####-####"
name="f" required="required"><br>
```













