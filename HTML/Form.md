#### form

- 화면에 입력된 값을 서버로 전송하기 위해 사용. (다른 목적 없음)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h1>Form Test</h1>
<form action ="a" method = "GET"> <!-- a라는 서버 프로그램에 get방식으로 전달할거다 -->
ID <input type ="text" name = "nm"><br>
PWD <input type ="password" name = "pwd"><br>
<input type="reset" value ="RESET">
<input type="submit" value ="lOGIN">
</form>
</body>
</html>

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

#### Form List

- 기억 할 것. 항상 name은 존재한다.

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h1>Form List</h1>

<form>
<fieldset>
<legend>Employee Register</legend>		<!-- 테두리 박스치기  -->
TEXT	<input type ="text" name ="tx"><br>
PASSWORD<input type ="password" name ="pwd"><br>
Male	<input type ="radio" name ="g" value = "m">  <!-- radio는  여러개중 한개 선택하게 함 단 name을 같게 하고 vlaue는 다르게. -->
Female	<input type ="radio" name ="g" value = "f">
Aje		<input type ="radio" name ="g" value = "a">
<hr>
Apple <input type ="checkbox" name ="f" value = "a">	<!-- checkbox는 동시에 여러개 선택가능 단 name은 같고 value는 모두 달라야함 -->
Grape <input type ="checkbox" name ="f" value = "g">	<!--  이름이 f로 서버로 동시에 날라감 -->
Orange <input type ="checkbox" name ="f" value = "o">
Melon <input type ="checkbox" name ="f" value = "m">
<hr>
<select name = "car">
	<option value ="h">Hyundai</option>
	<option value ="k">Kia</option>
	<option value ="s">SSang</option>
	<option value ="c">Chev</option>
</select>
<hr>
File <input type = "file" name = "ff">
<hr>
<input type ="button" value ="Button"> <!--  이건 의미없는 버튼 -->
<hr>
<input type ="submit" value ="SUBMIT"> <!--  요건 서버로 날리는 버튼 -->

</fieldset>
</form>

</body>
</html>
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





## HTML5 Form

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

```html
TEL<input type="tel" 
pattern="[0-9]{3}-[0-9]{4}-[0-9]{4}"
title="###-####-####"
name="f" required="required"><br>
```

- 패턴주고 그거에 맞게 사용. ex) email add.
- 정규식 모아둔 곳
  - http://regexlib.com











### Bootstrap



- 포트폴리오 사이트를 만드는 게 목표 
- git에다가 올리기 





