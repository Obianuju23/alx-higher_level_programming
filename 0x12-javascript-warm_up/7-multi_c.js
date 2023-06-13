#!/usr/bin/node

const Arg1 = process.argv[2];

if (!isNaN(parseInt(Arg1))) {
  const x = parseInt(Arg1);

  for (let i = 0; i < x; i++) {
    console.log('C if Fun');
  }
} else {
  console.log('Missing number of occurrences');
}
