#!/usr/bin/node

const request = require('request');

const files = process.argv.slice(2);
request(files[0], function (err, res) {
  if (err) console.error('error:', err);
  console.log('code:', res.statusCode);
});
