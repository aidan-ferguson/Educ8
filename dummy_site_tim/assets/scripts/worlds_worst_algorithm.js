
/*
  World's Least Efficient Seed Algorithm
  By Timothy Wang 2022

  Takes an input string and generates 3 integer values
  between 120 and 255.
  Changes the background colour of the target element.

  Very slow and inefficient and doesn't generate quite as randomly as possible.
  However, it works "well enough" ¯\_(ツ)_/¯
*/

function timGenerator(seedString, target) {

  // Function to convert an integer to only its last three digits
  function lastThreeDigits(num) {
    num = num.toString();
    return parseInt(num.substr(num.length-3, num.length));
  }

  // Function to reverse the digits of an integer
  function reverseNum(num) {
    num = num.toString().split("").reverse().join("");
    return parseInt(num);
  }

  // Function to convert a string to a number in between 120 and 255
  // Takes the sum of each character's ASCII code, then use the last 3 digits
  // If the resulant number is too large do "stuff" to it then try again
  function toNum(text) {
    var sum = 0;
    for (var i=0; i<text.length; i++) {
      sum += text.charCodeAt(i);
    }
    sum = lastThreeDigits(sum);
    while (sum > 119) {
      sum = sum*2+lastThreeDigits(reverseNum(sum)*7);
      console.log(sum);
      if (lastThreeDigits(sum) <= 119) {
        break;
      }
    }
    return lastThreeDigits(sum) + 135;
  }

  // Split text into three more-or-less-equal substrings, remove all spaces and whitespace
  var text = seedString;
  var leftSubstring = text.substring(0, Math.round(text.length/3)).replace(/ /g,'').toLowerCase();
  var midSubstring = text.substring(Math.round(text.length/3), Math.round(text.length/3)*2).replace(/ /g,'').toLowerCase();
  var rightSubstring = text.substring(Math.round(text.length/3)*2+1, text.length).replace(/ /g,'').toLowerCase();

  // Pass each substring into the value to get RGB values
  target.css("background-color", `rgb(${toNum(leftSubstring)}, ${toNum(midSubstring)}, ${toNum(rightSubstring)})`);
  console.log(toNum(leftSubstring), toNum(midSubstring), toNum(rightSubstring))

}
