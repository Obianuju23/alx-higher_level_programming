#!/usr/bin/node

const Arg1 = process.argv[2];
const Arg2 = process.argv[3];

function add (a, b) {
  const c = a + b;
  console.log(c);
}

add(Number(Arg1), Number(Arg2));
