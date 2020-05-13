# Node.js

> JavaScript 실행 환경  (out of browser)

`12.16.3 LTS` 버전 다운로드



`chocolathy` : 패키지 매니져



**`npm`?**

> 자바 스크립트 라이브러리 

`pip` vs `npm`



`dependency`



`Vanilla.js` : 세상에서 가장 빠르고 강력한 => 순수 자바 스크립트로 짭쉬받 





# JS

> 웹 페이지의 동적 

of the brower, by the brower, for the brower



`ES6 + ` 기준 

`backtick` 활용 

```javascript
const age = 10
const word1 = `Jae is ${age} years old` 
```

`null` : 개발자가 인위적으로 표시해주는 값 (값이 없음을 나타냄)

- `typeof null`  : `object`

`undefined` : 변수 할당하고 JS엔진이 자동으로 넣어주는 값

- `typeof undefined` : `undefined`



**Browser**

3대 요소 : `DOM`,`ES`,`BOM`

`BOM` : Browser Object Model => console.....

`DOM`: Document Object Model

`ES` : ECMA Script



`JS`의 존재 이유 ? => `DOM` 조작 



`Vanila JS`  vs `node JS`

> `브라우져` vs `서버`



## ES (Vanila JS)

**Variable**

`let` vs `const`

- `let`: 재할당 가능

- `const` : 재할당 불가능

```javascript
// 재할당이 불가능  != 값이 변할 수 없다.
// 엄연히 다른 말이다.
const a=[1,2,3]
a = 1 //불가능
a.push(4) // 가능
```

**Conventions**

- `airbnb style guide`

- `lowerCamelCase` : JS Naming Convention :

- **절대 느슨한 일치 연산자를 사용하지 않는다.**

  ex) `==`, `!=`  [x]

**Functions**

> JS는 함수로 시작해서 함수로 끝나는 언어라고 해도 과언이 아니다.

- 1급 객체 
  1. 변수에 저장할 수 있다.
  2. 함수의 리턴값이 될 수 있다.
  3. 함수의 인자가 될 수 있다.



## DOM

> `html`을  브라우저가 읽을 수 있도록  'object'로 변환한 결과물

예 ) `JSON`은 Object 다. [ X ]

`JSON` : String  "{ 'key': value  }"



`pasring` 하는 과정이 있어야 data를 컴퓨터가 `이해` 할 수 있음



`DOM ` 조작

잡기

`querySelector()`

```javascript
document.querySelector('h1')
myDiv = document.quertSelector('#myDiv')
```

바꾸는거

하드코딩

```javascript
myDiv.innerHTML="<p>hello</p>"
```

p태그를 만들고, 그 안에 텍스트를 집어 넣는다.

```javascript
const myP= document.createElement('p')
=> `<p> </p>`
myP.innerText = 'Greater'

myDiv.appendChild(myP)
```







생성

