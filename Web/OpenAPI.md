- 쉬운버전

```xml
<temps>
<temperature>
	<name>Seoul</name>
	<data1>10</data1>
	<data2>20</data2>
	<data3>30</data3>

</temperature>

<temperature>
	<name>Busan</name>
	<data1>10</data1>
	<data2>20</data2>
	<data3>30</data3>

</temperature>
</temps>
```



```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://code.highcharts.com/modules/exporting.js"></script>
<script src="https://code.highcharts.com/modules/export-data.js"></script>


<style></style>
<script>
function makeChart(datas){
	
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
	series: datas
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

// object 만들기  name이랑 data를 속성으로 가진 object임.
function Temp(n,d1,d2,d3){
	this.name = n;
	this.data = [d1,d2,d3];

};

function parsing(data){
// 이건은 배열임/  temperature tag가 여러개니까.	
	var ts = $(data).find('temperature');
	
	var datas =[];
// 배열 jQuery 	
	ts.each(function(index,item){
	// 여기서 this는 item 하나. temperature 안에 데이터들 []	
		var name = 		$(this).find('name').text();
		var data1 = 	$(this).find('data1').text();
		var data2 = 	$(this).find('data2').text();
		var data3 = 	$(this).find('data3').text();
	
	// 여기서 문제는 object를 만들고 배열을 만들어야댐.
	// data1,2,3을 넘버로 바꿔서 넣어줘야댐  Number(data)	
		var obj =
		new Temp (name,Number(data1),Number(data2),Number(data3));  //number(data1) 소문자로 하면 안댐..
		datas.push(obj);
	});
	makeChart(datas);
};

function getData(){
	$.ajax({
		url:'temp.xml',
		success: function(data){
			parsing(data);
		// String으로 출력된 결과를 다시 java ㅊcoding으로 변경 eval.	
			// makeChart(eval(data));
		}
	});
};

$(document).ready(function(){
// 문서가 준비가 되면 getdata 요청
	getData();
	// setInterval(getData,5000);	
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



