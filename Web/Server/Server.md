## **server**



##### 서버파일 위치 (Servlet)

- java resources
  - src
    - servlet



이름이 똑같은게 있으면 서버가 안뜸.



#### Servlet file

- HelloServlet

  - /hello

  - ```
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    //데이터를 받는건 request
    		String id = request.getParameter("id");
    		String pwd = request.getParameter("pwd");
    		//console에 받은 데이터 찍어보기
    		System.out.println(id+" "+pwd);
    HTML5 결과를 만들어줘야함-----------------------------------------------------		         나가는건 response 담당.
    		response.setContentType("text/html;charset=UTF-8");
    		response.setCharacterEncoding("UTF-8");  
    		
    		// PrintWriter 객체를 생성해서 글쓰는데 이용..
    		PrintWriter out = response.getWriter();
    		out.println("<h1>LOGIN OK</h1>");
    		out.println("<h1>"+id+"님 환영합니다</h1>");
    		out.close();		
    }		
    ```

  - 일일히 out.print 하기 번거롭고 유지보수가 어려움

  - 개선 방법1.	(이 방법도 현업에서는 잘 안씀)

    - ```html
      response.sendRedirect("ok.jsp?id="+id); 
      //ok.jsp 역시 서버 프로그램이다.(web 아래에 위치; javascript resources안에 없음)
      // ok.jsp 가 servlet으로 변경된 후 out.print 다 붙어서 들어옴.  그러나 이방식도 잘 사용하지 않음.	
      ```

  - 개선방법2.(jsp파일을 활용)

    - JSP파일은 실행될때 servlet파일로 바뀌면서 결과를 HTML을 browser로 쏴준다.

    - ```html
      		// 값을 넣어줄수 있다
        		request.setAttribute("id", id);
        		
        		// 객체 만들고 forward 함.
        		RequestDispatcher rd = request.getRequestDispatcher("ok.jsp");
        		rd.forward(request, response);
        		
      ```

    - ```jsp
      <%@ page language="java" contentType="text/html; charset=UTF-8"
          pageEncoding="UTF-8"%>
       
      <!--이 부분은 doget 안에 쓰는거랑 같음.-->        
      <%-- <%
      	int i = 10;
      	String id = request.getParameter("id");
      %>        
               --%>
              
      <%@ taglib prefix ="c" uri="http://java.sun.com/jsp/jstl/core" %>         
      <!DOCTYPE html>
      <html>
      <head>
      <meta charset="UTF-8">
      <title>Insert title here</title>
      </head>
      <body>
      <h1>LOGIN GOOD</h1>
      <h3>${id}님 환영 합니다.</h3>
      <%-- <h1><%=id %></h1>  --%> <!-- 이런식으로 선언된 변수를 가지고 올 수 도 있음 그러나 이런식은 유지보수가 안되므로 항상 HTML은 순정유지 -->
      </body>
      </html>
      ```

## JSTL

- ```jstl
  <!-- JSTL -->
  <c:if test="${cnt>5 }"><h2>High</h2></c:if>
  
  <!-- JSTL CHOOSE WHEN THEN -->
  <c:choose>
  	<c:when test ="${cnt >= 9 }"><h4>1등급</h4></c:when>
  	<c:when test ="${cnt>=8 && cnt<9 }"><h4>2등급</h4></c:when>
  	<c:when test ="${cnt>=7 && cnt<8 }"><h4>3등급</h4></c:when>
  	<c:otherwise><h4>4등급</h4></c:otherwise>
  </c:choose>
  ```

  

### Servlet 페이지 이동

**Dispatcher방식과 Redirect 방식**

서블릿에서 특정 URL이나 페이지로 이동하게 하는 두 가지 방식이 있는데, 두 방식의 차이점에 대해 알아보자.



#### **1. Dispatcher방식 -->forward()**

##### forward()[전달하기]는 클라이언트가 요청하면서 전송한 데이터를 그대로 유지한다.

-   포워딩이 되더라도 주소가 변경되지 않는다. (같은 request영역을 공유하게 됨)



#### **2. Redirect 방식 --> sendRedirect()**

##### Redirect()[이동하기]는 새로운 페이지로 완전히 이동해서 기존 데이터를 하나도 사용할 수 없다.

-   포워딩될 때 브라우저의 주소 표시줄의 URL이 변경된다. 포워딩된 jsp페이지에서는 서블릿에서 request영역에 공유한 속성값에 접근 할 수 없다.

  







```javascript

```