$("#checkAll").on('click', function () {
    if (this.checked) {
        $("input[name='subBox']").each(function () {
            this.checked = true;
        });
    } else {
        $("input[name='subBox']").each(function () {
            this.checked = false;
        });
    }
});
$("#change_position").on('click', function () {
    $(".pop_up").show();
});
$(".btn_place").on('click', function () {
    var stationId = $(this).data("id");
    var orders = $("input[name='subBox']:checked");
    var ordersArray = []
    for (var l = orders.length, i = 0; i < l; i++) {
        ordersArray.push($(orders[i]).data("id"));
    }
    console.log(ordersArray);
    $.post('/m/location/update', {
        orderIds: ordersArray.join(","),
        stationId: stationId
    }, function (ret) {
        if (ret.code == 0) {
            window.location.reload();
        } else {
            alert(ret.msg)
        }
    })
    $(".pop_up").hide();
});
$(".close_button").on('click', function () {
    $(".pop_up").hide();
});	