#!/usr/bin/node

const req = require('request')   //this means you are requiring the request module
req.get('https://swapi.dev/api/people/1', { encoding: 'utf-8'})
 .on('data', (data) => {
    console.log(data);
 });