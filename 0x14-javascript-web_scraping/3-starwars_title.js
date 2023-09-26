#!/usr/bin/node

const request = require('request');

const id = process.argv.slice(2);
request('https://swapi-api.alx-tools.com/api/films/' + id[0],
  function (err, res, body) {
    if (err) console.error('error:', err);
    else console.log(JSON.parse(body).title);
  });
