/*
const name = "Merit Ishekwene"
  let age = 25
  console.log("Hello " + name + " " + age)
//   you can use comma to concatenate in place of the plus sign
age = 26
console.log("Hello " , name + " " , age)
// write a prigram that counts
// javascript is dynamically typed i.e. the type of data you store inside a variable is determined at run time
let count = 1
while (count < 10)
{
    console.log(count)
    count = count + 1
}
*/
/*
datatype
-string - single, double or triple quote
-numbers
-boolean (true, false)
-arrays - []
-objects - {}

OPEERATORS
Arithmetic: +, -, /, *
Assignment: =, +=, -=, /=, *=
Comparison: ==, ===, <, >, >=, <=, !=, !==
Logical: &&, ||, !
Type operators: typeof, instanceof
== equal to
=== strictly equal to

CONTROL STATEMENT: it gives us control in the program
we can use the if statement
*/
const fruits = ['apples', 'berries', 'oranges']
const car = ['benz', 'telsa', 'toyota']
const items = [car, 56, {age: 34}, true]
console.log(items)
//objects in javascript are made up of key value pair
const person = {
    name: 'Merit',
    age: 34,
    height: 5,
    salary: 30000,
    currency: 'usd',
}


//PROJECT - JAVASCRIPT WARM UP
//RESOURCES
//Functions often take arguments: bits of data they need to do their job. Arguments go inside the parentheses, separated by commas if there is more than one argument.
/*
we create a simple function which takes two numbers as arguments and multiplies them:
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
//function call
multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);
DATA TYPES
-Arrays; An array is a single object that contains multiple values enclosed in square brackets and separated by commas.
et myNameArray = ["Chris", "Bob", "Jim"];
let myNumberArray = [10, 15, 40];
myNameArray[0]; // should return 'Chris'
myNumberArray[2]; // should return 40
-Object:
let dog = { name: "Spot", breed: "Dalmatian" };
To retrieve the information stored in the object, you can use the following syntax:
dog.name;

myNumber = 500; // much better — now this is a number
typeof myNumber;

Another example:
const bird = { species: "Kestrel" };
console.log(bird.species); // "Kestrel"
You can update, add, or remove properties of an object declared using const, because even though the content of the object has changed, the constant is still pointing to the same object:
bird.species = "Striated Caracara";
console.log(bird.species); // "Striated Caracara"

Conceptually, undefined indicates the absence of a value, while null indicates the absence of an object

BigInt type:
A BigInt is created by appending n to the end of an integer or by calling the BigInt() function.

When representing dates, the best choice is to use the built-in Date utility in JavaScript.

//Precedence
a OP1 b OP2 c
(a OP1 b) OP2 c
a OP1 (b OP2 c)
If OP1 and OP2 have different precedence levels (see the table below), the operator with the higher precedence goes first and associativity does not matter. 
Within operators of the same precedence, the language groups them by associativity. Left-associativity (left-to-right) means that it is interpreted as (a OP1 b) OP2 c, while right-associativity (right-to-left) means it is interpreted as a OP1 (b OP2 c). Assignment operators are right-associative, so you can write:
a = b = 5; // same as writing a = (b = 5);
const a = 4 ** 3 ** 2; // Same as 4 ** (3 ** 2); evaluates to 262144
const b = 4 / 3 / 2; // Same as (4 / 3) / 2; evaluates to 0.6666...
As another example, the unique exponentiation operator has right-associativity, whereas other arithmetic operators have left-associativity.
const a = 4 ** 3 ** 2; // Same as 4 ** (3 ** 2); evaluates to 262144
const b = 4 / 3 / 2; // Same as (4 / 3) / 2; evaluates to 0.6666...
Operators are first grouped by precedence, and then, for adjacent operators that have the same precedence, by associativity. So, when mixing division and exponentiation, the exponentiation always comes before the division. For example, 2 ** 3 / 3 ** 2 results in 0.8888888888888888 because it is the same as (2 ** 3) / (3 ** 2).


while (x < 10) {
  x++;
}
Here, { x++; } is the block statement.

A conditional statement is a set of commands that executes if a specified condition is true. JavaScript supports two conditional statements: if...else and switch.
An if statement looks like this:
if (condition) {
  statement1;
} else {
  statement2;
}


if (condition1) {
  statement1;
} else if (condition2) {
  statement2;
} else if (conditionN) {
  statementN;
} else {
  statementLast;
}

In general it's good practice to not have an if...else with an assignment like x = y as a condition:
if (x = y) {
  // statements here
}
use the while instead I think

-switch statement
switch (expression) {
  case label1:
    statements1;
    break;
  case label2:
    statements2;
    break;
  // …
  default:
    statementsDefault;
}
*/

/*
-DATA TYPES
NaN ("Not a Number") is a special kind of number value that's typically encountered when the result of an arithmetic operation cannot be expressed as a number. It is also the only value in JavaScript that is not equal to itself.
-BigInts - With BigInts, you can safely store and operate on large integers even beyond the safe integer limit (Number.MAX_SAFE_INTEGER) for Numbers. A BigInt is created by appending n to the end of an integer or by calling the BigInt() function. A TypeError is thrown if BigInt values are mixed with regular numbers in arithmetic expressions, or if they are implicitly converted to each other.
*/

//LIVE LEARNING SESSION
//-object im js
let personn = {
  namee: 'merit',
  age: '25',
  'date of birth': '0911'
};
console.log(personn.namee)
console.log(personn['age'])
console.log(personn['date of birth'])
personn.city = 'Ughelli'; //adds to the object
personn['school'] = 'ALX'  //adds to the object
console.log(personn);

//FUNCTIONS
function myfunction(x, y) {
  return (x + y);
}

let sum = myfunction(2, 5);
console.log(sum);

//importing the function, you can check how to import function in js
module.exports = {myfunction}



#!/usr/bin/node
export function add(num1, num2) {
  sum = num1 + num2
  return sum
};