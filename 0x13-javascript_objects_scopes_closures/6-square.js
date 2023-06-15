#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let count = 0;
      while (count < this.width) {
        console.log(c.repeat(this.width));
        count++;
      }
    }
  }
}
module.exports = Square;
