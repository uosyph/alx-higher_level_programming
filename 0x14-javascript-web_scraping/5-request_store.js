#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const api = process.argv.slice(2)[0];
const file = process.argv.slice(2)[1];
request(api, function (err, res, body) {
  if (err) console.error(err);
  else {
    fs.writeFile(file, body, function (err) {
      if (err) console.error(err);
    });
  }
});
