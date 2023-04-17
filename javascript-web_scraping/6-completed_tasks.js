#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const bodyParse = JSON.parse(body);
    const newDict = {};
    for (let i = 0; i < bodyParse.length; i++) {
      if (bodyParse[i].completed === true) {
        if (!newDict[bodyParse[i].userId]) {
          newDict[bodyParse[i].userId] = 0;
        }
        newDict[bodyParse[i].userId]++;
      }
    }
    console.log(newDict);
  }
});
