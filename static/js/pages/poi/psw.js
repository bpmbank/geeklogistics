var jQusrInput=$("#j-username");
var jQoriginInput = $("#j-origin-psw");
var jQnewInput = $("#j-new-psw");
var jQrepeatInput = $("#j-repeat-new-psw");

$("#j-change").bind('click', function () {
	var username = jQusrInput.val();
	var originPassword = jQoriginInput.val();
	var newPassword=jQnewInput.val();
	var repeatPassword = jQrepeatInput.val();
	if(username==''){
		alert("请输入用户名");
		return;
	}else if(originPassword==''){
		alert("请输入原始密码");
		return;
	}else if(newPassword==''){
		alert("请输入新的密码");
		return;		
	}else if(repeatPassword==''){
		alert("请重复您的密码");
		return;
	}else if(newPassword != repeatPassword){
		alert("请输入相同的密码");
		return;
	}else{
		$.post('/poi/psw/', {
			username: username,
			originPassword: originPassword,
			newPassword: newPassword
		}, function(ret){
			if(ret.code == 0){
				alert("更新成功！请重新登录");
				window.location.href="/coop"
			}else{
				alert(ret.msg)
			}
		})
	}

})