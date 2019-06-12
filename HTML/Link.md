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



``` html
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



