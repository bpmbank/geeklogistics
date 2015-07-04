var jQusrInput = $('#j-user-input');
var jQpswInput = $('#j-psw-input');
var jQloginBtn = $('#j-login-btn');

jQloginBtn.bind('click', function(){
	var username = jQusrInput.val();
	var password = jQpswInput.val();
	$.post('/user/login/', {
		username: username,
		password: password
	}, function(ret){
		if(ret.code ==0){
			var poiId = ret.poi
			window.location.href = '/list/'+poiId;
		}else{
			alert(ret.msg);
		}
	})
})
