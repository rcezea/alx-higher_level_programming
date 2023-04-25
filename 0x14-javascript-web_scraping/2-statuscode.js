#!/usr/bin/node
const request = require('request');
require('process');
request.get(process.argv[2], function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ', response.statusCode);
  }
});
