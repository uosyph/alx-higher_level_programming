#!/usr/bin/node

const request = require('request');

const movieId = process.argv.slice(2)[0];
request(`https://swapi-api.alx-tools.com/api/films/${movieId}`,
  function (err, res, body) {
    if (err) console.error(err);
    else console.log(JSON.parse(body).title);
  });
