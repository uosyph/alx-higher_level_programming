#!/usr/bin/node

const fs = require('fs');

const file = process.argv.slice(2)[0];
const msg = process.argv.slice(2)[1];
fs.writeFile(file, msg, function (err) {
  if (err) console.log(err);
});
