//on your console
/*

*/
const myName = prompt("Tell me your name");
alert("Hello " + myName);

const body = document.body;  //this stores document.body in a variable, so we can rewrite
const btn = document.createElement("button");    //this creates a button element
button.setAttribute('id', 'primary-btn')  //this adds attribute to the button
const btnText = document.createTextNode("click me");   // this writes text for the button element you created
button.append(btnText);    //this then writes/appends/add the text to the button element
//document.body.appendChild(button);   //this adds the button to the body/document - it adds the button to our page
body.appendChild(btn); //this is same as the line above it  but this adds the button below the script tag




const division = document.createElement("div");
const para = document.createElement("p");
para.innerHTML =  "Explaining paragraph";   //this adds text to the para/p you just created
division.appendChild(para);  //this adds the para/p to the div/division
body.appendChild(division);   //this adds the div element to the document/body.... recall we created a variable body = document.body
