/* WAD2 Team Project "Educ8" | Global Visual Scripts */

$(document).ready(function(){


	// Animate scrolling on buttons
	$('a[href*="#"]').on('click', function (e) {
		$('html, body').animate({
			scrollTop: $($(this).attr('href')).offset().top
		}, 600, 'swing');
	});


	// Back to top button
	var btn = $('#back2top');
	$(window).scroll(function() {
	  if ($(window).scrollTop() > 300) {
		btn.addClass('show');
	  } else {
		btn.removeClass('show');
	  }
	});
	btn.on('click', function(e) {
	  e.preventDefault();
	  $('html, body').animate({scrollTop:0}, '300');
	});


});
