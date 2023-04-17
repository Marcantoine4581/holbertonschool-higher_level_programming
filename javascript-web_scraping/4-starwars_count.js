#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const bodyParse = JSON.parse(body);
    const resultList = bodyParse.results;
    for (let i = 0; i < resultList.length; i++) {
      const character = resultList[i].characters;
      for (let j = 0; j < character.length; j++) {
        if (character[j].endsWith('/18/')) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
