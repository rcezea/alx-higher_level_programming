#!/usr/bin/node
const request = require('request');
require('process');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.endsWith('18/')) {
        count += 1;
        break;
      }
    }
  }
  console.log(count);
});
