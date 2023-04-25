#!/usr/bin/node
const fs = require('fs');
const { encode } = require('querystring');
require('process');

fs.writeFile(process.argv[2], process.argv[3], err => {
  if (err) {
    console.log(err);
  }
});
