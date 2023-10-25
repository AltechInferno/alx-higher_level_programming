#!/usr/bin/node
const url = process.argv[2]
const request = require('request');
const fs = require('fs');

request(url, function (err, response, body) {
  if (err == null) {
    fs.writeFileSync(process.argv[3], body);
  }
});
