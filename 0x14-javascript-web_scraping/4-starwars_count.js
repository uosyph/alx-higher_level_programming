#!/usr/bin/node

const request = require('request');

let data;
let count = 0;
const api = process.argv.slice(2)[0];
request(api, function (err, res, body) {
  if (err) console.error(err);
  else {
    data = JSON.parse(body);
    for (const result in data.results) {
      if (data.results[result].characters.filter(x => x.includes('18')).length > 0) count++;
    }
    console.log(count);
  }
});
