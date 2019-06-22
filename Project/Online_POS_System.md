```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css?family=Do+Hyeon|Ultra&display=swap" rel="stylesheet">
<title>Insert title here</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<style>
.dv{
	display: table-cell;
	float:left;
	padding: 10px;
	
}

#divm{
	width:400px;
}
.text{
	font-size:10px;
}
.img{
	width: 100px;
	height: 100px;
}
p{
	font-size:10px;
}
 #bt1, #bt11, #bt2, #bt22, #bt3, #bt33, #bt4, #bt44, #bt5, #bt55, #bt6, #bt66{display: none;} 



.ccc{
	display: inline;
	float:left;

}
</style>
<script>
var counta = 0;
var countb = 0;
var countc = 0;
var countd = 0;
var counte = 0;
var countf = 0;

var priceA = "";
var priceB = "";
var priceC = "";
var priceD = "";
var priceE = "";
var priceF = "";

var total = "";

//jQuery 버전 만들기

$(document).ready(function(){
//
	$("#t1").css({'color':'black','text-align': 'center','background':'#FFC596'});
	$("#table2").css({'color':'black','text-align': 'center','background':'#FAFAB4'});
	$("h4").css({'color':'black','text-align': 'center','width':'300px','font-family':'Do Hyeon'});
	$("h1").css({'color':'black','text-align': 'center','font-family':'Ultra'});
	$("HTML").css({'color':'black','text-align': 'center','font-family':'Do Hyeon'});
	$("p").css({'color':'black'});
	$("#tdshow>div").css({'background':'#D7AC87'});
	$("#tdprice>div").css({'background':'#D7AC87'});
	$("#tdcount>div>div").css({'background':'#D7AC87'});
	$("#total").css({'background':'#D7AC87'});
	
	$('#m01').hover(function(){
		$('#m01').css({ 'opacity':'1.0','border':'2px solid black'});
	},function(){
		$('#m01').css({'opacity':'0.9','border':'none'});
	});
	$('#m02').hover(function(){
		$('#m02').css({ 'opacity':'1.0','border':'2px solid black'});
	},function(){
		$('#m02').css({'opacity':'0.9','border':'none'});
	});	
	$('#m03').hover(function(){
		$('#m03').css({ 'opacity':'1.0','border':'2px solid black'});
	},function(){
		$('#m03').css({'opacity':'0.9','border':'none'});
	});
	$('#m04').hover(function(){
		$('#m04').css({ 'opacity':'1.0','border':'2px solid black'});
	},function(){
		$('#m04').css({'opacity':'0.9','border':'none'});
	});
	$('#m05').hover(function(){
		$('#m05').css({ 'opacity':'1.0','border':'2px solid black'});
	},function(){
		$('#m05').css({'opacity':'0.9','border':'none'});
	});	
	$('#m06').hover(function(){
		$('#m06').css({ 'opacity':'1.0','border':'2px solid black'});
	},function(){
		$('#m06').css({'opacity':'0.9','border':'none'});
	});						
//img 클릭시 함수 
	$('img:eq(0)').click(function(){
	// 누르면 수량버튼 보이기	
		$('#bt1').show();		
		$('#bt11').show(); 
	//갈비탕 카운트 증가	
		counta++;				
	//카운트 표시	
		$('#count1').html(counta);
	// 갈비탕 정보  가져오기
		priceA = $('#pr1').html();
		$('#price1').html(priceA *counta);
		$('#show1').html($('#mn1').html());
	//총액 변경
		total += ('+'+priceA);	
		$('#total').html(eval(total));
	}); //첫번째 img 끝 


	$('img:eq(1)').click(function(){
	// 누르면 수량버튼 보이기	
		$('#bt2').show();		
		$('#bt22').show();  
	//닭개장 카운트 증가	
		countb++;				
	//카운트 표시	
		$('#count2').html(countb);
	// 닭개장 정보  가져오기
		priceB = $('#pr2').html();
		$('#price2').html(priceB *countb);
		$('#show2').html($('#mn2').html());
	//총액 변경	
		total += ('+'+priceB);	
		$('#total').html(eval(total));	
	}); //두번째 img 끝 



	$('img:eq(2)').click(function(){
	// 누르면 수량버튼 보이기	
		$('#bt3').show();		
		$('#bt33').show(); 
	//김치찌개 카운트 증가	
		countc++;				
	//카운트 시	
		$('#count3').html(countc);
	//김치찌개 정보  가져오기
		priceC = $('#pr3').html();
		$('#price3').html(priceC *countc);
		$('#show3').html($('#mn3').html());
	//총액 변경	
		total += ('+'+priceC);	
		$('#total').html(eval(total));
	}); //세번째 img 끝 


	$('img:eq(3)').click(function(){
	// 누르면 수량버튼 보이기	
		$('#bt4').show();		
		$('#bt44').show(); 
	//돈까스  카운트 증가	
		countd++;				
	//카운트 표시	
		$('#count4').html(countd);
	// 돈까스  정보  가져오기
		priceD = $('#pr4').html();
		$('#price4').html(priceD *countd);
		$('#show4').html($('#mn4').html());
	//총액 변경	
		total += ('+'+priceC);	
		$('#total').html(eval(total));
	}); //네번째 img 끝 

	$('img:eq(4)').click(function(){
	// 누르면 수량버튼 보이기	
		$('#bt5').show();		
		$('#bt55').show(); 
	//비빔밥  카운트 증가	
		counte++;				
	//카운트 표시	
		$('#count5').html(counte);
	// 비빔밥 정보  가져오기
		priceE = $('#pr5').html();
		$('#price5').html(priceE *counte);
		$('#show5').html($('#mn5').html());
	//총액 변경	
		total += ('+'+priceE);	
		$('#total').html(eval(total));
	}); //다섯번째 img 끝
	
	
	$('img:eq(5)').click(function(){
	// 누르면 수량버튼 보이기	
		$('#bt6').show();		
		$('#bt66').show(); 
	//소고기국밥  카운트 증가	
		countf++;				
	//카운트 표시	
		$('#count6').html(countf);
	// 소고기국밥 정보  가져오기
		priceF = $('#pr6').html();
		$('#price6').html(priceF *countf);
		$('#show6').html($('#mn6').html());
	//총액 변경	
		total += ('+'+priceF);	
		$('#total').html(eval(total));
		
	}); //여번번째 img 끝 


//카운트 업 만들기 
	$('#bt11').click(function(){
		counta ++;

		$('#count1').html(counta);
		priceA = $('#pr1').html();
		$('#price1').html(priceA *counta);
		$('#show1').html($('#mn1').html());
		total += ('+'+priceA);	
		$('#total').html(eval(total));

	});	

	$('#bt22').click(function(){
		countb ++;

		$('#count2').html(countb);
		priceB = $('#pr2').html();
		$('#price2').html(priceB *countb);
		$('#show2').html($('#mn2').html());
		total += ('+'+priceB);	
		$('#total').html(eval(total));

	});	
	$('#bt33').click(function(){
		countc ++;

		$('#count3').html(countc);
		priceC = $('#pr3').html();
		$('#price3').html(priceC *countc);
		$('#show3').html($('#mn3').html());
		total += ('+'+priceC);	
		$('#total').html(eval(total));

	});	
		$('#bt44').click(function(){
		countd ++;
		$('#count4').html(countd);
		priceD = $('#pr4').html();
		$('#price4').html(priceD *countd);
		$('#show4').html($('#mn4').html());
		total += ('+'+priceD);	
		$('#total').html(eval(total));

	});
		$('#bt55').click(function(){
		counte ++;
		$('#count5').html(counte);
		priceE = $('#pr5').html();
		$('#price5').html(priceE *counte);
		$('#show5').html($('#mn5').html());
		total += ('+'+priceE);	
		$('#total').html(eval(total));

	});	
		$('#bt66').click(function(){
		countf ++;
		$('#count6').html(countf);
		priceF = $('#pr6').html();
		$('#price6').html(priceF *countf);
		$('#show6').html($('#mn6').html());
		total += ('+'+priceF);	
		$('#total').html(eval(total));
	});		
				
//카운트 다운 만들기
	$('#bt1').click(function(){
		counta--;
		if(counta < 0){
			return;
		}
		$('#count1').html(counta);
		priceA = $('#pr1').html();
		$('#price1').html(priceA *counta);
		$('#show1').html($('#mn1').html());
		total += ('-'+priceA);	
		$('#total').html(eval(total));
	});	//
		$('#bt2').click(function(){
		countb--;
		if(countb < 0){
			return;
		}
		$('#count2').html(countb);
		priceB= $('#pr2').html();
		$('#price2').html(priceB *countb);
		$('#show2').html($('#mn2').html());
		total += ('-'+priceB);	
		$('#total').html(eval(total));
	});	//
		$('#bt3').click(function(){
		countc--;
		if(countc < 0){
			return;
		}
		$('#count3').html(countc);
		priceC= $('#pr3').html();
		$('#price3').html(priceC *countc);
		$('#show3').html($('#mn3').html());
		total += ('-'+priceC);	
		$('#total').html(eval(total));
	});	//	
		$('#bt4').click(function(){
		countd--;
		if(countd < 0){
			return;
		}
		$('#count4').html(countd);
		priceD= $('#pr4').html();
		$('#price4').html(priceD *countd);
		$('#show4').html($('#mn4').html());
		total += ('-'+priceD);	
		$('#total').html(eval(total));
	});	//	
	$('#bt5').click(function(){
		counte--;
		if(counte < 0){
			return;
		}
		$('#count5').html(counte);
		priceE= $('#pr5').html();
		$('#price5').html(priceE *counte);
		$('#show5').html($('#mn5').html());
		total += ('-'+priceE);	
		$('#total').html(eval(total));
	});	//	
	$('#bt6').click(function(){
		countf--;
		if(countf < 0){
			return;
		}
		$('#count6').html(countf);
		priceF= $('#pr6').html();
		$('#price6').html(priceF *countf);
		$('#show6').html($('#mn6').html());
		total += ('-'+priceF);	
		$('#total').html(eval(total));
	});	//	

// 결제 
	$('#confirm1').click(function(){
		if($('#pay').val()==''||$('#pay').val()=='null'){
			$('#pay').focus();
			alert('결제 방식을 선택하세요 ');
			return;
		}
		if($('input[type="radio"]:checked').val() ==' '|| $('input[type="radio"]:checked').val()=='undefined'){
			alert('포장 하시겠습니까 ?');
			return;
		}
		else{
		alert(eval(total)+'원 결제 하시겠습니까?');
		
		}
	});
	
	$('#cancel').click(function(){
		var result = confirm("주문을 취소하고 나가시겠습니까?");
		if(result){
			alert('잘 가시오');
			location.replace('http://192.168.0.11/kiosk/pos.html');
		}
		
	});

});// ready  end--------------------------------------------------------------
</script>
</head>
<body>
<div class ="dv">
	<div id = "divm" class ="dv">
		<table id ="t1">
			<thead id = "thead1"><tr><th><h1>Cafeteria </h1></th></tr></thead>
			<tbody id = "tbody1">
				<!-- 메뉴 판 -->
				<tr><td><div>
					<form id ="f1">
					<table>
						<thead><tr><th colspan="3"><h4>메뉴</h4></th></tr></thead>
						<tbody>
							<tr><td><img id="m01"  " class ="img" src="images/g1.jpg"><p id ="mn1">갈비탕</p><p id = "pr1">6000 </p></td>
								<td><img id="m02"  " class ="img" src="images/d1.jpg"><p id ="mn2">닭개장</p><p id ="pr2">7000 </p></td>
								<td><img id="m03"  " class ="img" src="images/k1.jpg"><p id ="mn3">김치찌개  </p><p id ="pr3">8000 </p></td>
							</tr>
							<tr><td><img id="m04"  " class ="img" src="images/d2.jpg"><p id ="mn4">돈까스 </p><p id ="pr4">8000 </p></td>
								<td><img id="m05"  " class ="img" src="images/b1.jpg"><p id ="mn5">비빔밥 </p><p id ="pr5">7000 </p></td>
								<td><img id="m06"  " class ="img" src="images/s1.jpg"><p id ="mn6">소고기 국밥 </p><p id ="pr6" >9000 </p></td></tr>
						</tbody>
					</table>
					</form>
				</div></td></tr>
			</tbody>
		</table>
		<p class="text">그림을 선택하여 장바구니에 메뉴 추가 </p>
	</div>

	<!-- 주문확인 -->
	<div class ="dv">
		<table id = "table2">
			<thead><tr><th colspan="3"><h2>주문확인</h2></th></tr></thead>
			<tbody>
				<tr><td>메뉴</td><td>수량</td><td>가격</td></tr>
				<tr>
					<td id ="tdshow">
						<div id ="show1"></div>
						<div id ="show2"></div>
						<div id ="show3"></div>
						<div id ="show4"></div>
						<div id ="show5"></div>
						<div id ="show6"></div>
					</td>
					<td id="tdcount">
						<div >
						
						<input class ="ccc" id = "bt11" " type="button" value="+">
						<div class ="ccc" id ="count1" name= "count1"></div>
						<input class ="ccc" id = "bt1"  " type="button" value="-">
						</div>
						
						<div >
						<input class ="ccc" id = "bt22"  " type="button" value="+">
						<div class ="ccc" id ="count2" name= "count2"></div>
						<input class ="ccc" id = "bt2"  " type="button" value="-">
						</div>
						<div >
						<input class ="ccc" id = "bt33"  " type="button" value="+">
						<div class ="ccc" id ="count3" name= "count2"></div>
						<input class ="ccc" id = "bt3"  " type="button" value="-">
						</div>
						<div >
						<input class ="ccc" id = "bt44"  " type="button" value="+">
						<div class ="ccc" id ="count4" name= "count2"></div>
						<input class ="ccc" id = "bt4" " type="button" value="-">
						</div>
						<div >
						<input class ="ccc" id = "bt55"  " type="button" value="+">
						<div class ="ccc" id ="count5" name= "count2"></div>
						<input class ="ccc" id = "bt5"  " type="button" value="-">
						</div>
						<div >
						<input class ="ccc" id = "bt66" " type="button" value="+">
						<div class ="ccc" id ="count6" name= "count2"></div>
						<input class ="ccc" id = "bt6"  " type="button" value="-">
						</div>
					</td>
					<td id = "tdprice">
						<div id ="price1" name= "price"></div>
						<div id ="price2" name= "price"></div>
						<div id ="price3" name= "price"></div>
						<div id ="price4" name= "price"></div>
						<div id ="price5" name= "price"></div>
						<div id ="price6" name= "price"></div>
					</td>
				</tr>
				<tr><td colspan="3">지불방법 <select id = "pay">
									<option value = "">선택</option>
									<option value = "cash">현금</option>
									<option value = "card">카드</option>
								</select></td></tr>
				<tr>
					<td colspan="2">매장식사<input type="radio" name="pay1" value="p1"></td>
					<td>포장  <input type="radio" name="pay1" value="p2"></td>
				</tr>
				<tr>
					<td colspan="3">총 금액 <div id ="total"></div></td>
				</tr>
				<tr>
					<td colspan="2"><button id="cancel">취소</button></td>
					<td><button id="confirm1">결제</button></td>
				</tr>
			</tbody>
		</table>	
	</div>
</div>


</body>
</html>
```

