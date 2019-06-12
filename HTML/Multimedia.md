### 멀티 미디어



#### 오디오

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<h1>Audio Test</h1>
<audio src ="file/Kalimba.mp3" controls ="controls">
Not Support
</audio>
</body>
</html>
```

- 브라우저 마다 audio 태그의 모양이 다르다
  - explorer 는 버전마다 다름 



#### 비디오

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="EUC-KR">
<title>Insert title here</title>
</head>
<body>
<video src ="http://media.w3c.org/2010/05/bunny/movie.ogv" 
controls = "controls"></video>
</body>
</html>
```

#### iframe

- 쓰면 안됨.. 바이러스의 온상



#### div와 span

- div
  - block이라 다 차지하지만 사이즈를 결정할 수있다.
  - div로 layout을 잡고 그 안에다 내가 치장하는 것임
- span 
  - div 안에서 한곳만 바꾸고 싶을때 span을 이용
  - span은 Inline임.

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

