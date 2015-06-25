$('#j-intro-nav li').bind('click', function() {
	var jQself = $(this);
	var intro = jQself.data('intro');
	jQself.addClass('active').siblings().removeClass('active');
	$('.intro').hide();
	$('#'+intro).show();
});