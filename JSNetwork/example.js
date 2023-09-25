#!/usr/bin/node
const request = require('request');
const url = `https://swapi.dev/api/people/1`
request.get(url, function(response, error, body) {
    console.log('Status Code: ', response.statusCode);
    const object_body = JSON.parse(body);
    console.log(object_body.name);
    //console.log(object_body.result) - to get the result property that is in our data
    /*
    //object_body.result.forEach(function (film) {
        //console.log(film.title);
    //})
    */
});