var jQusrInput = $('#j-user-input');
var jQpswInput = $('#j-psw-input');
var jQloginBtn = $('#j-login-btn');

jQloginBtn.bind('click', function () {
    var username = jQusrInput.val();
    var password = jQpswInput.val();
    $.post('/m/dispatcher/login/', {
        username: username,
        password: password
    }, function (ret) {
        if (ret.code == 0) {
            var dispatcherId = ret.dispatcher
            window.location.href = '/m/list/' + dispatcherId;
        } else {
            alert(ret.msg);
        }
    })
})
