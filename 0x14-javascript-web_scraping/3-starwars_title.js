#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api/films/';
const epNo = process.argv[2];

request(API_URL + epNo, function (err, response, body) {
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else if (err) {
    console.log(err);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
