#!/usr/bin/node

const Arg1 = parseInt(process.argv[2]);

function factorial(num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}

const result = factorial(Arg1);
console.log(result);
