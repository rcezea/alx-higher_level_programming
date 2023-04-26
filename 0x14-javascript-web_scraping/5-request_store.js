#!/usr/bin/node
const request = require('request');
require('process');
const url = process.argv[2];
fs = require('fs');
request(url, function (err, resp, body) {
    if (err) {
        console.log(err)
    } else {
        fs.writeFile(process.argv[3], body, err => {
            if (err) {
              console.log(err);
            }
          });
    }
})
