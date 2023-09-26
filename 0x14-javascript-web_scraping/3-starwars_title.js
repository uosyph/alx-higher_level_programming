#!/usr/bin/node

const request = require('request');

const files = process.argv.slice(2);
request('https://swapi-api.alx-tools.com/api/films/' + files[0],
  function (err, body) {
    if (err) console.error('error:', err);
    else console.log(JSON.parse(body).title);
  });
