#!/usr/bin/node

const Arg1 = process.argv;
const arrArgv = Arg1.slice(2);

function secondBiggest (arr) {
  if (arr.length < 2) {
    return (0);
  } else {
    arr.sort((a, b) => b - a);
    // This sorts in ascending order
    return (arr[1]);
  }
}
console.log(secondBiggest(arrArgv));
