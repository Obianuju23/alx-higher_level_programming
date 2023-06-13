#!/usr/bin/node

const Arg1 = process.argv[2];

if (isNaN(parseInt(Arg1))) {
  console.log('Not a number');
} else {  
  console.log('My number: ' + parseInt(Arg1));
} 
