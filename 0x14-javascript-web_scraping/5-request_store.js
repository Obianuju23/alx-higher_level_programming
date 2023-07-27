#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const URL = process.argv[2];
const file = process.argv[3];

request
  .get(URL)
  .on('err', err => console.log(err))
  .pipe(fs.createWriteStream(file));
