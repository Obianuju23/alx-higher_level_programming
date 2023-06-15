#!/usr/bin/node
const dict = require('./101-data').dict;
const NewDict = {};
let key;
for (key in dict) {
//Object.keys(dict).map(function (key, index) {
  if (NewDict[dict[key]] === undefined) {
    NewDict[dict[key]] = [];
  }
  NewDict[dict[key]].push(key);
}

console.log(NewDict);
