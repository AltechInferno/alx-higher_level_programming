#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2]
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

function supportRequest (arr, i) {
  if (i === arr.length) {
    return;
  }
  request(arr[i], function (err, response, body) {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).name);
    supportRequest(arr, i + 1);
  });
}

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const charac = JSON.parse(body).characters;
  supportRequest(charac, 0);
});
