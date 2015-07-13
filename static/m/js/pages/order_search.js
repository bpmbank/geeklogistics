var jQorderInput = $("#j-order-id");
var jQorderBtn = $("#j-search-btn");

jQorderBtn.bind('click', function(){
	var orderId = jQorderInput.val();
	if(orderId == ''){
		alert("请输入订单配送id");
	}else{
		window.location.href="/m/order/"+orderId;
	}
})