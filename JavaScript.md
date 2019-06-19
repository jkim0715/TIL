## JavaScript



```javascript
alert('1');
alert('2');
alert('3');

```

### document.write

``` javascript
var now = new Date();
document.write(now);    /* body랑 body 사이에다가 now를ㄹ 뿌리라는이야기 */
```



```javascript
setInterval(function() {
		var now = new Date();
		document.write(now);
	}, 1000);

```



### 외부 자바스크립트

```javascript
<script src = "j1.js"></script> //연동
```



### 인라인 자바스크립트 (지양할것)

```javascript
<h1 onclick="alert('ok');">JavaScript Test</h1>
```





#### 변수

- JS는 var로 통일

```javascript
//1.number
var v1 =10;
//2. boolean
var v2 = true;
//3.string
var v3 = "hhihih"
//4. object
var v4 = {};
// 5. function
var v5 = function(){};
//6. array
var v8 =[1,2,3,'a'];
//7. undefined
var v9;
//8. null
var v10 = null;

alert(typeof(v10));


```

### JavaScript Object

- JSON (JavaScript Object Notation)

``` javascript
var v5 = {name:'k1', size:1000, go:function(){},stop:function()[]};\

var v6 = {name:'k1' ,size:1000};   // v6만 날리면 name이랑 size가 같이 날라감.

//배열로 받기

var person = [
{id:"id01" , name:"일말숙" },
{id:"id02" , name:"이말숙" },
{id:"id03" , name:"삼말숙" },
{id:"id04" , name:"사말숙" },
{id:"id05" , name:"오말숙" }
];


```

- 요즘 데이터를 주고 받는 표준 form 으로 많이 쓰임.



#### 연산자

```javascript
var a = 10;
var b = '20';

alret(a+b); // 1020
alret(a*b); // 200

//  + 빼고 num와 String 연산이 다 가능.
// 굳이 더하고 싶다면
alert(a+parseInt(b));
//혹은
alert(String(a));
```





### prompt() 함수

- 사용자에게 어떤 사항을 알려주고 사용자가 답변을 입력할 수 있는 윈도우를 화면에 띄운다.
- 기본적으로 JS에서 입력받은 모든 변수는 String으로 받는다

``` javascript
// 입력값  반환
var d = prompt('input pwd', '');

//
var p1 =prompt('Input Number 1');
var p2 =prompt('Input Number 2');


var result = parseInt(p1) + parseInt(p2) ;
// 에러 체크 : 콘솔창에 값 표시
console.log(result);
// 에러체크 : alert으로 값 확인( 위에 것 지향)
alert(result);
```

##  confirm() 함수

``` javascript
// 확인 true  취소 false 반환
var c = confirm('are you sure?');
```



### calc() 함수

``` javascript
function calc(){
	
// n1,n2 값 가져오기
	var num1 = document.getElementById('n1').value;
	var num2 = document.getElementById('n2').value;
	
// n1 + n2
	var sum = Number(num1) + Number(num2);
	
//result 미리 가져오기
	var r= document.getElementById('result')
	
	r.style.color= 'red' ;
// 값을 HTML body 사이에 집어 넣기.
	r.innerHTML = sum  ;  
	
	
	var rr = document.getElementById('rr');
	rr.value = sum;    //input form에서는 value라고 함.
// 	r.innerHTML = '<a href ="">' +sum +'</a>' ;  
	//결과값을 수정 못하게 하려면?
			
			
};
```

```javascript

```



### JS 랜덤 숫자 받아오기

```javascript
// 0~ 1 미만
var cnum = Math.random();


// 0~ 100까지 정수
var cnum = Math.floor(Math.random()*100+1);
```



### function 활용 I

```javascript
alert(typeof(v3));

```

```javascript
//Return type이랑 argument에 type이 없는 이유는 JS에서는 어짜피 var 하나기 때문에 생략됨.

//함수 선언방법1.
function a(){
	alert('a');
};

//똑같은 이름의 함수가 중복되면 아래라인에 있는 함수가 호출 됨 !! 주의 !
function a(){
	alert('aaa');
};

// 함수 실행선언 방법 2.
var b= function (){
	alert('b');
};

```



### function 활용 II

``` javascript
function a(k){
	return 10 *k;
};
function b(){
	return 20;
};

// 두개의 함수 a,b가 있고,  함수 c의 argument에 함수를 넣을 수 있음. 함수 i, 함수 j, k...z
function c(i,j){
	var result = i()+j();
	return result;
}
// 실행1.
var data = c(a,b);  // 일단 여기에 argument가 있는 함수는 못들어감.. 넣고싶으면 c 안에서 조정 해야함
alert(data);
// 실행 2.   함수를 만들어서 넣기도 가능.. 대부분 이런식으로 사용.
var data1 = c (a, function(){
	return 500;
});

```

### 딜레이 주기 setInterval( , );

```javascript
// 기준은 ms. 
setInterval(function(){ alert('hi');}, 3000);
// 3초에 한번 함수 실행 (hi)


```



### return값 함수로 받기

```javascript
var f1 = function(){
	return function(i){
        return 100*i;
    };
};

//활용
 var f2 = f1();
 var result = f2(2);
 alert(result);

// ans : 200
```



### Error 검사 (Exception 처리 )

```javascript
try{
c = new Daate();
}catch(error){
	alert('Network Error..');
}
```



### DOM (Document Object Model)

- 규칙이 있는 문서 모델.
  - HTML, XML, word
- 트리구조



#### document.getElementById()

```javascript
var h1 = document.getElementById('h1')  // <h1 id = 'h1'>Test</h1> 을 지칭.
var h1 = document.getElementById('h1').innertText // Test를 지칭.


var h1 = document.getElementById('h1').innerText; // 가져올때도 innerText  뿌릴 때도 innerText

	 document.getElementById('h1').innerText = h1 +'ADD TEXT';


	var id = document.getElementById('id').value;

	document.getElementById('id').value = id +'ADD iD';
```





### BOM (Browser Object Model)







quotation:

Java = double

JS = single



