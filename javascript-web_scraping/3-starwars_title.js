#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/' + id, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const bodyParse = JSON.parse(body);
    console.log(bodyParse.title);
  }
});
