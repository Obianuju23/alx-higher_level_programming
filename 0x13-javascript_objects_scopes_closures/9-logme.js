#!/usr/bin/node

let NumArg = 0;

exports.logMe = function (item) {
  console.log(NumArg + ':' + '' + item);
  NumArg++;
};
