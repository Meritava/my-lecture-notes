#!/usr/bin/node
// this means you are requiring the request module
const req = require('request');
const id = process.argv[2];
const url = `https://swapi.dev/api/people/${id}`

//on is a function or you can call it an event, and data in semi colomn is the argument which on listens to, and the data in a bracket is an arrow function, it's a closure to the on function
req.get(url, { encoding: 'utf-8'})
 .on('data', (data) => {
   const response = JSON.parse(data);  //converst the JSON data to an object, so as to access individual properties
   //  console.log(data);
   console.log(response.name + " " + response.height);
   console.log("Character name: ", response.name)
 });



/*
 from my task 1
 const request = require('request');
const url = `${process.argv[2]}`
request.get(url)
 .on(('response', response => {
    console.log('code: ', response.statusCode)
 }))
 */

 