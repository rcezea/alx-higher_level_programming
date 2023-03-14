#!/usr/bin/node
require('process');
let i;
for (i = 0; process.argv[i]; i++);
if (i > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
