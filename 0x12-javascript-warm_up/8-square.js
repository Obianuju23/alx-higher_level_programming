#!/usr/bin/node
const Arg1 = process.argv[2];

if (isNaN(parseInt(Arg1))) {
  console.log('Missing size');
} else {
  const x = Number(Arg1);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
