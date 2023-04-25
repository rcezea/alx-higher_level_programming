#!/usr/bin/node
const request = require('request');
require('process');
if (process.argv.length - 2 == 0) {
    return;
}
request(process.argv[2], function (error, response) {
  console.log('code: ', response.statusCode);
});
