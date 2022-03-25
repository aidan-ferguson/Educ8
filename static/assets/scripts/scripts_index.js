/* WAD2 Team Project "Educ8" | "My Courses" Page Visual Scripts */

$(document).ready(function(){

  // Cat
  $("#activate_cat").click(function() {
    $(".cat_use").slideToggle();
  });

  // Banner
  let bannerArray = [
    "Now with extra cheese!",
    "🍆🍆🍆🍆🍆",
    "a",
    "AAAAAAAAA",
    "Please do not hack!",
    "Educ8ing since 2022!",
    "The one and only!",
    "Now in 4 sizes!",
    "Coming soon to a cinema near you!",
    "thereisnocatthereisnocatthereisnocatthereisnocatthereisnocat",
    "Get Educ8'd!",
    "Brought to you with <3!",
    "Better than M00dle!",
    "Always one step behind!",
    "GOLP",
    "Eggplants included!",
    "404: Banner not found.",
    "Educ8 or nothin'!",
    "Hello World!",
    "A Gr8 Time to Educ8!",
  ]
  let bannerText = bannerArray[Math.floor(Math.random()*bannerArray.length)];
  $("#banner").text(bannerText);

});
