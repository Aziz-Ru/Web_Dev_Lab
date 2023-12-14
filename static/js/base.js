// var prevScrolpos = window.screenY;

// window.addEventListener("scroll", () => {
//   console.log(prevScrolpos);
//   var currenScrolpos = window.screenY;
//   if (prevScrolpos > currenScrolpos) {
//     document.getElementById("navlinks").style.top = "0";
//   } else {
//     document.getElementById("navlinks").style.top = "-50px";
//   }
//   prevScrolpos = currenScrolpos;
// });

const textNode = document.createTextNode("Hello World!This javascript");
const newParagraph = document.createElement("p");
newParagraph.appendChild(textNode);
document.body.appendChild(newParagraph);
