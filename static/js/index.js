$(window).scroll(function() {
	var sticky = $('.header'),
		scroll = $(window).scrollTop();

	if (scroll >= 200) {
		sticky.addClass('color_header')
	} else {
		sticky.removeClass('color_header')
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
	$('.menu-btn-left').click(function() {
	var currentT = $('.menu-row').css('transform').split(/[()]/)[1];
		var posX = currentT.split(',')[4];
		var left_offset = parseInt(posX) + 100;
		var right_offset = parseInt(posX) - 100;
		
		console.log('translateX('+ left_offset +')');
		$('.menu-row').animate({
			transform: 'translateX('+ left_offset +')'
		}, 'slow');
	});
	$('.menu-btn-right').click(function() {
		$('.menu-row').animate({
			
		}, {
			step: function() {
				$(this).css('transform', 'translateX('+ right_offset +')');
			},
			duration: 'slow',
		}, 'linear');
	});
})