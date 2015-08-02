var getCookie = function(c_name){
	if (document.cookie.length>0){
	  c_start=document.cookie.indexOf(c_name + "=")
	  if (c_start!=-1){ 
	    c_start=c_start + c_name.length+1 
	    c_end=document.cookie.indexOf(";",c_start)
	    if (c_end==-1) c_end=document.cookie.length
	    return unescape(document.cookie.substring(c_start,c_end))
	    } 
	  }
	return ""
}

function setCookie(cname, cvalue, exdays) {
	var exdate=new Date();
	var expires;
	if(exdays){
	exdate.setDate(exdate.getDate() + exdays);
	expires = exdate.toUTCString();
	}else{
		expires = exdate;
	}
document.cookie = cname + "=" + encodeURIComponent(cvalue) + "; path=/" +"; expires="+expires;
}	
// var poiId = getCookie('poiid');
$('#j-order-list').delegate(".j-delete", 'click', function() {
	var jQself = $(this);
	orderId = jQself.data('id');
	delConfirm = confirm("是否确认删除订单？");
	if(delConfirm){

	}
});

$("")