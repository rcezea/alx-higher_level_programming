#!/usr/bin/node
require('process');
let val;
let x = 'X'
if (process.argv[2]) {
  if (parseInt(process.argv[2])) {
    val = parseInt(process.argv[2]);
  } else {
    val = 'Missing size';
  }
} else {
  console.log('Missing size');
  return;
}
let i = val;
while (i > 0) {
  console.log(x.repeat(val));
  i--;
}
