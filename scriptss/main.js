/*
const myHeading = document.querySelector("h1");
myHeading.textContent = "Hello world!";
let myVariable = "Merit";
myVariable = "Ava";
document.querySelector("html").addEventListener("click", function () {
    alert("Ouch! Stop poking me!");
  });
  */
/*
  There are a number of ways to attach an event handler to an element. Here we select the <html> element. We then call its addEventListener() function, passing in the name of the event to listen to ('click') and a function to run when the event happens.

The function we just passed to addEventListener() here is called an anonymous function, because it doesn't have a name. There's an alternative way of writing anonymous functions, which we call an arrow function. An arrow function uses () => instead of function ():
*/
//   document.querySelector("html").addEventListener("click", () => {
//     alert("Ouch! Stop poking me!");
//   });

/*
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
  if (!myName) {
    setUserName();
  } else {
    localStorage.setItem("name", myName);
    myHeading.textContent = `Mozilla is cool, ${myName}`;
  }
}
if (!localStorage.getItem("name")) {
  setUserName();
} else {
  const storedName = localStorage.getItem("name");
  myHeading.textContent = `Mozilla is cool, ${storedName}`;
}
myButton.onclick = () => {
  setUserName();
};  
*/
  // live class
  // const name = "Merit Ishekwene"
  // let age = 25
  // console.log("Hello" + name)

  const buttonA = document.querySelector("#button_A");
const headingA = document.querySelector("#heading_A");

buttonA.onclick = () => {
  const name = prompt("What is your name?");
  alert(`Hello ${name}, nice to see you!`);
  headingA.textContent = `Welcome ${name}`;
};