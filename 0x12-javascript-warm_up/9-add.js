#!/usr/bin/node
require('process');

function add(x, y) {
  console.log(parseInt(x) + parseInt(y));
}

let x = parseInt(process.argv[2]);
let y = parseInt(process.argv[3]);

add(x,y);
