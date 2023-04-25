#!/usr/bin/node
const request = require('request');
require('process');
request(process.argv[2], function (error, response) {
  console.log('code: ', response.statusCode);
});
