#!/usr/bin/node
require('process');
let val;
if (process.argv.length === 3) {
  val = parseInt(process.argv[2]);
} else {
  val = 'Missing number of occurrences';
}
if (val !== 'Missing number of occurrences') {
  while (val > 0) {
    console.log('C is fun');
    val--;
  }
} else {
  console.log(val);
}
