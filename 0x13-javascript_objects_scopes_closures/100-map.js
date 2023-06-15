#!/usr/bin/node

const list = require('./100-data').list;
const NewList = list.map(function (num, index) {
  return num * index;
});

console.log(list);
console.log(NewList);
