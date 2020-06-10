
$(document).ready(function() {
	$("header").mouseover(function() {
		$(this).addClass("color_header");
	});

	$("header").mouseleave(function() {
		$(this).removeClass("color_header");
	});
})

$(function () {
	$(".jumbotron").css({
		"background-image": "linear-gradient(rgba(255,255,255,0.6), rgba(255,255,255,0.6)), url('/static/images/coffee.jpg')",
		"background-size": "cover",
		"height": "100%",
		"background-position": "center",
		"background-repeat": "no-repeat",
	});
})


$(document).ready(function() {
	var item_count = $('.menu .col-md-4').length;
	
	$('.menu-btn-left').click(function() {
		var carsize = $('.menu .col-md-4').width();
		var currentT = $('.menu-row').css('transform').split(/[()]/)[1];
		var posX = currentT.split(',')[4];
		var left_offset = parseInt(posX) + parseInt(carsize) + 30;

		if (parseInt(posX)*-1 >= 0) {
			$('.menu-row').css(
				"transform", "translateX("+left_offset+"px)"
			);
		}
	});

	$('.menu-btn-right').click(function() {
		var item_count = parseInt($('.menu .col-md-4').length) - 2;
		var carsize = $('.menu .col-md-4').width();
		var currentT = $('.menu-row').css('transform').split(/[()]/)[1];
		var posX = currentT.split(',')[4];
		var right_offset = parseInt(posX) - parseInt(carsize) - 30;

		if (parseInt(posX)*-1 <= (parseInt(carsize)+30)*(parseInt(item_count)-1)) {
			$('.menu-row').css(
				"transform", "translateX("+right_offset+"px)"
			);
		}
	});
})