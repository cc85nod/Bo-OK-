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