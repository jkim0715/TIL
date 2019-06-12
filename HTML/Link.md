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
<a href = "#" onclick = "send();">Click5</a>	<!-- 손가락 때문에 만듬 -->
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
<h1>Header1</h1>
<h1 id="h_target">Header1</h1>					id를 정해서 부여 
<h1>Header1</h1>
```







