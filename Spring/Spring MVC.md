# Spring MVC



-web.xml

1. dispatcher
2. filter

-spring.xml

1. ViewResolver



View Folder에서 모든 jsp관리 



Spring에서 자동적으로 만들어주는게 많음!

1. ModelAndView
2. Request처리
3. Session처리

```java
	@RequestMapping("/loginimpl.mc")
	public ModelAndView loginimpl(ModelAndView mv,HttpServletRequest request,HttpSession session) {
		String id = request.getParameter("id");
		String pwd = request.getParameter("pwd");
		
		if(id.equals("id01") && pwd.equals("pwd01")) {
			User user = new User(id,pwd,"james");
			session.setAttribute("loginuser", user);
			mv.addObject("center","loginok");
		}else {
			mv.addObject("center","loginfail");
		}		
		mv.setViewName("main");
		return mv;
	}
```

화면에서 입력한 Data를 받는 방법

1. HttpServletRequest

2. USER를 그대로 받는 방법
   - name이 User의 변수 이름과 같아야 함.
3. File 보낼땐? 



Data를 JSON으로 받아와서 Chart 로 뿌리기 

1. Data를 chart로 뿌려주기 위해서 chart 생성.

   - aboutus.jsp 

     - ```html
       <%@ page language="java" contentType="text/html; charset=UTF-8"
           pageEncoding="UTF-8"%>
       <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
       <%@ taglib prefix="spring" uri="http://www.springframework.org/tags" %>
       
       
       <script>
       
       function chart1(pdata){
       	// Create the chart
       	Highcharts.chart('container', {
       	    chart: {
       	        type: 'column'
       	    },
       	    title: {
       	        text: 'Browser market shares. January, 2018'
       	    },
       	    subtitle: {
       	        text: 'Click the columns to view versions. Source: <a href="http://statcounter.com" target="_blank">statcounter.com</a>'
       	    },
       	    xAxis: {
       	        type: 'category'
       	    },
       	    yAxis: {
       	        title: {
       	            text: 'Total percent market share'
       	        }
       
       	    },
       	    legend: {
       	        enabled: false
       	    },
       	    plotOptions: {
       	        series: {
       	            borderWidth: 0,
       	            dataLabels: {
       	                enabled: true,
       	                format: '{point.y:.1f}%'
       	            }
       	        }
       	    },
       
       	    tooltip: {
       	        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
       	        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
       	    },
       
       	    series: [
       	        {
       	            name: "Browsers",
       	            colorByPoint: true,
       	            data: pdata
       	        }
       	    ],
       	   
       	});
       	
       	
       };// chart1 END
       
       $(document).ready(function(){
       	$.ajax({
       		url:'pdata.mc',
       		success:function(pdata){
       			chart1(pdata);
       		}
       	})
       	
       	
       
       });
       
       </script>
       
       <div class ="center_page">
       <h1>About Us Page</h1>
       <div id="container" style="min-width: 310px; height: 400px; margin: 0 auto"></div>
       <spring:message code="welcome.txt" arguments="hi,mulcam"></spring:message>
       </div>
       ```

2. Controller를 이용해 Data를 받아옴

   - MainController.java

     - ```java
       	@RequestMapping("/pdata.mc")
       	@ResponseBody
       	public void pdata(HttpServletResponse rep) {
       		ArrayList<Product> plist = null;
       		try {
       			plist = pbiz.get();
       		} catch (Exception e) {
       			e.printStackTrace();
       		}
       		
       		JSONArray ja = new JSONArray();
       		for(Product p: plist) {
       			JSONObject jo = new JSONObject();
       			jo.put("name", p.getName());
       			jo.put("y",p.getPrice());
       			ja.add(jo);
       		}
       		PrintWriter out = null;
       		try {
       			rep.setCharacterEncoding("EUC-KR");
       			rep.setContentType("text/json;charset=UTF-8");
       			out = rep.getWriter();
       		} catch (IOException e) {
       			e.printStackTrace();
       		}
       ```

3.  Spring 환경에서 카카오 맵 띄워보기

   - register.jsp

     - ```html
       <%@ page language="java" contentType="text/html; charset=UTF-8"
           pageEncoding="UTF-8"%>
       <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
       <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=deba508a56db6a2df5907510c5e9ac0e"></script>
       <script>
       
        $(document).ready(function(){
       	var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
       	var options = { //지도를 생성할 때 필요한 기본 옵션
       		center: new kakao.maps.LatLng(33.450701, 126.570667), //지도의 중심좌표.
       		level: 3 //지도의 레벨(확대, 축소 정도)
       	};
       
       	var map = new kakao.maps.Map(container, options);
       });
       
       </script>
       <body>
       <div class ="center_page">
       <h1>Register Page</h1>
       	<div id="map" style="width:500px;height:400px;"></div>
       
       
       </div>
       </body>
       
       ```

     - 카카오 디벨로버에서 허용 IP address 추가 할 것,

     - 또한 Appkey도 확인하기.

4. 