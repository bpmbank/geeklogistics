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


var jQusrInput = $('#j-user-input');
var jQpswInput = $('#j-psw-input');
var jQloginBtn = $('#j-login-btn');

jQloginBtn.bind('click', function(){
	var username = jQusrInput.val();
	var password = jQpswInput.val();
	$.post('/api/v1/poi/login', {
		username: username,
		password: password
	}, function(ret){
		if(ret.code ==0){
			var poiId = ret.data;
			setCookie('poiid', poiId);
			window.location.href = '/list/'+poiId;
		}else{
			alert(ret.msg);
		}
	})
})
