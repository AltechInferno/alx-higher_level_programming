#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2]
fs.readFile(filePath, 'utf8', function (err, contents) {
  if (contents === undefined) {
    console.log(err);
  } else {
    console.log(contents);
  }
});
