#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const w = this.width;
    const h = this.height;
    for (let i = 0; i < h; i++) {
      let result = '';
      for (let j = 0; j < w; j++) {
        result += 'X';
      }
      console.log(result);
    }
  }

  rotate () {
    const w = this.width;
    const h = this.height;
    this.width = h;
    this.height = w;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
