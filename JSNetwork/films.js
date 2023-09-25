#!/usr/bin/node
const request = require('request');
const url = `https://swapi.dev/api/films`;
request.get(url, { encoding: 'utf-8'})
 .on('data', data => {
   const object = JSON.parse(data);
   console.log(object.results)
 })
 .on('response', response => {
    console.log('Status code: ', response.statusCode)
 })
 .on('error', err => {
    console.log(err);
 })



 /*
const request = require('request');
const url = `https://swapi.dev/api/films`;
request.get(url, { encoding: 'utf-8'})
 .on('data', data => {
    console.log(data)
 })
 .on('response', response => {
    console.log(response.statusCode)   //response is an event
 })
 .on('error', err => {
    console.log(err);      //error is an event, on is a function
 })

//const url = `https://swapi.dev/api/films`;  this line is to get the films
//  .on('error', err => {
//    console.log(err);
//  })
//this is to listen to error, any error that comes in, log it for me, try typing the second on line immediately after the first one without comments on your code
*/