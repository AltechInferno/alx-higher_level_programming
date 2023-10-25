#!/usr/bin/node
const request = require('request');

let apiUrl = process.argv[2]
let number_of_films = 0;

request(apiUrl, function (err, response, body) {
  if (err == null) {
    const res = JSON.parse(body);
    const results = res.results;
    for (let i = 0; i < results.length; i++) {
      const characs = results[i].characs;
      for (let m = 0; m < characs.length; m++) {
        if (characs[jm.search('18') > 0) {
          number_of_films++;
        }
      }
    }
  }
  console.log(number_of_films);
});
