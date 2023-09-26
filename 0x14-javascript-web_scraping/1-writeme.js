#!/usr/bin/node

const fs = require('fs');

const files = process.argv.slice(2);
fs.writeFile(files[0], files[1], function (err) {
  if (err) console.log(err);
});
