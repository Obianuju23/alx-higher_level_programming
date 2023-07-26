#!/usr/bin/node

const fs = require('fs');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(argv[3], body, 'utf-8', function (error) {
      if (error) {
        console.error(error);
      }
    });
  }
});
