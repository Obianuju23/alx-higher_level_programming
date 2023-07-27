#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const URL = process.argv[2];
const file = process.argv[3];

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.createWriteStream(file, body, 'utf-8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
