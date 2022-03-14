
/*
  World's Least-Efficient Seed Algorithm
  By Timothy Wang 2022

  Takes an input string and generates 3 integer values
  between 120 and 255.
  Changes the background colour of the target element.

  Slow and inefficient, it doesn't really generate quite as randomly as possible.
  However, it works well enough ¯\_(ツ)_/¯
*/

// seedString is the String input used to generate the colour
// target is the jQuery element which will have its background colour attribute modified
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

  // Function to convert a string to a number in between 130 and 255
  // Takes the sum of each character's ASCII code, then use the last 3 digits
  // If the resulant number is too large do "stuff" to it then try again
  function toNum(text) {
    let sum = 0;
    for (let i=0; i<text.length; i++) {
      sum += text.charCodeAt(i);
    }
    sum = lastThreeDigits(sum);
    while (sum > 109) {
      // The "stuff"
      sum = sum*2+lastThreeDigits(reverseNum(sum)*7);
      console.log(sum);
      if (lastThreeDigits(sum) <= 109) {
        break;
      } else if (sum > 1000000) {
        // Just to keep things under control
        sum = Math.round(Math.sqrt(sum));
        //console.log(sum);
      }
    }
    return lastThreeDigits(sum) + 145;
  }

  // Split text into three more-or-less-equal substrings, remove all spaces and whitespace
  let text = seedString;
  if (text.length < 10) {
    // Make the seed more interesting if the text is too short
    text += "i <3 javascript" + text;
  }
  const leftSubstring = text.substring(0, Math.round(text.length/3)).replace(/ /g,'');
  const midSubstring = text.substring(Math.round(text.length/3), Math.round(text.length/3)*2).replace(/ /g,'');
  const rightSubstring = text.substring(Math.round(text.length/3)*2+1, text.length).replace(/ /g,'');

  // Pass each substring into the value to get RGB values
  target.css("background-color", `rgb(${toNum(leftSubstring)}, ${toNum(midSubstring)}, ${toNum(rightSubstring)})`);

}
