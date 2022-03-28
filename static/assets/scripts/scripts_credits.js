/* WAD2 Team Project "Educ8" | Course Page Visual Scripts */

$(document).ready(function(){

  // Fade credits on scroll
  $(window).scroll(function() {

    $('.fade').each(function() {
      var bottom_of_element = $(this).offset().top + $(this).outerHeight();
      var bottom_of_window = $(window).scrollTop() + $(window).height();
      if(bottom_of_window > bottom_of_element) {
        $(this).animate({'opacity':'1','margin-left':'0px'}, 2000);
      }
    });

  });

  // Roll credits
   $("html, body").animate({ scrollTop: $(document).height() }, 30000, "linear");

});
