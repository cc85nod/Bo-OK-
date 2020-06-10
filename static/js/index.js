
$(document).ready(function() {
	$("header").mouseover(function() {
		$(this).addClass("color_header");
	});

	$("header").mouseleave(function() {
		var scroll = $(window).scrollTop();
		
		if (scroll < 200) {
			$(this).removeClass("color_header");
		}
	});

	
})


$(window).scroll(function(e) {
	var sticky = $('.header'),
		scroll = $(window).scrollTop();

	if (scroll >= 200) {
		sticky.addClass('color_header');
	} else {
		sticky.removeClass('color_header');
	}
})

$(function () {
	var images = [
		'read-0.jpg',
		'read-1.jpg',
		'read-2.jpg',
		'read-3.jpg'
	];

	var imgn = Math.floor(Math.random() * images.length);

	$(".jumbotron").css({
		"background-image": "linear-gradient(rgba(255,255,255,0.25), rgba(255,255,255,0.25)), url('/static/images/"+images[imgn]+"')",
		"background-size": "cover"
	});
})

function search_empty() {
	var x = document.getElementById('book_name').value;
	console.log(x);
	if(x == "") {
		return false;
	}
	return true;
}

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

function validateEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function checkEmail() {
	var email = document.getElementById('email').value;

	if (!validateEmail(email)) {
		alert("請輸入正確格式的 Email");
		return false;
	}
	alert("成功！");
	return true;
}