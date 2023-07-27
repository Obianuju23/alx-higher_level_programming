#!/usr/bin/node

const request = require('request');
const epiNum = process.argv[2];
const API_URL = 'https://swapi-api.alx-tools.com/api/films/' + epiNum;
request(API_URL, function (err, respobse, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
