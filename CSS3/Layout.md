## Layout

- 박스모델

- 블록 요소와 인라인 요소

  - 블록(block): 화면의 한 줄을 전부 차지

    - ``` html
      <h1>,<p>,<ul>,<li>,<table>,<blockquote>,<pre>,<div>,<form>,<header>,<nav>
      ```

  - 인라인(inline): 한줄에 차례대로 배치, 한 줄에서 필요한 만큼만 공간차지.

    - ``` html
      <a>,<img>,<strong><em><br><input><span>
      ```



### 요소위치 정하기

- #### Position

  - ``` css
    바로 옆에 위치한 요소 기준( relative)
    	position: relative;
    	left: 50px;
    	top:50px;
    
    body 기준 (absolute)
    	position: absolute;
    	left: 50px;
    	top:50px;
    
    특정 위치에 고정 (fixed) 스크롤이 내려가도 유지.
    	position: fixed;
    	left: 50px;
    	top:50px;
    	
    
    ```

- #### float

  - 좌정렬, 우정렬

  - 화면에 맞춰서 조정됨.

  - ``` css
    float: left;
    float: right;
    	
    ```

- #### opacity  ( 1~ 0 )

  - ``` css
    투명화 0 에 가까울 수록 투명해짐.
    opacity: 0.8;
    ```

- #### z-index

  - 숫자는 의미없고 상대적으로 높은 숫자가 우선순위.

  - ``` css
    	z-index: 100;
    ```



- #### overflow

  - 아무리 div가  감싸고 있어도 안의 내용물이 커지면 삐져나간다.
  - 따라서 오차 조절이 중요함.

  - 삐져 나간거 정리 (hidden, scroll, auto)

  - ``` css
    overflow: hidden;
    overflow: scroll;
    overflow: auto; 
    ```

- #### max / min size



#### 의미적 요소를 이용한 레이아웃

- 원래는 이런식으로 사용 했었는데

- ```html
  div id ="header"
  div id ="nav"
  div id   ="footer"
  ```

- HTML5 에서는 그냥 

- ```html
  이것들이 전부 div.
  <header> </header>
  <section> </section>
  <footer> </footer>
  ```

  