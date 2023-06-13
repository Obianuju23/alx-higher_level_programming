#!/usr/bin/node

const Arg1 = process.argv[2];

let i = 0;
if (isNaN(parseInt(Arg1))) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(Arg1)) {
    console.log('C is fun');
    i++;
  }
}
