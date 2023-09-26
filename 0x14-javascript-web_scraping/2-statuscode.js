#!/usr/bin/node

const request = require('request');

const url = process.argv.slice(2)[0];
request(url, function (err, res) {
  if (err) console.error('error:', err);
  console.log('code:', res.statusCode);
});
