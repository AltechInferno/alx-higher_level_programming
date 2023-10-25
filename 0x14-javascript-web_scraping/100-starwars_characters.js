#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

request(apiUrl + movieId, function (err, response, body) {
  if (err) {
    console.log(error);
  }
  JSON.parse(body).characters.forEach(function (apiUrl, callback) {
    request(apiUrl, function (err, response, body) {
      if (err) {
        console.error(err);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
