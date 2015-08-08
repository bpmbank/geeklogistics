var jQorderBtn = $("#j-order-btn");
var jQcancelBtn = $("#j-order-cancel");

// 商家相关
var jQpoiNameInput = $("#j-poi-name");
var jQpoiPhoneInput = $("#j-poi-phone");
var jQpoiaddressInput = $("#j-poi-address");
//订单相关
var jQorderIdInput = $("#j-order-id");
var jQorderPriceInput = $("#j-order-price");
var jQorderStuffInput = $("#j-order-stuff");
var jQorderTopayInput = $("#j-order-topay");
var jQremarkInput = $("#j-remark");
// 收货人相关
var jQcustomerNameInput = $("#j-customer-name");
var jQcustomerPhoneInput = $("#j-customer-phone");
var jQcustomerAddressInput = $("#j-customer-address");

var jQerr = $("#j-err");
var order = {};
jQorderBtn.bind('click', function(){
	var poiId = $(this).data('poi-id');
	var poiName = jQpoiNameInput.val();
	var poiPhone = jQpoiPhoneInput.val();
	var poiAddress = jQpoiaddressInput.val();
	var orderId = jQorderIdInput.val();
	var orderPrice = jQorderPriceInput.val();
	var orderStuff = jQorderStuffInput.val();
	var orderTopay = jQorderTopayInput.val();
	var remark = jQremarkInput.val();
	var customerName = jQcustomerNameInput.val();
	var customerPhone = jQcustomerPhoneInput.val();
	var customerAddress = jQcustomerAddressInput.val();
	if(poiName == ''){
		jQerr.text('请填写商家名称');
		return;
	}else if(poiPhone == ''){
		jQerr.text('请填写商家联系电话');
		return;
	}else if(poiAddress == ''){
		jQerr.text('请填写商家取货地址');
		return;
	}else if(customerName == ''){
		jQerr.text('请填写收货人姓名');
		return;
	}else if(customerPhone == ''){
		jQerr.text('请填写收货人电话');
		return;
	}else if(customerAddress == ''){
		jQerr.text('请填写收货人地址');
		return;
	}else{
		$.post('/api/v1/order/add', {
			'poiId': poiId,
			'poiName': poiName,
			'poiPhone': poiPhone,
			'poiAddress': poiAddress,
			'orderId': orderId,
			'orderPrice': orderPrice,
			'orderTopay': orderTopay,
			'orderStuff': orderStuff,
			'customerName': customerName,
			'customerPhone': customerPhone,
			'customerAddress': customerAddress,
			'remark': remark
		}, function(ret){
			if(ret.code == 0){
				window.location.href = '/order/success/'+ ret.data;

			}else{
				alert(ret.msg);
			}
		});
	}



})



