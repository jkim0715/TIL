## CSS

- www.w3schools.com 기본적으로 여기 다 나와있음.

### 선택자

- 타입 선택자

  - ```css
    모든 h1요소를 선택한다
    h1{
        color:green;
    }
    ```

- 전체 선택자

  - ```css
    * {
        color: red;
    }
    ```

- 클래스 선택자

  - ```css
    모든 hi01 class 선택
    .hi01{
        color:red;
    }
    ```

- 아이디 선택자

  - ```css
    ID가 id01인 친구 선택
    #id01{
        color:red;
    }
    
    모든 h1요소중 ID가 id01인친구 선택.
    h1#id01{
        color:green;
    }
    ```

- 속성 선택자

  - ```css
    	input[type="text"]{
      		background: yellow; 
      	}
      	input[name="id"]{
      		background: yellow; 
      	}
    ```

  - 

- 의사 선택자

  - 

- ### 자손,자식, 형제 결합자

  - ```css
    s1의 직계자식 s2 선택 (자식)
    s1 > s2{
        color:red;
    }
    ```

  - ```css
    s1요소에 포함된 s2선택 (후손)
    s1 s2{
       	color:red;
    }
    ```

  - 

```css
h3:nth-child(2n) {
	color:red;
}
h3:nth-child(2n + 1 ) {
	color:blue;
}
	not(selector)
div> :not(h4) {
	color:red;
}
	not(.class) 클래스가 들어갈 수도 있음
div > :not(.a){
    color:red;
}
```



### 폰트

- 우선순위대로 써넣는다.

```css
	font-family:"Courier New", Times, serif; 
				
```

-  OS 폰트보다 Web 폰트를 사용해야함
  - google fonts 이용.

```css

```

## 박스모델

- div 같은거 ~
- margin 설정.

```css
(전체 마진설정 body포함)
*{
    margin:0;
}

(위 오른쪽 아래 왼쪽 순서)
div{
    margin:50px 0 100px 20px;   
    		
}


```

- 경계선

```css
왼쪽 위부터 시계방향
border-radius: 20px 20px 0 0 ;

그림자 주기
box-shadow: 10px 10px 10px black;


```



- 박스안에 인라인은 제어가 어려움 
  - 따라서 블럭으로 바꿔서 컨트롤 함.

```css
div>a{
	display:block;
	font-size: 2em;
	border: 10px solid red;
	width: 100px;
	margin: 10px auto;
}
```







### CSS를 삽입하는 방법



#### 외부 스타일 시트

- css 파일 따로 만들어서 HTML파일에서 링크만 걸어주면 됨.

```html
<link type="text/css" rel="stylesheet" href="c1.css">
```





#### 주석달기

- comments

  - ctrl + Shift + ? 

  ```css
  /* CSS Comments */
  ```

