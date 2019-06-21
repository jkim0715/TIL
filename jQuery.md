## jQuery

- 일종의 JS 라이브러리.

- JS 문법의 short term 정도라고 생각하면 됄듯.

  

#### 준비

- https://jquery.com/>

- [Download the compressed, production jQuery 3.4.1](https://code.jquery.com/jquery-3.4.1.min.js)

- 다른이름으로 저장 - workspace(web) - day09 - web- newfolder(jquery)에 저장.

- ```css
  <title></title>
  <script src="jquery/jquery.min.js"></script>
  ```

##### CDN 방식

- GOOGLE 같은데서 서버에 저장해둔걸 제공해줌.

- ```html
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  ```

  



## Selector

- ```javascript
  $(document).ready(function(){});   // 이거 외워두기.  window 함수랑 같은거임 
  ```

- 

- css 여러개 줄땐 JSON 이용. ( 제일 많이 쓴다.)

``` javascript
// 문자 불러오기
$().text();
```

```html
$(document).ready(function(){});	// (document)가  준비되면 실행() 해라라는 뜻.
```

```javascript
$(document).ready(function(){ 

	$('h1').text('----------'); 		// 가져올때도 text  뿌릴때도 text
	$('#hh').html('<a href=" ">Click</a>');
	$('.ch').text('Class');
	$('input[type="text"]').css('background','gray');
	$('input[name="pwd"]').css({'color':'red','background':'blue'}); // css여러개를 동시에 컨트롤 하고 싶으면 JSON을 사용하여 넣는다.. 배열이나 딴거 ㅅ쓸생각 ㄴㄴ ㄴ. 키값 벨류값이 없어서 안댐..
    
});	
```

#### nth-child()

```javascript
$('h1:nth-child(2n+1)').css('color','red');  // 만약 h1이 여러개 있으면 jQuery는 다해준다.


```

#### eq()

```javascript
$('h1:eq(4)').css('color','red'); 
or
$('h1').eq(0).css('color','red');	// eq는 0부터 시작.
```



#### **not**()

```javascript
$('h1:not(h1:eq(3))').css('color','red'); // 나뺴고 다.
```



### 이벤트 처리 

```javascript
 // a에 click이 일어나면 함수 실행	
	$('a:first').click(function(){ $('button').show();});
	$('a:last').click(function(){ $('button').hide();});

// hover랑 같은 거
	$().mouseenter();
	$().mouseleave();
// hover $().hover(function(){},function(){});
	$('a').hover(function(){
		$('h1').text('Mouser Enter');
	},function(){
		$('h1').text('Mouser Leave');
	});


//여러개 이벤트를 동시에 처리 $().on({JSON}); 
		$('input').on({
//들어올 때
		focus:function(){
			$(this).css('background','gray');	//this는 'input' 을 의미함 
		},
//키를  땔 때
		keyup:function(){
			alert($(this).val());
		},
// 나갈 때
		blur:function(){
			$(this).css('background','yellow');
		}
	});

```

애니메이션 효과

```javascript
// show(); hide();
// toggle();
// animate();
	$('img').css('position','relative');
		$('button').click(function(){
			$('img').animate({left:'300px', width:'100px', opacity:'0.5'});
		});
```

## 함수



반복문