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

