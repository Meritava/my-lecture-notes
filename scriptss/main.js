/*
const myHeading = document.querySelector("h1");
myHeading.textContent = "Hello world!";
let myVariable = "Merit";
myVariable = "Ava";
document.querySelector("html").addEventListener("click", function () {
    alert("Ouch! Stop poking me!");
  });
*/
//   document.querySelector("html").addEventListener("click", () => {
//     alert("Ouch! Stop poking me!");
//   });

const myImage = document.querySelector("img");

myImage.onclick = () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "image/firefox2.png") {
    myImage.setAttribute("src", "image/firefox2.png");
  } else {
    myImage.setAttribute("src", "image/firefox-icon.png");
  }
};

let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
    const myName = prompt("Please enter your name.");
    localStorage.setItem("name", myName);
    myHeading.textContent = `Mozilla is cool, ${myName}`;
  }
  

  // live class
  const name = "Merit Ishekwene"
  let age = 25
  console.log("Hello" + name)