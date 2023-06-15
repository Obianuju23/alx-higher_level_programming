#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    } else {
      let num = 0;
      while (num < this.width) {
        console.log(c.repeat(this.width));
        num++;
      }
    }
  }
}
module.exports = Square;
