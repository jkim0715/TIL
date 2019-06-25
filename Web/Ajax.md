# Ajax

- 서버와 데이터를 교환하는 기술의 하나.
- 비동기적으로 HTML 페이지 업데이트.
- 전체 페이지를 다시 적재하지 않고 웹 페이지의 일부를 업데이트
  - ex) 네이버 실검순위/ 급상승 검색어 etc..
  - Google Map



두개 숫자 계산하기.

```javascript
function sendData(n1,n2){
	var surl = 'calc1';
//여러가지 정보를 집어 넣을땐?  -- 객체 쓰기 JSON	
	$.ajax({
		url:surl, method:"post", data:{"num1":n1,"num2":n2},
		success:function(result){//alert('['+result+']');
	display(result);
	},
// 전송에 실패했을 때  사용 error..
	error:function(){}
	});
};

$(document).ready(function(){
	$('button').click(function(){
		var num1= $('input[name="num1"]').val();
		var num2= $('input[name="num2"]').val();
	// 함수 하나 그냥 만들어서 전송해 ~	
		sendData(num1,num2);
	});
});

<body>
    <!-- 두개의  숫자 서버로 전송 -->
NUM1<input type="number" name="num1"><br>
NUM2<input type="number" name="num2"><br>
<button>Calc</button>
</body>

```

서버 데이터 연동 Ajax

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

<style></style>
<script>
function display(result){
	
	if(result == '1'){
		$('span').text('사용 가능 한 아이디');
	}else{
		$('span').text('이미 사용중인 아이디 ');
	}
};

function checkId(id){
	$.ajax({
		url:'register',
		data:{'id':id},
		method:'get',
		success:function(result){
		
		// 맞냐 틀리냐 보내면 됨 
			
			display(result);
		}
	});
};

$(document).ready(function(){
	$('input[type="button"]').click(function(){
		
		$('#login_form').attr('method','POST');
		$('#login_form').attr('action','register');	 // 서버에 login이라는 프로그램이 있다고 가정  
		$('#login_form').submit();
	});

	$('input[name="id"]').keyup(function(){
		 var id = $(this).val();
		 checkId(id);
	});
});
</script>
</head>
<body>
<h1>REGISTER</h1>
<!-- // form에서 한글을 던지면 깨져서 나옴 주의! -->
<form id= "login_form">
	ID<input type="text" name="id"><span></span><br>
	PWD<input type="password" name="pwd"><br>
	NAME<input type="text" name="name"><br>
	<input type="button" value="REGISTER">
	
</form>
</body>
</html>
```

실시간 데이터 연동 

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

<style>
div{
	width:300px;
	border:2px solid red;
	
}
</style>
<script>

function display(data){
//jQuery for문	.each();
	$('div').empty(); // 업데이트가 append형식으로 되니까 한번 비워주기.
	$(data).each(function(index,item){
		
		var str ="";

		str += '<h3>';
			str+= item.rank+" "+ item.keyword+" "+item.cnt;
			if(item.type =='up'){
				str+= '<img src="a1.png">';
			}else{
				str+= '<img src="a2.png">';
			}

		str += '</h3>';	

		$('div').append(str);
	});
};
function getData(){
	$.ajax({
	// 서버이름 설정.. 내맘대로..	
		url:'chart',
	//method를 안쓰면 default 값으로 자동 설정됨.
		success: function(result){
			// String을 Object으로 만들어 주기 위해 eval을 씀..
			
			display(eval(result));
		}	
	});
};	
$(document).ready(function(){
	getData();
	setInterval(getData,3000);
});
</script>
</head>
<body>
<h1>Keyword Chart</h1>
<div></div>
</body>
</html>
```

```html
package com.sds;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;



/**
 * Servlet implementation class ChartServlet
 */
@WebServlet({ "/ChartServlet", "/chart" })
public class ChartServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#service(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	//JSON 형태로 만들어주는 API가 있어야댐.. 근데 지금 여기JDK엔ㅇ ㅓㅄ음...-- 다운 받아쓰셈 
		response.setCharacterEncoding("UTF-8"); // 한글 안깨지도록 하는법
		PrintWriter out = response.getWriter();
		
		Random r = new Random();
	//make JSON data	
		JSONArray ja = new JSONArray();
		for(int i=0; i<10; i++) {
			int temp = r.nextInt(10)+1;
			JSONObject jo = new JSONObject();
			jo.put("rank", i+1);	//object
			jo.put("keyword", "김서겸"+temp);
			if(temp%2==0) {
				jo.put("type","up");
			}else {
				jo.put("type","down");
			}
			
			jo.put("cnt",temp);	//object
			ja.add(jo);  //array
		}
	// and response client
		out.print(ja.toJSONString());
		out.close();
		
	}

}

```





#### chart만들기 

- www.highcharts.com
  - demo
    - Edit in JSFIDDLE



```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<!-- highcharts library  -->
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://code.highcharts.com/modules/exporting.js"></script>
<script src="https://code.highcharts.com/modules/export-data.js"></script>


<style></style>
<script>
function makeChart(data){
	
	Highcharts.chart('container', {
    chart: {
// 종류별로 chart 바꿀 수 있음 line, pie, bar 		
        type: 'line'
    },
    title: {
        text: 'Seoul Monthly Average Temperature'
    },
 
    xAxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    },
    yAxis: {
        title: {
            text: 'Temperature (°C)'
        }
    },
    plotOptions: {
        line: {
            dataLabels: {
                enabled: true
            },
            enableMouseTracking: false
        }
	},
// JSON만 Series에 넣어주면 됨 !	
// data는 JSON형태로 서버에서 받아올거임 	
	series: data
	// [{
    //     name: 'Seoul',
    //     data: [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
    // }, {
    //     name: 'Busan',
    //     data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
    // }, {
    //     name: 'Daegu',
    //     data: [5.9, 6.2, 9.7, 10.5, 13.9, 17.2, 19.0, 18.6, 16.2, 8.3, 7.6, 5.8]
    // }]
	});
}; // end makeChart

function getData(){
	$.ajax({
		url:'hchart',
		success: function(data){
		// String으로 출력된 결과를 다시 java ㅊcoding으로 변경 eval.	
			makeChart(eval(data));
		}
	});
};

$(document).ready(function(){
// 문서가 준비가 되면 getdata 요청
	getData();
	setInterval(getData,5000);	
// chart그리기 	
	// makeChart();
	// setInterval(makeChart,5000);


}); 
</script>
</head>
<body>
	<h1>My Charts</h1>
<!-- highchats 에서 가저온 양식	 -->
	<div id="container" style="min-width: 310px; height: 400px; margin: 0 auto"></div>
</body>
</html>
```

#### 서버 hchart

```html
protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {		
		Random r = new Random();
		JSONArray ja = new JSONArray();
		
		
		String datas[] = {"Seoul","Busan","Daegu"};
		
		for(int i=0; i<3; i++) {
			int temp = r.nextInt(20)+1;
			
			JSONObject jso = new JSONObject();
			jso.put("name", datas[i]);
	// data도 array형식이라 한개더 생성		
			JSONArray js = new JSONArray();
			for(int j=0; j<12; j++) {
				js.add(r.nextInt(30)+1);
			}
			jso.put("data", js);
			ja.add(jso);
		}
		
		response.setCharacterEncoding("UTF-8");
		PrintWriter out = response.getWriter();
	// 결과를 String으로 출력 	
		out.print(ja.toJSONString());
		out.close();
		
	}
}
```







