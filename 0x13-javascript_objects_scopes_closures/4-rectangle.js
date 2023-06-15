#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let num = 0;
    while (num < this.height) {
      console.log('X'.repeat(this.width));
      num++;
    }
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
