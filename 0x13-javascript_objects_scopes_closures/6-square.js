#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super(size, size);
    this.height = size;
    this.width = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let result = '';
        for (let j = 0; j < this.width; j++) {
          result += c;
        }
        console.log(result);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
