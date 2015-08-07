// $.post('/order/detail', {
// 	'deliverId': '14263863782'
// }, function (ret) {
// 	if(ret.code == 0){
// 		console.log(ret.order)
// 	}
// })

var jQorderInput = $("#j-order-id");
var jQorderBtn = $("#j-search-btn");

jQorderBtn.bind('click', function(){
	var orderId = jQorderInput.val();
	if(orderId == ''){
		alert("请输入订单配送id");
	}else{
		orderId = $.trim(orderId);
		window.location.href="/order/"+orderId;
	}
})