#!/usr/bin/node

const index = process.argv;
if (index[2]) {
  console.log(index[2]);
} else {
  console.log('No Argument');
}
